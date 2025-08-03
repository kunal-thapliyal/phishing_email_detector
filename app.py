from flask import Flask, render_template, request
import joblib
from check_virustotal import check_url_virustotal as check_virustotal
from datetime import datetime
import os
import re
import csv

app = Flask(__name__)

# Load ML model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Logging directory
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

def extract_urls(text):
    url_pattern = r'(https?://[^\s]+)'
    return re.findall(url_pattern, text)

@app.route("/", methods=["GET", "POST"])
def index():
    result_ml = ""
    result_vt = ""
    confidence = ""

    if request.method == "POST":
        email_content = request.form.get("email_content")
        url = request.form.get("url")

        # ML Prediction
        if email_content:
            X_test = vectorizer.transform([email_content])
            prediction = model.predict(X_test)[0]
            probability = model.predict_proba(X_test)[0][prediction]
            confidence = round(probability * 100, 2)
            result_ml = "Phishing (by ML)" if prediction == 1 else "Safe (by ML)"

            # Extract URL if not provided
            if not url:
                extracted_urls = extract_urls(email_content)
                if extracted_urls:
                    url = extracted_urls[0]
        else: 
            result_ml = "No email content provided"
            confidence = "N/A"

        # VirusTotal URL Check
        if url:
            vt_result = check_virustotal(url)
            result_vt = vt_result.get("label", "Not checked") if isinstance(vt_result, dict) else "Error checking URL"
        else:
            result_vt = "No URL provided"

        # Save to CSV
        log_path = os.path.join(log_dir, "email_log.csv")
        write_header = not os.path.exists(log_path)
        with open(log_path, "a", newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            if write_header:
                writer.writerow(["Time", "Email Content", "URL", "ML Result", "Confidence", "VirusTotal Result"])
            writer.writerow([datetime.now(), email_content, url, result_ml, confidence, result_vt])

        return render_template("index.html", result_ml=result_ml, confidence=confidence, result_vt=result_vt)

    return render_template("index.html", result_ml="", confidence="", result_vt="")


@app.route("/analytics")
def analytics():
    return render_template("analytics.html")

if __name__ == "__main__":
    app.run(debug=True)
