{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6a2addd6-9fb7-4413-a8f0-30d22fb866b1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Quality of Sleep  Physical Activity Level  Stress Level  Heart Rate  \\\n",
      "0                 6                       42             6          77   \n",
      "1                 6                       60             8          75   \n",
      "2                 6                       60             8          75   \n",
      "3                 4                       30             8          85   \n",
      "4                 4                       30             8          85   \n",
      "\n",
      "   Daily Steps  Systolic  Diastolic  Sleep Disorder Encoded  BMI_Normal  \\\n",
      "0         4200       126         83                       2       False   \n",
      "1        10000       125         80                       2        True   \n",
      "2        10000       125         80                       2        True   \n",
      "3         3000       140         90                       1       False   \n",
      "4         3000       140         90                       1       False   \n",
      "\n",
      "   BMI_Normal Weight  BMI_Obese  BMI_Overweight  \n",
      "0              False      False            True  \n",
      "1              False      False           False  \n",
      "2              False      False           False  \n",
      "3              False       True           False  \n",
      "4              False       True           False  \n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "\n",
    "# Load the dataset\n",
    "df = pd.read_csv(\"/Users/usufahmed/30Projects30Days/Sleep_health_and_lifestyle_dataset.csv\")\n",
    "\n",
    "# ➤ Step 1: Split Blood Pressure into Systolic and Diastolic\n",
    "df[['Systolic', 'Diastolic']] = df['Blood Pressure'].str.split('/', expand=True).astype(int)\n",
    "\n",
    "# ➤ Step 2: Encode BMI Category (One-hot encoding)\n",
    "bmi_encoded = pd.get_dummies(df['BMI Category'], prefix='BMI')\n",
    "\n",
    "# ➤ Step 3: Encode Sleep Disorder using LabelEncoder\n",
    "le_sleep_disorder = LabelEncoder()\n",
    "df['Sleep Disorder Encoded'] = le_sleep_disorder.fit_transform(df['Sleep Disorder'])\n",
    "\n",
    "# ➤ Step 4: Drop irrelevant columns\n",
    "df_model = df.drop(columns=[\n",
    "    'Person ID', 'Gender', 'Age', 'Occupation', 'Sleep Duration',\n",
    "    'Blood Pressure', 'BMI Category', 'Sleep Disorder'  # original categorical columns\n",
    "])\n",
    "\n",
    "# ➤ Step 5: Combine one-hot encoded BMI columns\n",
    "df_model = pd.concat([df_model, bmi_encoded], axis=1)\n",
    "\n",
    "# ➤ Output: Cleaned dataset ready for modeling\n",
    "print(df_model.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8dc05951-86ee-4be2-acac-e7eab3f2e8c2",
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
