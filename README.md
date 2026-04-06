-Chatroom One-

A live web chatroom built with Flask and Socket.IO. Users log in details is stored in SQLite and exchange messages instantly via WebSockets — no page refresh needed. Features a live online-user sidebar and a dark mode toggle that persists between sessions.

Built as a Team building and Learning project demonstrating full-stack fundamentals: server-side routing, WebSocket communication, session management, database interaction, and front-end design.

-Features-

Real-time messaging — Instant message broadcast to all connected users using WebSockets.
User authentication — SQLite-backed login with Flask session management.
Live online user list — Sidebar updates automatically as users join and leave.
Dark mode — Theme toggle with localStorage persistence across sessions to improve user usabilty. 


-Tech Stack-

Python 3.12 · Flask · Flask-SocketIO · SQLite · HTML/CSS/JS · Socket.IO


-Getting Started-

bash
git clone <your-repo-url>
cd Chatroom_one
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install flask flask-socketio
python chatroom_one.py


Then open http://127.0.0.1:5000. The database is rebuilt fresh on each server start with these placeholder logins:

| Username  | Password |
| carlos    | bro1     |
| johnston  | bro2     |
| dhaanish  | bro3     |



-Status-

Actively in development — CSS cleanup in progress, with responsive layout improvements and additional chat features (timestamps, logout, message history, attachements) on the roadmap as of 6/04/26.


