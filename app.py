# from flask import Flask
# import os
# from datetime import datetime
# import psutil

# app = Flask(__name__)

# @app.route('/htop')
# def htop():
    
#     username = os.getlogin()
   
#     ist_time = datetime.now().astimezone().isoformat()
    
   
#     cpu_usage = psutil.cpu_percent(interval=1)
#     memory_info = psutil.virtual_memory()
#     memory_usage = memory_info.percent
#     memory_available = memory_info.available
#     memory_total = memory_info.total
    
   
#     return f"""
#     <html>
#     <head>
#         <title>System Info</title>
#     </head>
#     <body>
#         <h1>System Info</h1>
#         <p><strong>Name:</strong>Harsh Kaushik</p>
#         <p><strong>Username:</strong> {username}</p>
#         <p><strong>Server Time (IST):</strong> {ist_time}</p>
#         <h2>System Resource Usage</h2>
#         <p><strong>CPU Usage:</strong> {cpu_usage}%</p>
#         <p><strong>Memory Usage:</strong> {memory_usage}%</p>
#         <p><strong>Memory Available:</strong> {memory_available / (1024 ** 2):.2f} MB</p>
#         <p><strong>Memory Total:</strong> {memory_total / (1024 ** 2):.2f} MB</p>
#     </body>
#     </html>
#     """

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
from flask import Flask
import os
import psutil
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def home():
    return "Internshhip Assignment Submitted by - Harsh Kaushik (ENG21CS0149)"


@app.route('/htop')
def htop():
    # Get system username
    username = os.getlogin()
    
    # Get current server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # Get process information similar to 'top' command
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent']):
        processes.append(proc.info)
    
    # Create a table for process information
    process_table = "<table ><tr><th>PID</th><th>Name</th><th>User</th><th>CPU%</th><th>Memory%</th></tr>"
    for proc in processes:
        process_table += f"<tr><td>{proc['pid']}</td><td>{proc['name']}</td><td>{proc['username']}</td><td>{proc['cpu_percent']}</td><td>{proc['memory_percent']}</td></tr>"
    process_table += "</table>"

    # HTML response with system and process info
    return f'''
    <html>
    <head>
        <title>System Info</title>
    </head>
    <body>
        <h1>System Info</h1>
        <p><strong>Name:</strong> Harsh Kaushik</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <h2>Top Output</h2>
        {process_table}
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
