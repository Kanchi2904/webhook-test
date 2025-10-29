from flask import Flask, request, jsonify

app = Flask(__name__)

# Base alert ID prefix (without version)
ALERT_ID_PREFIX = "11def244-307b-4dc9-9b38-85f153d21451"

# ---------- ROUTE 1: Generic echo ----------
@app.route('/webhook/echo', methods=['POST', 'OPTIONS'])
def echo():
    # Handle CORS preflight
    if request.method == 'OPTIONS':
        response = jsonify({'message': 'CORS preflight accepted'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response, 200

    # Handle normal POST
    data = request.get_json()
    print("Received POST data:", data)
    return jsonify({"message": "Webhook received successfully", "status": "OK"}), 200


# ---------- ROUTE 2: Alert ID-specific route ----------
@app.route('/webhook/echo/<alert_id>', methods=['POST', 'OPTIONS'])
def handle_alert_id(alert_id):  # <-- now includes alert_id parameter
    # Handle CORS preflight
    if request.method == 'OPTIONS':
        response = jsonify({'message': 'CORS preflight accepted'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response, 200

    # Check if alert_id starts with the base prefix
    if alert_id.startswith(ALERT_ID_PREFIX):
        print(f"Received blocked alert_id: {alert_id}")
        return jsonify({"error": "Invalid alert ID"}), 404

    # Otherwise, handle normally
    data = request.get_json()
    print(f"Received alert_id: {alert_id}, data: {data}")
    return jsonify({"message": "Valid alert received", "alert_id": alert_id}), 200


# Render automatically runs gunicorn, so no need for app.run()
