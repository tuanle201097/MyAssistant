from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import subprocess
import os
import webbrowser

app = Flask(__name__)
socketio = SocketIO(app)

base_dir = os.path.dirname(os.path.abspath(__file__))
nircmd_path = os.path.join(base_dir, 'nircmd-x64', 'nircmd.exe')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('play_video')
def handle_play_video(url):
    print('Received play command:', url)
    # Mở URL trong Chrome
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    subprocess.Popen([chrome_path, url])
    # Gửi lại cho client thông báo
    emit('status_update', f'Playing video: {url}')

@socketio.on('stop_video')
def handle_stop_video():
    print('Received stop command')
    # Đóng Chrome (Windows)
    os.system("taskkill /IM chrome.exe /F")
    emit('status_update', 'Stopped video')

@socketio.on('volume_up')
def volume_up_func():
    subprocess.run([nircmd_path, 'changesysvolume', '6500'])
    print('Tang 10% am luong')
    # Gửi lại cho client thông báo
    emit('status_update', f'Da tang am luong')

@socketio.on('volume_down')

def volume_down_func():
    subprocess.run([nircmd_path, 'changesysvolume', '-6500'])
    print('Giam 10% am luong')
    # Gửi lại cho client thông báo
    emit('status_update', f'Da giam am luong')
 
@socketio.on('monitor_on')
def monitorOff_func():
    subprocess.run([nircmd_path, 'monitor', 'on'])

    subprocess.run([nircmd_path, 'sendmouse', 'move', '1', '1'])
    print('Monitor On')
    # Gửi lại cho client thông báo
    emit('monitor_update', f'Monitor On')

@socketio.on('monitor_off')
def monitorOn_func():
    subprocess.run([nircmd_path, 'monitor', 'off'])
    print('Monitor Off')
    # Gửi lại cho client thông báo
    emit('monitor_update', f'Monitor Off')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
