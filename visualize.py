import pandas as pd
import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt

df = pd.read_csv("logs/email_log.csv", header=None, names=["Time", "Email Content", "ML Result", "URL", "VirusTotal Result"])

df["ML Result"] = df["ML Result"].str.strip()
df["VirusTotal Result"] = df["VirusTotal Result"].str.strip()

ml_counts = df["ML Result"].value_counts()


vt_counts = df["VirusTotal Result"].value_counts()

plt.figure(figsize=(8, 4))
ml_counts.plot(kind='bar', color=['red', 'green'])
plt.title("ML Prediction Count")
plt.ylabel("Number of Emails")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("ml_bar_chart.png")  
plt.close()

plt.figure(figsize=(8, 4))
vt_counts.plot(kind='bar', color=['blue', 'lightgreen'])
plt.title("VirusTotal Result Count")
plt.ylabel("Number of URLs")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("vt_bar_chart.png")
plt.close()

print(" Charts saved as ml_bar_chart.png and vt_bar_chart.png")
