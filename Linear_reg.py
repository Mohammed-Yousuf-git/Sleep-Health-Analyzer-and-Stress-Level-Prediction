{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "68f4abf2-1fc4-48d7-9684-bce439677772",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "📉 Mean Squared Error (Stress Level): 0.20758102726638744\n",
      "✅ Saved model as 'stress_model.pkl'\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.metrics import mean_squared_error\n",
    "import joblib\n",
    "\n",
    "# Load dataset\n",
    "df = pd.read_csv(\"/Users/usufahmed/30Projects30Days/Sleep_health_and_lifestyle_dataset.csv\")\n",
    "\n",
    "# Preprocessing\n",
    "df[['Systolic', 'Diastolic']] = df['Blood Pressure'].str.split('/', expand=True).astype(int)\n",
    "bmi_encoded = pd.get_dummies(df['BMI Category'], prefix='BMI')\n",
    "\n",
    "# Drop irrelevant and target-unrelated columns\n",
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
    "y = df_model['Stress Level']\n",
    "\n",
    "# Train-test split\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "# Train regression model\n",
    "regressor = LinearRegression()\n",
    "regressor.fit(X_train, y_train)\n",
    "\n",
    "# Predict and evaluate\n",
    "y_pred = regressor.predict(X_test)\n",
    "mse = mean_squared_error(y_test, y_pred)\n",
    "print(\"📉 Mean Squared Error (Stress Level):\", mse)\n",
    "\n",
    "# Save the trained model\n",
    "joblib.dump(regressor, \"stress_model.pkl\")\n",
    "print(\"✅ Saved model as 'stress_model.pkl'\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cfee0c6a-38b6-4fb5-afc9-389f9d4c7fca",
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
