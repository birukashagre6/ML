from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the trained model
model = joblib.load("student_performance_model.pkl")

# Initialize FastAPI app
app = FastAPI()

# Define request body structure
class StudentData(BaseModel):
    studytime: float
    failures: int
    absences: float
    G1: float
    G2: float

# Define prediction endpoint
@app.post("/predict")
def predict(student: StudentData):
    # Extract features from the request data
    features = np.array([[student.studytime, student.failures, student.absences, student.G1, student.G2]])
    
    # Make prediction using the model
    prediction = model.predict(features)
    
    # Return the prediction result(final grade prediction)
    return {"prediction": prediction[0]}
