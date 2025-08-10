from flask import Flask, request, jsonify
from notifier import send_slack_notification
import os
from validators import validate_payload, run_all_validators

app = Flask(__name__)

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

@app.route("/railway-deploy", methods=["POST"])
def railway_deploy():
    data = request.get_json()

    if not validate_payload(data):
        return jsonify({"error": "Invalid payload"}), 400

    issues = run_all_validators(data)

    project_name = "Unknown Project"
    # try to get project name from either payload style
    if "project" in data and isinstance(data["project"], dict):
        project_name = data["project"].get("name", project_name)
    elif "tags" in data and isinstance(data["tags"], dict):
        project_name = data["tags"].get("projectId", project_name)

    message = f"🚀 Railway Deployment Update for *{project_name}*"

    if issues:
        message += "\n⚠️ Issues detected:\n"
        for i, issue in enumerate(issues, 1):
            message += f"{i}. {issue}\n"
    else:
        message += "\n✅ No issues detected."

    if send_slack_notification(SLACK_WEBHOOK_URL, message):
        return jsonify({"status": "Notification sent", "issues": issues}), 200
    else:
        return jsonify({"error": "Failed to send notification"}), 500

@app.route("/", methods=["GET"])
def home():
    return "Railway Deploy Tracker is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
