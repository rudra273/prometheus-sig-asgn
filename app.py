from datetime import timedelta
import json
from flask import Flask, render_template, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_settings', methods=['POST'])
def update_settings():
    data = request.get_json()
    work_duration = int(data['workDuration'])
    break_duration = int(data['breakDuration'])
    return jsonify(work_duration=work_duration, break_duration=break_duration)

if __name__ == '__main__':
    app.run(debug=True)
