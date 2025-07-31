# 🛌 Sleep Health Analyzer & Stress Predictor

A machine learning-based web application to assess sleep health and predict stress, developed by Mohammed Yousuf.

## 📌 Project Objectives

- **Predict stress level** (1–10; regression)
- **Classify sleep disorder type** (None, Insomnia, Sleep Apnea)
- **Visualize user and population health metrics**

## 🔍 Features

- **User Input Form**:  
  - Sleep Quality (1–10)
  - Physical Activity (minutes/day)
  - Heart Rate (bpm)
  - Daily Steps
  - Blood Pressure (Systolic & Diastolic)
  - BMI Category (Underweight, Normal, Overweight)

- **Predictions:**  
  - Stress Level (1–10)
  - Sleep Disorder (None, Insomnia, Sleep Apnea)

- **Dashboard Visualizations:**  
  - Bar chart: User vs average stress levels
  - Pie chart: Sleep disorder probability
  - Boxplots/histograms: User metrics vs dataset

## ⚙️ Tech Stack

| Area         | Technology                                 |
|--------------|--------------------------------------------|
| Frontend     | HTML5, CSS3, Bootstrap                     |
| Backend      | Python, Flask                              |
| ML Models    | scikit-learn (Regression & Classification) |
| Visualization| matplotlib, seaborn, plotly                |

## 📊 Dataset

- **Sleep Quality Scores**
- **Heart Rate, Activity, Daily Steps**
- **Blood Pressure (Systolic & Diastolic)**
- **BMI Category**
- **Sleep Disorder Diagnosis**

*Data is preprocessed and used for:*
- Stress regression prediction
- Sleep disorder classification

## 🧠 Machine Learning Models

- **Stress Prediction:**  
  - LinearRegression or RandomForestRegressor
- **Sleep Disorder Classification:**  
  - RandomForestClassifier or LogisticRegression

*Models are saved as `.pkl` files and loaded for real-time prediction.*

## 📈 Example Dashboard Elements

- **Bar Chart:**  
  *User stress vs population average*

- **Pie Chart:**  
  *Probability of each sleep disorder for the user*

- **Boxplot/Histogram:**  
  *Compare individual health metrics to dataset norms*

## 🚀 How to Run

```bash
git clone https://github.com/yourusername/sleep-health-analyzer.git
cd sleep-health-analyzer
# (follow readme for additional setup)
```

## ✅ Future Improvements

- Add login/user sessions
- Save & analyze user prediction history
- Export results (PDF/CSV)
- Cloud deployment (Heroku/Render/AWS)

## 📜 License

MIT License

## 👤 Author

Mohammed Yousuf

**Sleep Health & Wellness AI Project**  
*Empowering users to track, understand, and improve their sleep and stress health.*

Sources
