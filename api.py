from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the trained model
model = joblib.load("student_performance_model.pkl")

# Initialize FastAPI app
app = FastAPI()

# Define request body structure (without failures)
class StudentData(BaseModel):
    studytime: float
    absences: float
    G1: float
    G2: float

# Define prediction endpoint
@app.post("/predict")
def predict(student: StudentData):
    # Extract features from the request data (without failures)
    features = np.array([[student.studytime, student.absences, student.G1, student.G2]])
    
    # Make prediction using the model
    prediction = model.predict(features)
    
    # Return the prediction result (final grade prediction)
    return {"prediction": float(prediction[0])}  # Ensure JSON compatibility
