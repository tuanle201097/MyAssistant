from flask import Flask, render_template
from flask_socketio import SocketIO
import subprocess
import os
import webbrowser

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('play_video')
def handle_play_video(url):
    print('Received play command:', url)
    # Mở URL trong Chrome
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    subprocess.Popen([chrome_path, url])

@socketio.on('stop_video')
def handle_stop_video():
    print('Received stop command')
    # Đóng Chrome (Windows)
    os.system("taskkill /IM chrome.exe /F")

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
