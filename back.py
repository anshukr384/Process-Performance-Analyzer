from flask import Flask, render_template, jsonify
import psutil
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    # Get CPU usage over a 1-second interval for more accurate reading
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    processes = len(psutil.pids())
    time = datetime.now().strftime('%H:%M:%S')
    return jsonify({
        'cpu': round(cpu, 1),  # Round to 1 decimal place
        'memory': round(memory, 1),
        'processes': processes,
        'time': time
    })

if __name__ == '__main__':
    app.run(debug=True)