from flask import Flask, request, jsonify

app = Flask(__name__)

# The specific alert_id that should trigger 404
TARGET_ALERT_ID = "1dc854de-c208-4c2e-83ce-9fc0aca69cc6_1"

@app.route('/webhook/echo', methods=['POST'])
@app.route('/webhook/echo/<alert_id>', methods=['POST'])
def echo(alert_id=None):
    data = request.get_json()
    print("Received POST data:", data)

    # Case 1: if the alert_id matches your test ID → simulate failure
    if alert_id == TARGET_ALERT_ID:
        print(f"Simulating 404 for alert_id: {alert_id}")
        return jsonify({
            "message": f"Alert ID {alert_id} not found",
            "status": "FAILED"
        }), 404

    # Case 2: any other alert_id (or none) → success
    return jsonify({
        "message": "Webhook received successfully",
        "status": "OK",
        "alert_id": alert_id
    }), 200
