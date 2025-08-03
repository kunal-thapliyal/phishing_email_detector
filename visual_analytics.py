import matplotlib
matplotlib.use('Agg')  

import pandas as pd
import matplotlib.pyplot as plt


log_path = "logs/email_log.csv"
df = pd.read_csv(log_path)


df["ML Result"] = df["ML Result"].astype(str).str.strip().str.lower()
df["VirusTotal Result"] = df["VirusTotal Result"].astype(str).str.strip().str.lower()


ml_counts = df["ML Result"].value_counts()
ml_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['red', 'green'])
plt.title("ML Prediction: Phishing vs Safe")
plt.ylabel("")  
plt.tight_layout()
plt.savefig("ml_pie_chart.png")
plt.close()


vt_counts = df["VirusTotal Result"].value_counts()
vt_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['blue', 'lightgreen'])
plt.title("VirusTotal: Unsafe vs Safe")
plt.ylabel("")  # Hide y-axis label
plt.tight_layout()
plt.savefig("vt_pie_chart.png")
plt.close()

summary = pd.DataFrame({
    "ML Result": ml_counts,
    "VirusTotal": vt_counts
}).fillna(0)

summary.plot(kind='bar', color=["orange", "skyblue"])
plt.title("ML vs VirusTotal Result Comparison")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("ml_vs_vt_bar.png")
plt.close()

print("✅ Charts created: ml_pie_chart.png, vt_pie_chart.png, ml_vs_vt_bar.png")
