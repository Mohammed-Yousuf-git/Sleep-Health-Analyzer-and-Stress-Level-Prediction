from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load models
regressor = joblib.load("/Users/usufahmed/Desktop/SLEEP_STRESS/stress_model.pkl")
classifier = joblib.load("/Users/usufahmed/Desktop/SLEEP_STRESS/sleep_disorder_model.pkl")
label_encoder = joblib.load("/Users/usufahmed/Desktop/SLEEP_STRESS/label_encoder.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get form data
        quality = int(request.form["quality"])
        activity = int(request.form["activity"])
        heart_rate = int(request.form["heart_rate"])
        steps = int(request.form["steps"])
        systolic = int(request.form["systolic"])
        diastolic = int(request.form["diastolic"])
        bmi = request.form["bmi"]

        # One-hot encode BMI
        bmi_normal = 1 if bmi == "Normal" else 0
        bmi_obese = 1 if bmi == "Obese" else 0
        bmi_overweight = 1 if bmi == "Overweight" else 0

        features = np.array([[quality, activity, heart_rate, steps, systolic, diastolic,
                              bmi_normal, bmi_obese, bmi_overweight]])

        # Predict stress
        stress_pred = regressor.predict(features)[0]

        # Predict sleep disorder
        sleep_pred = classifier.predict(features)[0]
        sleep_label = label_encoder.inverse_transform([sleep_pred])[0]

        return render_template("index.html", stress=round(stress_pred, 2), disorder=sleep_label)

    return render_template("index.html", stress=None, disorder=None)

if __name__ == "__main__":
    app.run(debug=True)
