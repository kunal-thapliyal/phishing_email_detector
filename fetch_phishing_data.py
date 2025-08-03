import requests
import csv


url = "https://urlhaus.abuse.ch/downloads/csv_recent/"

response = requests.get(url)

if response.status_code == 200:
    decoded_content = response.content.decode('utf-8')
    lines = decoded_content.splitlines()
    
    
    filtered_lines = [line for line in lines if not line.startswith("#") and line.strip()]
    
    
    with open("logs/phishing_feed.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for line in filtered_lines:
            writer.writerow(line.split(","))
    
    print("✅ Real-time phishing URLs saved to logs/phishing_feed.csv")

else:
    print("❌ Failed to download phishing feed.")
