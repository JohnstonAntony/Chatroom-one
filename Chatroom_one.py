# pip install Flask
# pip install flask-socketio

# make sure to install both of these bro if pip isn't found in command try using pip3 install ... 

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template("login.html")

@socketio.on('message')
def handle_message(msg):
    emit('message', msg, broadcast=True) 
    # this bit emits the message to everyone, read the pusedo code in the word doc to see what we should try. 



if __name__ == '__main__':
    socketio.run(app, debug=True)

