import os
import threading
import requests
import schedule
import time
from flask import Flask

# 1. Web server for Render's free tier
app = Flask(__name__)

@app.route('/')
def home():
    return "Report Refresher App is active!"

# 2. REST Refresh Configuration
# Replace the URL string inside quotes with your actual full URL
URL = "https://brands.hotstar.com/api/v1/report/refresh?verifyToken=2c3ee3be6bc076c8e93a131c732cb2...&expDate=16-11-2026"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "application/json"
}

def job():
    print("Triggering report refresh at 7:00 AM...")
    try:
        response = requests.post(URL, headers=HEADERS, timeout=30)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error firing refresh: {e}")

def run_scheduler():
    schedule.every().day.at("07:00").do(job)
    print("Scheduler thread started. Waiting for 07:00 AM trigger...")
    while True:
        schedule.run_pending()
        time.sleep(60)

threading.Thread(target=run_scheduler, daemon=True).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
