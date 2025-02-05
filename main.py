
from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
from pydantic import BaseModel
from sklearn.preprocessing import StandardScaler

# Initialize FastAPI app
app = FastAPI()

# Load trained model
model = joblib.load("logreg.joblib")

# Define request schema
class DiabetesInput(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int
    # BMI_to_Age_Ratio: float = None  # Allow it to be optional

# Load dataset to fit scaler (ensuring consistent scaling)
df = pd.read_csv("diabetes.csv")
numerical_columns = [
    "Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"
]
scaler = StandardScaler()
df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

def preprocess(data: DiabetesInput):
    # Convert input data to dataframe
    df_input = pd.DataFrame([data.dict()])
    
    # Only use the original training features (remove BMI_to_Age_Ratio)
    original_features = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", 
                         "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]
    
    # Ensure the dataframe has only these features
    df_input = df_input[original_features]

    # Transform the numerical features
    df_input[original_features] = scaler.transform(df_input[original_features])
    
    return df_input


@app.post("/predict")
def predict_diabetes(data: DiabetesInput):
    try:
        # Log the incoming data for debugging
        print(f"Received data: {data}")
        
        processed_data = preprocess(data)
        prediction = model.predict(processed_data)[0]
        probability = model.predict_proba(processed_data)[0][1]
        return {"prediction": int(prediction), "probability": float(probability)}
    
    except Exception as e:
        # Log the exception to understand the problem
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")

@app.get("/")
def root():
    return {"message": "Diabetes Prediction API is running!"}
