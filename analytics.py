import pandas as pd

# Load the log file
df = pd.read_csv("logs/email_log.csv", header=None, names=["Time", "Email Content", "URL", "ML Result", "Confidence", "VirusTotal Result"])

# Clean up whitespace from results
df["ML Result"] = df["ML Result"].str.strip()
df["VirusTotal Result"] = df["VirusTotal Result"].str.strip()

# Total entries
print("🔢 Total entries:", len(df))

# Count of phishing and safe by ML
print("🛑 Phishing emails (ML):", (df["ML Result"] == "Phishing (by ML)").sum())
print("✅ Safe emails (ML):", (df["ML Result"] == "Safe (by ML)").sum())

# Count of unsafe URLs by VirusTotal
print("🔷 Unsafe by VirusTotal:", (df["VirusTotal Result"] == "Phishing (by VirusTotal)").sum())
print("🟢 Safe by VirusTotal:", (df["VirusTotal Result"] == "Safe (by VirusTotal)").sum())
