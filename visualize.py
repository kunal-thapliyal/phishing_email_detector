import pandas as pd
import matplotlib
matplotlib.use('Agg')  # ✅ Force matplotlib to use non-GUI backend
import matplotlib.pyplot as plt

# Read the email log
df = pd.read_csv("logs/email_log.csv", header=None, names=["Time", "Email Content", "ML Result", "URL", "VirusTotal Result"])

# Clean column values
df["ML Result"] = df["ML Result"].str.strip()
df["VirusTotal Result"] = df["VirusTotal Result"].str.strip()

# Count ML results
ml_counts = df["ML Result"].value_counts()

# Count VirusTotal results
vt_counts = df["VirusTotal Result"].value_counts()

# Plot ML results
plt.figure(figsize=(8, 4))
ml_counts.plot(kind='bar', color=['red', 'green'])
plt.title("ML Prediction Count")
plt.ylabel("Number of Emails")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("ml_bar_chart.png")  # ✅ Save instead of show
plt.close()

# Plot VirusTotal results
plt.figure(figsize=(8, 4))
vt_counts.plot(kind='bar', color=['blue', 'lightgreen'])
plt.title("VirusTotal Result Count")
plt.ylabel("Number of URLs")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("vt_bar_chart.png")  # ✅ Save instead of show
plt.close()

print("✅ Charts saved as ml_bar_chart.png and vt_bar_chart.png")
