{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d1413c79-1bfb-4978-90a3-dd0f22a29a94",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Sleep Disorder Classification Accuracy: 0.88\n",
      "✅ Saved model as 'sleep_disorder_model.pkl'\n",
      "✅ Saved label encoder as 'label_encoder.pkl'\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "from sklearn.metrics import accuracy_score\n",
    "import joblib\n",
    "\n",
    "# Load dataset\n",
    "df = pd.read_csv(\"/Users/usufahmed/30Projects30Days/Sleep_health_and_lifestyle_dataset.csv\")\n",
    "\n",
    "# Preprocessing\n",
    "df[['Systolic', 'Diastolic']] = df['Blood Pressure'].str.split('/', expand=True).astype(int)\n",
    "bmi_encoded = pd.get_dummies(df['BMI Category'], prefix='BMI')\n",
    "\n",
    "# Encode target: Sleep Disorder\n",
    "le_sleep_disorder = LabelEncoder()\n",
    "df['Sleep Disorder Encoded'] = le_sleep_disorder.fit_transform(df['Sleep Disorder'])\n",
    "\n",
    "# Drop unused columns\n",
    "df_model = df.drop(columns=[\n",
    "    'Person ID', 'Gender', 'Age', 'Occupation', 'Sleep Duration',\n",
    "    'Blood Pressure', 'BMI Category', 'Sleep Disorder'\n",
    "])\n",
    "\n",
    "# Combine with BMI encodings\n",
    "df_model = pd.concat([df_model, bmi_encoded], axis=1)\n",
    "\n",
    "# Define input features and target\n",
    "features = ['Quality of Sleep', 'Physical Activity Level', 'Heart Rate',\n",
    "            'Daily Steps', 'Systolic', 'Diastolic', 'BMI_Normal', 'BMI_Obese', 'BMI_Overweight']\n",
    "X = df_model[features]\n",
    "y = df_model['Sleep Disorder Encoded']\n",
    "\n",
    "# Train-test split\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "# Train classification model\n",
    "classifier = RandomForestClassifier(random_state=42)\n",
    "classifier.fit(X_train, y_train)\n",
    "\n",
    "# Predict and evaluate\n",
    "y_pred = classifier.predict(X_test)\n",
    "accuracy = accuracy_score(y_test, y_pred)\n",
    "print(\"✅ Sleep Disorder Classification Accuracy:\", accuracy)\n",
    "\n",
    "# Save the trained model and label encoder\n",
    "joblib.dump(classifier, \"sleep_disorder_model.pkl\")\n",
    "joblib.dump(le_sleep_disorder, \"label_encoder.pkl\")\n",
    "print(\"✅ Saved model as 'sleep_disorder_model.pkl'\")\n",
    "print(\"✅ Saved label encoder as 'label_encoder.pkl'\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "505f1e7c-e4ec-4562-91e1-117d811ae24e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
