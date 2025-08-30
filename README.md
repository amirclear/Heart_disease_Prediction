# ❤️ Heart Disease Prediction Web App

## Overview

This project is a machine learning-based web application developed using Streamlit and Python to predict the likelihood of heart disease in individuals. By inputting 13 key health parameters, users can receive a real-time prediction indicating the presence or absence of heart disease.

---

## 🔬 Model Details

- **Algorithm**: Logistic Regression (Binary Classification)
- **Dataset**: Cleveland Heart Disease Dataset
- **Features**:
  1. Age
  2. Sex
  3. Chest Pain Type (cp)
  4. Resting Blood Pressure (trestbps)
  5. Serum Cholesterol (chol)
  6. Fasting Blood Sugar (fbs)
  7. Resting Electrocardiographic Results (restecg)
  8. Maximum Heart Rate Achieved (thalach)
  9. Exercise Induced Angina (exang)
  10. ST Depression Induced by Exercise (oldpeak)
  11. Slope of Peak Exercise ST Segment (slope)
  12. Number of Major Vessels Colored by Fluoroscopy (ca)
  13. Thalassemia (thal)

---

## 🚀 Features

- **User-Friendly Interface**: Built with Streamlit for easy interaction.
- **Real-Time Prediction**: Instant results upon input submission.
- **Visual Feedback**: Clear indicators for prediction outcomes.
- **Model Deployment**: Can be hosted on platforms like Streamlit Cloud or Heroku.

---

## 🛠️ Technologies Used

- **Python**: Programming language
- **Streamlit**: Framework for building the web application
- **Scikit-learn**: Machine learning library for model development
- **joblib**: For saving and loading the trained model
- **NumPy**: For numerical operations

---

## 📥 Installation & Usage

### Prerequisites

Ensure you have Python 3.7+ installed. Then, install the required packages:

```bash
pip install -r requirements.txt
streamlit run main.py
