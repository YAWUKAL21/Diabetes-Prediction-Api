
import streamlit as st
import requests
from PIL import Image
import time

# FastAPI URL
API_URL = "https://diabetes-prediction-api-2.onrender.com/predict"

# Set page title and icon
st.set_page_config(page_title="Diabetes Prediction", page_icon="🩺", layout="centered")

# Custom CSS for a better gradient background
st.markdown(
    """
    <style>
        /* Modern Gradient Background */
        body {
            background: linear-gradient(to right, #00c6ff, #3a47d5);
            color: white;
        }

        .stApp {
            background: linear-gradient(to right, #00c6ff, #3a47d5);
            color: white;
        }

        /* Prediction container with background image */
        .prediction-container {
            position: relative;
            width: 100%;
            max-width: 600px;
            margin: auto;
            padding: 40px;
            border-radius: 15px;
            text-align: center;
            background: url('diabetes.jpg') no-repeat center center;
            background-size: cover;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.5);
            color: white;
        }

        /* Dark overlay for text readability */
        .prediction-container::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.6);
            border-radius: 15px;
        }

        /* Ensure text appears above the overlay */
        .prediction-container h2, .prediction-container h3 {
            position: relative;
            z-index: 2;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.markdown("<h1 style='text-align: center; color: white;'>Diabetes Prediction App 🩺</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter your health details below to check your diabetes risk.</p>", unsafe_allow_html=True)

# Collect user input
col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, step=1)
    Glucose = st.number_input("Glucose Level", min_value=0, max_value=200, step=1)
    BloodPressure = st.number_input("Blood Pressure", min_value=0, max_value=200, step=1)
    SkinThickness = st.number_input("Skin Thickness", min_value=0, max_value=100, step=1)

with col2:
    Insulin = st.number_input("Insulin Level", min_value=0, max_value=1000, step=1)
    BMI = st.number_input("BMI", min_value=0.0, max_value=50.0, step=0.1)
    DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, step=0.01)
    Age = st.number_input("Age", min_value=0, max_value=120, step=1)

# Predict button
if st.button("🔍 Predict Diabetes"):
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

    with st.spinner("Analyzing your data..."):
        time.sleep(2)  # Simulate loading time

    try:
        response = requests.post(API_URL, json=input_data)

        if response.status_code == 200:
            result = response.json()
            prediction = result["prediction"]
            probability = result["probability"]

            st.success("✅ Prediction Successful!")

            # Display prediction inside a styled div
            prediction_text = ""
            if prediction == 1:
                prediction_text = "<h2 style='color: red;'>You are at risk of Diabetes 😢</h2>"
            else:
                prediction_text = "<h2 style='color: green;'>You are NOT at risk of Diabetes 😊</h2>"

            st.markdown(
                f"<div class='prediction-container'>{prediction_text}<h3>Probability: {probability * 100:.2f}%</h3></div>",
                unsafe_allow_html=True
            )
        else:
            st.error(f"Error: {response.json()['detail']}")

    except Exception as e:
        st.error(f"Error connecting to the API: {e}")
