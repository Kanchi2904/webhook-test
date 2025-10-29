from flask import Flask, request, jsonify

app = Flask(__name__)

# ---------- GLOBAL CORS HANDLER ----------
@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response


# ---------- ROUTE 1: Root webhook handler ----------
@app.route('/', methods=['POST', 'OPTIONS'])
def root():
    if request.method == 'OPTIONS':
        return '', 200  # CORS preflight accepted

    data = request.get_json(silent=True)
    print(f"Received POST at root: {data}")
    return jsonify({"message": "Webhook received successfully"}), 200


# ---------- CATCH-ALL: Return 404 for anything else ----------
@app.route('/<path:subpath>', methods=['GET', 'POST', 'OPTIONS', 'PUT', 'DELETE'])
def catch_all(subpath):
    print(f"Invalid path accessed: /{subpath}")
    return jsonify({"error": "Not Found"}), 404


# Render automatically uses gunicorn on Render
