from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook/echo', methods=['POST'])
def echo():
    data = request.get_json()
    print("Received POST data:", data)
    return jsonify({"message": "Webhook received successfully", "status": "OK"}), 200

# Render runs this with gunicorn, so no need for app.run()
