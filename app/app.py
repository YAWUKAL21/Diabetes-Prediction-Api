# import streamlit as st
# import requests

# # FastAPI server URL
# API_URL = "https://diabetes-prediction-api-2.onrender.com/predict"

# # Streamlit UI setup
# st.title("Diabetes Prediction")

# # Input fields for the user to enter data
# Pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, step=1)
# Glucose = st.number_input("Glucose", min_value=0, max_value=200, step=1)
# BloodPressure = st.number_input("Blood Pressure", min_value=0, max_value=200, step=1)
# SkinThickness = st.number_input("Skin Thickness", min_value=0, max_value=100, step=1)
# Insulin = st.number_input("Insulin", min_value=0, max_value=1000, step=1)
# BMI = st.number_input("BMI", min_value=0.0, max_value=50.0, step=0.1)
# DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, step=0.01)
# Age = st.number_input("Age", min_value=0, max_value=120, step=1)

# # Button to trigger prediction
# if st.button("Predict"):
#     # Prepare the input data as a dictionary
#     input_data = {
#         "Pregnancies": Pregnancies,
#         "Glucose": Glucose,
#         "BloodPressure": BloodPressure,
#         "SkinThickness": SkinThickness,
#         "Insulin": Insulin,
#         "BMI": BMI,
#         "DiabetesPedigreeFunction": DiabetesPedigreeFunction,
#         "Age": Age,
#     }
    
#     try:
#         # Send the data to the FastAPI server
#         response = requests.post(API_URL, json=input_data)
        
#         if response.status_code == 200:
#             result = response.json()
#             prediction = result["prediction"]
#             probability = result["probability"]
            
#             # Display the results
#             st.write(f"Prediction: {'Diabetic' if prediction == 1 else 'Non-Diabetic'}")
#             st.write(f"Probability: {probability * 100:.2f}%")
#         else:
#             st.error(f"Error: {response.json()['detail']}")
    
#     except Exception as e:
#         st.error(f"Error connecting to the API: {e}")

import streamlit as st
import requests
from PIL import Image
import time

# FastAPI URL
API_URL = "https://diabetes-prediction-api-2.onrender.com/predict"

# Set page title and icon
st.set_page_config(page_title="Diabetes Prediction", page_icon="🩺", layout="centered")

# Custom CSS for gradient background
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(to right, #00c6ff, #0072ff);
            color: white;
        }
        .stApp {
            background: linear-gradient(to right, #00c6ff, #0072ff);
            color: white;
        }
        .stTextInput, .stNumberInput, .stButton {
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Load a medical-themed image
# image = Image.open("diabetes.jpg")  
# st.image(image, use_column_width=True)
st.image("https://cdn.pixabay.com/photo/2020/04/16/19/18/diabetes-5054901_1280.jpg", use_column_width=True)

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

            if prediction == 1:
                st.markdown(
                    "<h2 style='color: red; text-align: center;'>You are at risk of Diabetes 😢</h2>",
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    "<h2 style='color: green; text-align: center;'>You are NOT at risk of Diabetes 😊</h2>",
                    unsafe_allow_html=True
                )

            st.markdown(f"<h3 style='text-align: center;'>Probability: {probability * 100:.2f}%</h3>", unsafe_allow_html=True)
        else:
            st.error(f"Error: {response.json()['detail']}")

    except Exception as e:
        st.error(f"Error connecting to the API: {e}")
