# Railway Deploy Tracker

A lightweight Flask-based service that listens for deployment event webhooks from Railway, analyzes deployment logs for errors, and sends real-time notifications to a Slack channel.

---

## Features

- **Receive Railway Deployment Webhooks:** Listens for HTTP POST requests containing deployment event logs from your Railway projects.
- **Error Detection:** Parses incoming webhook payloads to detect common issues such as syntax errors or build failures.
- **Slack Notifications:** Sends formatted alerts to your Slack workspace via Incoming Webhooks to keep your team informed instantly.
- **Easy Deployment:** Ready for deployment on Railway with Docker support, environment variable configuration, and a health check endpoint.

---

## Getting Started

Follow these steps to run the project locally or deploy it to Railway.

### Prerequisites

- Python 3.8+ installed locally (for local testing)
- Git installed for cloning/pushing the repo
- A Slack workspace and an Incoming Webhook URL ([how to create one](https://api.slack.com/messaging/webhooks))
- Railway account for deployment (optional for local use)

---

### Running Locally

1. **Clone the Repository**

   ```bash
   git clone https://github.com/huseyinlokman/railway-deploy-tracker.git
   cd railway-deploy-tracker
