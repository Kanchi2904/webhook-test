from flask import Flask, request, jsonify

app = Flask(__name__)

# Base alert ID prefix (without version)
ALERT_ID_PREFIX = "11def244-307b-4dc9-9b38-85f153d21451"


# ---------- GLOBAL CORS HANDLER ----------
@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response


# ---------- ROUTE 1: Root health check ----------
@app.route('/', methods=['GET', 'OPTIONS'])
def root():
    if request.method == 'OPTIONS':
        return '', 200
    return jsonify({"message": "Webhook service is running"}), 200


# ---------- ROUTE 2: Handle incoming alert_id ----------
@app.route('/<alert_id>', methods=['POST', 'OPTIONS'])
def handle_alert_id(alert_id):
    # Handle CORS preflight (OPTIONS)
    if request.method == 'OPTIONS':
        return jsonify({'message': 'CORS preflight accepted'}), 200

    # Check if the alert_id starts with your known prefix
    if alert_id.startswith(ALERT_ID_PREFIX):
        # If it matches the blocked alert prefix → send 404
        print(f"Blocked alert_id received: {alert_id}")
        return jsonify({"error": "Invalid URL"}), 404

    # Otherwise, treat it as a valid webhook POST
    data = request.get_json(silent=True)
    print(f"Received valid alert_id: {alert_id}, data: {data}")
    return jsonify({"message": "Valid alert received", "alert_id": alert_id}), 200


# Render automatically uses gunicorn, so no need for app.run()
