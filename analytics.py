import pandas as pd

df = pd.read_csv("logs/email_log.csv", header=None, names=["Time", "Email Content", "URL", "ML Result", "Confidence", "VirusTotal Result"])

df["ML Result"] = df["ML Result"].str.strip()
df["VirusTotal Result"] = df["VirusTotal Result"].str.strip()

print("🔢 Total entries:", len(df))

print("🛑 Phishing emails (ML):", (df["ML Result"] == "Phishing (by ML)").sum())
print("✅ Safe emails (ML):", (df["ML Result"] == "Safe (by ML)").sum())

print("🔷 Unsafe by VirusTotal:", (df["VirusTotal Result"] == "Phishing (by VirusTotal)").sum())
print("🟢 Safe by VirusTotal:", (df["VirusTotal Result"] == "Safe (by VirusTotal)").sum())
