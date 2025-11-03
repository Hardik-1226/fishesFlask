from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

latest_data: dict = {}


@app.route('/')
def home():
    return jsonify({"message": "Mine Safety System Backend Running"})


@app.route('/data', methods=['POST'])
def receive_data():
    global latest_data
    try:
        data = request.get_json()
        if not isinstance(data, dict):
            raise ValueError('Invalid JSON payload')

        data['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        latest_data = data

        print("Data received from ESP32:", data)
        return jsonify({"status": "success", "message": "Data received successfully!"}), 200

    except Exception as e:
        print("Error receiving data:", str(e))
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/latest', methods=['GET'])
def send_latest_data():
    if not latest_data:
        return jsonify({"status": "error", "message": "No data received yet!"}), 404
    return jsonify(latest_data), 200


if __name__ == '__main__':
    # Bind to 0.0.0.0 so ngrok and external devices can reach the server
    app.run(host='0.0.0.0', port=5000, debug=True)