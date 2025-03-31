from flask import Flask, jsonify, request
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)

# Mock vehicle detection function (will replace with actual YOLO integration)
def get_vehicle_counts():
    return {
        "north": 5,
        "east": 3,
        "south": 7,
        "west": 2
    }

# Signal timing algorithm
def calculate_signal_duration(counts):
    total = sum(counts.values())
    if total == 0:
        return {k: 15 for k in counts.keys()}
    
    return {
        direction: int(count/total * 60) 
        for direction, count in counts.items()
    }

@app.route('/api/detect', methods=['GET'])
def detect():
    counts = get_vehicle_counts()
    durations = calculate_signal_duration(counts)
    return jsonify({
        "counts": counts,
        "durations": durations
    })

@app.route('/api/control', methods=['POST'])
def control():
    data = request.json
    # In real implementation, this would control actual signals
    return jsonify({
        "status": "success",
        "message": f"Signal timing updated: {data}"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)