import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.secret_key = "battle_cats_key_2026"
socketio = SocketIO(app)

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
        return redirect(url_for('login')) # Wrong? Just reloads login

@app.route('/room')
def room():
    # Only allows entry if they logged in successfully
    if 'username' not in session:
        return redirect(url_for('login')) #Stay at login page
    return render_template("room.html") # Shows chatroom

@socketio.on('message')
def handle_message(msg):
    print("server got:", msg)
    emit('message', msg, broadcast=True) 
    # this bit emits the message to everyone, read the pusedo code in the word doc to see what we should try. 



if __name__ == '__main__':
    socketio.run(app, debug=True)


