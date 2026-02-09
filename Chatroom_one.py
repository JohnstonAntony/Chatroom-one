# pip install Flask
# pip install flask-socketio

# make sure to install both of these bro if pip isn't found in command try using pip3 install ... 

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template("home.html")

if __name__ == '__main__':
    socketio.run(app, debug=True)

