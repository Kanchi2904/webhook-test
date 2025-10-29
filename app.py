from flask import Flask, request, jsonify

app = Flask(__name__)

ALERT_ID = "11def244-307b-4dc9-9b38-85f153d21451_2"

# === Main Webhook Endpoint ===
@app.route('/webhook/echo', methods=['POST', 'OPTIONS'])
def echo():
    # Handle OPTIONS (preflight) request
    if request.method == 'OPTIONS':
        response = app.make_response('')
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response, 200

    # Handle POST request
    data = request.get_json()
    print("Received POST data:", data)
    return jsonify({"message": "Webhook received successfully", "status": "OK"}), 200


# === Alert ID Endpoint ===
@app.route(f'/webhook/echo/{ALERT_ID}', methods=['POST', 'OPTIONS'])
def handle_alert_id():
    # Handle OPTIONS (preflight) request
    if request.method == 'OPTIONS':
        response = app.make_response('')
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response, 200

    # Handle POST request for the specific alert_id
    return jsonify({"error": "Invalid alert ID"}), 404


# Render automatically runs gunicorn for Flask apps, so no need for app.run()
