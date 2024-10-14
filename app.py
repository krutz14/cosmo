from flask import Flask, jsonify, request

app = Flask(__name__)

# Example data storage (in-memory, later replaced with Cosmocloud storage)
health_data = {
    "heart_rate": 72,
    "steps": 1000,
    "sleep_duration": 7,
    "weight": 70,
    "blood_pressure": "120/80"
}

# Route to get health data
@app.route('/health', methods=['GET'])
def get_health_data():
    return jsonify(health_data)

# Route to update health data
@app.route('/health', methods=['POST'])
def update_health_data():
    data = request.get_json()
    for key in health_data.keys():
        if key in data:
            health_data[key] = data[key]
    return jsonify(health_data)

if __name__ == "__main__":
    app.run(debug=True)
