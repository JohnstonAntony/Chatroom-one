import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.secret_key = "battle_cats_key_2026"
socketio = SocketIO(app)

active_users = set() # Set to store active users

def init_db():
    connection = sqlite3.connect('chatroom.db')
    cursor = connection.cursor()

    # Drops and recreates login table to ensure a fresh table
    cursor.execute("DROP TABLE IF EXISTS LOGIN")
    cursor.execute("CREATE TABLE LOGIN(userid INTEGER, username TEXT, password TEXT)")
    
    users = [(1, 'carlos', 'bro1'), (2, 'johnston', 'bro2'), (3, 'dhaanish', 'bro3')]
    cursor.executemany("INSERT INTO LOGIN VALUES (?, ?, ?)", users)
    
    connection.commit()
    connection.close()

init_db()

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/login_check', methods=['POST'])
def login_check():
    user_value = request.form.get('username') # Grabs what the inputted username and password
    password_value = request.form.get('password')
    
    conn = sqlite3.connect('chatroom.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM LOGIN WHERE username=? AND password=?", (user_value, password_value))
    user = cursor.fetchone()
    conn.close()

    if user:
        session['username'] = user_value # This "saves" the login
        return redirect(url_for('room')) # Goes to next page
    else:
        error = "Incorrect Login Details"
        return render_template("login.html", error=error) #Wrong login details displays incorrect login details message

@app.route('/room')
def room():
    # Only allows entry if they logged in successfully
    if 'username' not in session:
        return redirect(url_for('login')) #Stay at login page
    return render_template("room.html", username = session['username']) # Shows chatroom + stores username in a readable form for HTML.

@socketio.on('message')
def handle_message(msg):
    print("server got:", msg)
    emit('message', msg, broadcast=True) 
    # this bit emits the message to everyone, read the pusedo code in the word doc to see what we should try. 

@socketio.on('connect')
def handle_connect(): # handles connect message when a user connects to the chatroom.
    username = session.get('username') # get's username from session.
    if username:
        active_users.add(username) # adds to 'set' 
        emit('user_list',list(active_users), broadcast=True) #sends to everyone, notice it's getting converted to a list because sets can't be sent as JSON.
        print(f"{username} connected. Active users: {active_users}")

@socketio.on('disconnect')
def handle_disconnect(): # handles disconnect message when a user disconnects from the chatroom.
    username = session.get('username')
    if username:
        active_users.discard(username)
        emit('user_list', list(active_users), broadcast=True)
        print(f"{username} disconnected. Active users: {active_users}")



if __name__ == '__main__':
    socketio.run(app, debug=True) # host = '0.0.0.0') #turned it off so I don't have to keep turning off my network firewall. 


