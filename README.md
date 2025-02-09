# 🎓 Student Performance Prediction - Machine Learning Project

## 📖 Project Overview

This project aims to predict student performance (final grade `G3`) based on factors such as study habits, attendance, and past scores using a **regression model**. The goal is to help educators identify students who may need additional support and understand the key factors influencing academic performance.

---

## 📊 Dataset

- **File:** `student-por.csv`
- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/320/student+performance)
- **Description:** The dataset contains 649 student records with 33 features, including:
  - `studytime`: Weekly study time (1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, 4 - >10 hours).
  - `absences`: Number of school absences.
  - `G1`: First period grade (numeric: 0 to 20).
  - `G2`: Second period grade (numeric: 0 to 20).
  - `G3`: Final grade (numeric: 0 to 20, target variable).

---

## ⚙️ Tech Stack

- **Python** 🐍: Primary programming language for data analysis and machine learning.
- **pandas, numpy**: Used for data manipulation and numerical computations.
- **scikit-learn**: For model training, evaluation, and hyperparameter tuning.
- **matplotlib, seaborn**: For data visualization and exploratory data analysis (EDA).
- **FastAPI**: For deploying the model as a REST API.

---

## 🚀 Model Workflow

1. **Data Loading & Exploration:**

   - Load the dataset and perform exploratory data analysis (EDA) to understand the data distribution, correlations, and potential outliers.
   - Visualize key features using histograms, scatter plots, and heatmaps.

2. **Data Preprocessing:**

   - Handle missing values (if any) and remove duplicates.
   - Encode categorical features using `LabelEncoder` and one-hot encoding.
   - Scale numerical features using `StandardScaler`.
   - Perform feature engineering (e.g., interaction terms, binning).

3. **Model Training:**

   - Split the data into training and testing sets (80% train, 20% test).
   - Train a **Linear Regression** model as a baseline.
   - Perform hyperparameter tuning using **GridSearchCV** for **Ridge** and **Lasso** regression models.

4. **Model Evaluation:**

   - Evaluate the model using **R²** and **Mean Squared Error (MSE)**.
   - Compare the model's performance against a baseline (`DummyRegressor`).
   - Visualize actual vs. predicted grades and residual distribution.

5. **Model Deployment:**
   - Deploy the best-performing model (Ridge Regression) as a REST API using **FastAPI**.
   - Host the API on **Render** and create a React-based web app for user interaction.

---

## API Endpoint

- **POST /predict :**
  `https://ml-sk2t.onrender.com/predict`
- **Input:** Provide the following features in JSON format:
  ```json
  {
    "studytime": 2,
    "absences": 5,
    "G1": 98,
    "G2": 96
  }
  ```

---

## 📌 Model Deployment Details

### Output:

The predicted final grade (G3):

```json
{
  "prediction": 92.00821967137978
}
```

### 🛠️ Deployment

The model is deployed on Render as a REST API using FastAPI. You can access the API and interact with it using the following links:

🔗 **Live API Link:** [https://ml-sk2t.onrender.com/docs](https://ml-sk2t.onrender.com/docs)  
🔗 **React-based Web App:** [https://machine-learning-roan.vercel.app/](https://machine-learning-roan.vercel.app/)

The API provides an interactive Swagger UI for testing and documentation.

---

## 🎯 Future Improvements

- **Feature Engineering:** Explore additional interaction terms or polynomial features to improve model performance.
- **Hyperparameter Tuning:** Use advanced techniques like Bayesian Optimization or RandomizedSearchCV for better hyperparameter tuning.
- **Model Interpretability:** Use tools like SHAP or LIME to explain model predictions and understand feature importance.
- **Scalability:** Deploy the model on a more scalable platform (e.g., AWS, GCP) to handle larger datasets and higher traffic.
- **User Interface:** Develop a more interactive and user-friendly React-based UI for educators and students.

---

## 🛠️ Setup & Installation

Clone this repository:

```bash
git clone https://github.com/birukashagre6/ML.git
cd ML
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the FastAPI server:

```bash
uvicorn api:app --reload
```

Access the API:  
Open your browser and navigate to `http://127.0.0.1:8000/docs` to interact with the API.

---

## ⚠️ Limitations

### Render Free Tier Delay

Due to Render's free tier limitations, the API may experience delays or timeouts on the first request. To resolve this:

- Refresh the page or press "Predict" 4-5 times.
- Consider upgrading to Render's paid plan for better performance.

### Model Generalization

The model's performance may vary on new datasets. Regular retraining with updated data is recommended.

---


## 🙏 Acknowledgments

- Dataset sourced from the UCI Machine Learning Repository.
- Special thanks to the open-source community for providing the tools and libraries used in this project.

---

## 📧 Contact

For questions or feedback, feel free to reach out:

- **Name:** Biruk Ashagre
- **Email:** birukashagre639@gmail.com
- **GitHub:** [birukashagre6](https://github.com/birukashagre6)
