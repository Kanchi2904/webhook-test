from flask import Flask, request, jsonify

app = Flask(__name__)

ALERT_ID = "1dc854de-c208-4c2e-83ce-9fc0aca69cc6_1"

@app.route('/webhook/echo', methods=['POST'])
def echo():
    data = request.get_json()
    print("Received POST data:", data)
    return jsonify({"message": "Webhook received successfully", "status": "OK"}), 200

@app.route(f'/webhook/echo/{ALERT_ID}', methods=['POST'])
def handle_alert_id():
    return jsonify({"error": "Invalid alert ID"}), 404

# Render automatically runs gunicorn for Flask apps, so no need for app.run()
