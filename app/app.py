from flask import Flask
import socket
import platform
from datetime import datetime
import os
from flask import jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():

    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def increment_visit_count():

    try:

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE visits SET visit_count = visit_count + 1 WHERE id = 1"
        )

        conn.commit()

        cursor.execute(
            "SELECT visit_count FROM visits WHERE id = 1"
        )

        count = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        return count
    
    except Exception as e:
        return f"Database Error: {e}"

@app.route('/')
def index():
    
    hostname = socket.gethostname()

    try:
        ip_address = socket.gethostbyname(hostname)
    except:
        ip_address = "Unavailable"
    


    os_info = platform.system()
    
    python_version = platform.python_version()

    platform_info = platform.platform()



    container_id = hostname[:12]  # Assuming container ID is the first 12 characters of the hostname
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    app_version = os.getenv('APP_VERSION', 'Unknown')

    visit_count = increment_visit_count()


    return f"""
    <html>
    <head> 
        <title>Dockerized System Information</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                margin: 0;
                padding: 20px;
            }}
            h1 {{
                color: #333;
            }}
            p {{    
                font-size: 18px;
                color: #555;
            }}
        </style>
    </head>
    <body>

        <h1>Dockerized System Information</h1> 
        <p><strong>Hostname:</strong> {hostname}</p>
        <p><strong>IP Address:</strong> {ip_address}</p>
        <p><strong>Operating System:</strong> {os_info}</p>
        <p><strong>Current Time:</strong> {current_time}</p>
        <p><strong>Python Version:</strong> {python_version}</p>
        <p><strong>Container ID:</strong> {container_id}</p>
        <p><strong>Application Version:</strong> {app_version}</p>
        <p><strong>Platform:</strong> {platform_info}</p>
        <p><strong>Visit Count:</strong> {visit_count}</p>
    </body>
    </html>
    """



@app.route('/health')
def health():

    return jsonify({
        "status": "healthy",
        "application": "Dockerized System Monitor"
    }), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)