# t
import requests
import time
import os
from dotenv import load_dotenv 
load_dotenv()

API_KEY = os.getenv("VT_API_KEY")

def check_url_virustotal(url):
    headers = {
        "x-apikey": API_KEY
    }
    scan_url = "https://www.virustotal.com/api/v3/urls"

    try:
        print(f"Sending URL to VirusTotal for scanning...")

        response = requests.post(scan_url, headers=headers, data={"url": url})
        print("Step 1 - POST status code:", response.status_code)

        if response.status_code != 200:
            return {"label": "VirusTotal Error"}

        analysis_id = response.json()["data"]["id"]
        print("Step 2 - Analysis ID received:", analysis_id)

        result_url = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"

        for i in range(10):
            time.sleep(3)
            print(f"Step 3 - Waiting for result (try {i + 1})...")
            report_response = requests.get(result_url, headers=headers)
            report = report_response.json()

            stats = report["data"]["attributes"]["stats"]
            if stats["malicious"] + stats["suspicious"] > 0 or stats["undetected"] + stats["harmless"] > 0:
                break

        print("Step 4 - Stats:", stats)

        if stats["malicious"] > 0 or stats["suspicious"] > 0:
            return {"label": "Phishing (by VirusTotal)"}
        else:
            return {"label": "Safe (by VirusTotal)"}

    except Exception as e:
        print("Error while checking URL on VirusTotal:", e)
        return {"label": "VirusTotal Error"}
