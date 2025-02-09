# Diabetes Prediction System

## Overview

The **Diabetes Prediction System** is a machine learning-based web application that predicts whether an individual is diabetic based on medical features. The project is built using **FastAPI** for the backend and **Streamlit** for the user interface.

## Features

- **Machine Learning Model**: Utilizes Logistic Regression for binary classification.
- **User-Friendly Interface**: Allows users to input their health data and receive predictions.
- **REST API with FastAPI**: Provides an endpoint for model inference.
- **Deployed Application**: Accessible as a web application.

## Dataset

- **Source**: [UCI Machine Learning Repository - Pima Indians Diabetes Dataset]
- **Rows**: 768
- **Columns**: 9 (Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age, Outcome)
- **Target Variable**: Outcome (0 - Non-Diabetic, 1 - Diabetic)

## Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: Streamlit (Python)
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Deployment**: Render (or any cloud platform)

## Installation and Setup

### 1. Clone the Repository

```sh
git clone https://github.com/YAWUKAL21/diabetes-prediction.git
cd diabetes-prediction
```

### 2. Create a Virtual Environment

```sh
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Run the FastAPI Backend

```sh
uvicorn app:app --reload
```

- The API will be available at: [https://diabetes-prediction-api-0qct.onrender.com/docs]
-Open:

🔗 **Live API URL:** [https://diabetes-prediction-api-0qct.onrender.com/docs](https://diabetes-prediction-api-0qct.onrender.com)


### 5. Run the Streamlit Frontend

```sh
streamlit run app.py
```

- The Stream Available At [https://diabetes-prediction-api-1-jx5c.onrender.com/docs](https://diabetes-prediction-api-1-jx5c.onrender.com/docs) 

-Open:
### 🔗 [LIVE ON Stream](https://diabetes-prediction-api-1-jx5c.onrender.com/docs) 
## API Endpoints

| Endpoint   | Method | Description                               |
| ---------- | ------ | ----------------------------------------- |
| `/predict` | POST   | Predicts diabetes based on input features |

### Sample Request

```json
{
  "Pregnancies": 2,
  "Glucose": 120,
  "BloodPressure": 70,
  "SkinThickness": 20,
  "Insulin": 80,
  "BMI": 25.0,
  "DiabetesPedigreeFunction": 0.5,
  "Age": 30
}
```

### Sample Response

```json
{
  "prediction": 1,
  "probability": 0.85
}
```

## Future Improvements

- Enhance the model with advanced algorithms.
- Improve UI/UX design for better user experience.
- Integrate real-time data input from wearable devices.

## License

This project is licensed under the MIT License.

## Acknowledgments

- **UCI Machine Learning Repository** for the dataset.
- **Scikit-learn, FastAPI, and Streamlit** for making machine learning deployment seamless.

---

### 🔗 [GitHub Repository](https://github.com/YAWUKAL21/Diabetes-Prediction-Api.git):https://github.com/YAWUKAL21/Diabetes-Prediction-Api.git

## Contact

For questions or collaborations, feel free to reach out via or create an issue in this repository.

Develped by **Yabkal**:

### 🔗 [Email]:(yabkalmelak@gmail.com) 

### 🔗 [GitHub]:(https://github.com/YAWUKAL21) 

### 🔗 [Linkedin]:(https://www.linkedin.com/in/yawkal-melak-7913b1307) 
