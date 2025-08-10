import requests

url = "https://railway-deploy-tracker-production.up.railway.app/railway-deploy"
payload = {
    "project": {"name": "Test Project"},
    "status": "failed",
    "deploy": {"url": "https://example.com/deploy/123"}
}

response = requests.post(url, json=payload)
print("Status code:", response.status_code)
print("Response:", response.text)
