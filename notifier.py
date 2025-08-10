import requests

def send_slack_notification(webhook_url, message):
    if not webhook_url:
        print("No Slack webhook URL provided.")
        return False

    response = requests.post(webhook_url, json={"text": message})
    return response.status_code == 200
