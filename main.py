import os
import threading
import requests
import schedule
import time
from flask import Flask

# 1. Tiny Web Server for Render's Free Tier
app = Flask(__name__)

@app.route('/')
def home():
    return "Report Refresher App is running active!"

# 2. Your 7:00 AM Refresh Logic
URL = "https://hs-adtech-ss-lego-alb-0.sgp.hotstar-prod.com/api/v2/ads-report/graphql"
HEADERS = {"Content-Type": "application/json"}
PAYLOAD = {
    "operationName": "RefreshReport",
    "variables": {},
    "query": "mutation RefreshReport { refreshReport { status } }"
}

def job():
    print("Triggering daily report refresh at 7:00 AM...")
    try:
        response = requests.post(URL, json=PAYLOAD, headers=HEADERS, timeout=30)
        print(f"Status Code: {response.status_code}")
        print(f"Response text: {response.text}")
    except Exception as e:
        print(f"Error executing refresh: {e}")

def run_scheduler():
    schedule.every().day.at("07:00").do(job)
    print("Scheduler thread started. Waiting for 07:00 AM trigger...")
    while True:
        schedule.run_pending()
        time.sleep(60)

# Start scheduler in background thread
threading.Thread(target=run_scheduler, daemon=True).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
