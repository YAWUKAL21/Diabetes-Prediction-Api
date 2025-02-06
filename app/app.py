import streamlit as st
import requests

# FastAPI server URL
API_URL = "https://diabetes-prediction-api-2.onrender.com/predict"

# Streamlit UI setup
st.title("Diabetes Prediction")

# Input fields for the user to enter data
Pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, step=1)
Glucose = st.number_input("Glucose", min_value=0, max_value=200, step=1)
BloodPressure = st.number_input("Blood Pressure", min_value=0, max_value=200, step=1)
SkinThickness = st.number_input("Skin Thickness", min_value=0, max_value=100, step=1)
Insulin = st.number_input("Insulin", min_value=0, max_value=1000, step=1)
BMI = st.number_input("BMI", min_value=0.0, max_value=50.0, step=0.1)
DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, step=0.01)
Age = st.number_input("Age", min_value=0, max_value=120, step=1)

# Button to trigger prediction
if st.button("Predict"):
    # Prepare the input data as a dictionary
    input_data = {
        "Pregnancies": Pregnancies,
        "Glucose": Glucose,
        "BloodPressure": BloodPressure,
        "SkinThickness": SkinThickness,
        "Insulin": Insulin,
        "BMI": BMI,
        "DiabetesPedigreeFunction": DiabetesPedigreeFunction,
        "Age": Age,
    }
    
    try:
        # Send the data to the FastAPI server
        response = requests.post(API_URL, json=input_data)
        
        if response.status_code == 200:
            result = response.json()
            prediction = result["prediction"]
            probability = result["probability"]
            
            # Display the results
            st.write(f"Prediction: {'Diabetic' if prediction == 1 else 'Non-Diabetic'}")
            st.write(f"Probability: {probability * 100:.2f}%")
        else:
            st.error(f"Error: {response.json()['detail']}")
    
    except Exception as e:
        st.error(f"Error connecting to the API: {e}")

