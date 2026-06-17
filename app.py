from flask import Flask, render_template, request
import os
import joblib

from utils.resume_parser import extract_text
from utils.skill_extractor import extract_skills
from utils.ats_score import calculate_ats
from utils.recommendation import recommend_jobs

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
model = joblib.load("models/resume_classifier.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/predict", methods=["POST"])
def predict():

    if "resume" not in request.files:
        return "No file uploaded"

    file = request.files["resume"]

    if file.filename == "":
        return "No file selected"

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    text = extract_text(filepath)

    skills = extract_skills(text)

    ats_score = calculate_ats(skills)

    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)[0]

    recommendations = recommend_jobs(prediction)

    return render_template(
        "result.html",
        ats_score=ats_score,
        skills=skills,
        prediction=prediction,
        recommendations=recommendations
    )

if __name__ == "__main__":
    app.run(debug=True)