from flask import Flask
import socket
import platform
from datetime import datetime
import os
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    
    hostname = socket.gethostname()

    try:
        ip_address = socket.gethostbyname(hostname)
    except:
        ip_address = "Unavailable"
    


    os_info = platform.system() + " " + platform.release()
    
    python_version = platform.python_version()
    


    container_id = hostname[:12]  # Assuming container ID is the first 12 characters of the hostname
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    app_version = os.getenv('APP_VERSION', 'Unknown')


    return f"""
    <h1>Dockerized System Information</h1> 
    <p><strong>Hostname:</strong> {hostname}</p>
    <p><strong>IP Address:</strong> {ip_address}</p>
    <p><strong>Operating System:</strong> {os_info}</p>
    <p><strong>Current Time:</strong> {current_time}</p>
    <p><strong>Python Version:</strong> {python_version}</p>
    <p><strong>Container ID:</strong> {container_id}</p>
    <p><strong>Application Version:</strong> {app_version}</p>
    """



@app.route('/health')
def health():

    return jsonify({
        "status": "healthy"
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)