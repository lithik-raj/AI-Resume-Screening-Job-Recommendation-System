import os
import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
df = pd.read_csv("resume_dataset.csv")

# Features and target
X = df["Resume"]
y = df["Category"]

# Create vectorizer
vectorizer = TfidfVectorizer()

# Convert text to vectors
X_vectorized = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vectorized, y)

# Create models folder if it doesn't exist
os.makedirs("models", exist_ok=True)

# Save model and vectorizer
joblib.dump(model, "models/resume_classifier.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("Model and Vectorizer saved successfully!")