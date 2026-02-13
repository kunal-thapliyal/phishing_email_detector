import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score
import pickle

print(" Loading dataset...")
df = pd.read_csv("phishing_email.csv")

print(" Checking columns...")
print(df.columns)

print(" Preparing features and labels...")
X = df["text_combined"]
y = df["label"]

print(" Vectorizing text...")
vectorizer = TfidfVectorizer(max_features=5000)
X_vec = vectorizer.fit_transform(X)

print("🛠 Splitting data...")
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

print("Training model (this may take a few seconds)...")
model = RandomForestClassifier(n_estimators=30, max_depth=10, n_jobs=-1)
model.fit(X_train, y_train)

print(" Model trained successfully!")
print(" Evaluating...")
y_pred = model.predict(X_test)
print(" Accuracy:", accuracy_score(y_test, y_pred))

print(" Saving model and vectorizer...")
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print(" Model and vectorizer saved successfully.")
print(f" Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
