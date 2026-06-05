import flask # pyright: ignore[reportMissingImports]
import socket
import platform
from datetime import datetime

app = flask.Flask(__name__)

@app.route('/')
def index():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    os_info = platform.system() + " " + platform.release()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    python_version = platform.python_version()

    return f"""
    <h1>Dockerized System Information</h1> 
    <p><strong>Hostname:</strong> {hostname}</p>
    <p><strong>IP Address:</strong> {ip_address}</p>
    <p><strong>Operating System:</strong> {os_info}</p>
    <p><strong>Current Time:</strong> {current_time}</p>
    <p><strong>Python Version:</strong> {python_version}</p>
    """



@app.route('/health')
def health():
    return {"status": "healthy"}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)