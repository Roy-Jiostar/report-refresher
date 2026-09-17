import os
import threading
import requests
import schedule
import time
from flask import Flask

# 1. Web server required for Render's free tier
app = Flask(__name__)

@app.route('/')
def home():
    return "Report Refresher App is active!"

# 2. GraphQL Endpoint & Headers Setup
URL = "https://hs-adtech-ss-lego-alb-0.sgp.hotstar-prod.com/api/v2/ads-report/graphql"

HEADERS = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "authorization": "Bearer 60e93936-1eb9-4b1c-8910-8a16221b1a65",
    "businessaccountid": "6086",
    "content-type": "application/json",
    "origin": "https://origin-hs-adtech-ams-ops-portal.sgp.hotstar-prod.com",
    "priority": "u=1, i",
    "referer": "https://origin-hs-adtech-ams-ops-portal.sgp.hotstar-prod.com/",
    "sec-ch-ua": '"Google Chrome";v="153", "Not_A Brand";v="8", "Chromium";v="153"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"
}

# 3. GraphQL Query Payload
PAYLOAD = {
    "query": """
    mutation {
      refreshReport(request: {
        userMeta: {
          userId: "Roydin Dass"
          tenant: "hotstar"
          system: "ads-reporting"
        }
        reportId: "5fb43dc7-54eb-48fa-b38f-c027ea8b608f"
      })
    }
    """
}

# 4. Main Refresh Job
def job():
    print("Triggering GraphQL report refresh...")
    try:
        response = requests.post(URL, headers=HEADERS, json=PAYLOAD, timeout=30)
        print(f"Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")
    except Exception as e:
        print(f"Error firing GraphQL refresh request: {e}")

# 5. Scheduler Loop (11:00 UTC = 04:30 PM IST)
def run_scheduler():
    schedule.every().day.at("11:00").do(job)
    print("Scheduler thread started. Waiting for 11:00 UTC (04:30 PM IST) trigger...")
    while True:
        schedule.run_pending()
        time.sleep(60)

threading.Thread(target=run_scheduler, daemon=True).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
