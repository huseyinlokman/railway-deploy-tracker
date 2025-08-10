from flask import Flask, request, jsonify
from validators import validate_payload
from notifier import send_slack_notification
import os

app = Flask(__name__)

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

@app.route("/railway-deploy", methods=["POST"])
def railway_deploy():
    data = request.get_json()

    if not validate_payload(data):
        return jsonify({"error": "Invalid payload"}), 400

    project_name = data.get("project", {}).get("name", "Unknown Project")
    status = data.get("status", "unknown")
    url = data.get("deploy", {}).get("url", "")

    message = f"🚀 Railway Deployment Update\nProject: {project_name}\nStatus: {status}\nURL: {url}"

    if send_slack_notification(SLACK_WEBHOOK_URL, message):
        return jsonify({"status": "Notification sent"}), 200
    else:
        return jsonify({"error": "Failed to send notification"}), 500
    
@app.route("/", methods=["GET"])
def home():
    return "Railway Deploy Tracker is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
