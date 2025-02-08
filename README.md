# 🎓 Student Performance Prediction - Machine Learning Project

## 📖 Project Overview

This project aims to predict student performance based on various factors such as study habits, attendance, and past scores using a classification model. The goal is to help educators identify students who may need additional support.

## 📊 Dataset

- **File:** `student-por.csv`
- **Source:** [https://archive.ics.uci.edu/dataset/320/student+performance](https://archive.ics.uci.edu/dataset/320/student+performance)
- **Description:** Contains student records including study habits, attendance, and past scores. The target variable is the final grade.

## ⚙️ Tech Stack

- **Python** 🐍
- **pandas, numpy** (Data Processing)
- **scikit-learn** (Model Training & Evaluation)
- **matplotlib, seaborn** (Data Visualization)
- **FastAPI** (Model Deployment)

## API Endpoint

- **POST /predict :**
  `https://ml-sk2t.onrender.com/predict`
- **Example Request:**
  ```json
  {
    "studytime": 2,
    "absences": 5,
    "G1": 98,
    "G2": 96
  }
  ```
- **Example Response:**
  ```json
  {
    "prediction": 92.00821967137978
  }
  ```

## 🛠️ Deployment

This model is deployed on Render.

- **🔗 Live API Link:** [https://ml-sk2t.onrender.com/docs](https://ml-sk2t.onrender.com/docs)
- **🔗 React-based web app:** [https://machine-learning-roan.vercel.app/](https://machine-learning-roan.vercel.app/)

## 🎯 Future Improvements

- Optimize feature selection 🔍
- Tune hyperparameters using GridSearchCV ⚙️
- Deploy a React-based UI for better accessibility 💻

## 🛠️ Setup & Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/birukashagre6/ML.git
   cd ML
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   python api.py
   uvicorn api:app --reload  # For FastAPI
   ```

## Limitation

- Render Cloud Free Tier Delay: On first request, the API may be slow and show a fetching error. Pressing "Predict" 4-5 times resolves this issue. The issue is due to Render’s free plan limitations; upgrading to a paid version would fix it.
