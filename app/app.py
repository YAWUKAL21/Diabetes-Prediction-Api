
import streamlit as st
import requests
import time

# FastAPI URL
API_URL = "http://localhost:8000/predict/"  # Change to your FastAPI URL if hosted online

# Set page title and icon
st.set_page_config(page_title="Diabetes Prediction", page_icon="🩺", layout="centered")

# Title and description
st.title("Diabetes Prediction App 🩺")
st.markdown("Enter your health details below to check your diabetes risk.")

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
        # Send the input data to the FastAPI server
        response = requests.post(API_URL, json=input_data)
        
        # Check if the status code is OK
        if response.status_code == 200:
            result = response.json()
            prediction = result["prediction"]
            probability = result["probability"]

            st.success("✅ Prediction Successful!")

            # Display prediction message
            if prediction == 1:
                st.error(f"You are at risk of Diabetes 😢")
            else:
                st.success(f"You are NOT at risk of Diabetes 😊")

            # Display probability
            st.write(f"Probability: {probability * 100:.2f}%")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        st.error(f"Error connecting to the API: {e}")


# import streamlit as st
# import requests

# # FastAPI endpoint
# API_URL = "http://127.0.0.1:8000/predict/"  # Update this if the FastAPI server runs on a different host

# # Streamlit UI
# st.title("Diabetes Prediction App")
# st.write("Enter the patient details to predict the likelihood of diabetes.")

# # Input fields
# pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=0)
# glucose = st.number_input("Glucose Level", min_value=0.0, max_value=300.0, value=100.0)
# blood_pressure = st.number_input("Blood Pressure", min_value=0.0, max_value=200.0, value=70.0)
# skin_thickness = st.number_input("Skin Thickness", min_value=0.0, max_value=100.0, value=20.0)
# insulin = st.number_input("Insulin Level", min_value=0.0, max_value=1000.0, value=30.0)
# bmi = st.number_input("BMI", min_value=0.0, max_value=100.0, value=25.0)
# diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5)
# age = st.number_input("Age", min_value=0, max_value=120, value=30)

# # Prediction button
# if st.button("Predict"):
#     # Prepare input data
#     input_data = {
#         "Pregnancies": pregnancies,
#         "Glucose": glucose,
#         "BloodPressure": blood_pressure,
#         "SkinThickness": skin_thickness,
#         "Insulin": insulin,
#         "BMI": bmi,
#         "DiabetesPedigreeFunction": diabetes_pedigree,
#         "Age": age
#     }

#     try:
#         # Send request to FastAPI
#         response = requests.post(API_URL, json=input_data)
#         result = response.json()

#         if response.status_code == 200:
#             prediction = result["prediction"]
#             probability = result["probability"]
#             st.success(f"Prediction: {'Diabetic' if prediction == 1 else 'Non-Diabetic'}")
#             st.info(f"Probability of diabetes: {probability:.4f}")
#         else:
#             st.error(f"Error: {result['detail']}")
#     except Exception as e:
#         st.error(f"Failed to connect to API: {e}")
