import os
import requests
import schedule
import time

# Target GraphQL Endpoint
URL = "https://hs-adtech-ss-lego-alb-0.sgp.hotstar-prod.com/api/v2/ads-report/graphql"

# Required Headers
HEADERS = {
    "Content-Type": "application/json"
}

# Payload copied from your browser Network tab
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

# Schedule job for 07:00 AM daily
schedule.every().day.at("07:00").do(job)

print("Report Refresher App Started. Waiting for 7:00 AM trigger...")

while True:
    schedule.run_pending()
    time.sleep(60)
