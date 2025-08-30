import joblib
import streamlit as st
import numpy as np

model = joblib.load('model.pkl')

st.title("Heart Disease Prediction")

inputs = {}

age = st.text_input("Age")
if age:
    if age.isdigit():
        inputs["Age"] = int(age)
    else:
        st.error("Age must be a number!")

gender = st.radio("Gender", ["Male", "Female"])
inputs["Gender"] = 1 if gender == "Male" else 0

cp = st.text_input("Cp (0-3)")
if cp:
    if cp.isdigit():
        inputs["Cp"] = int(cp)
    else:
        st.error("Cp must be a number!")

trestbps = st.text_input("Trestbps")
if trestbps:
    try:
        inputs["Trestbps"] = float(trestbps)
    except ValueError:
        st.error("Trestbps must be a number!")

chol = st.text_input("Chol")
if chol:
    try:
        inputs["Chol"] = float(chol)
    except ValueError:
        st.error("Chol must be a number!")

fbs = st.text_input("Fbs (0 = false; 1 = true)")
if fbs:
    if fbs in ["0", "1"]:
        inputs["Fbs"] = int(fbs)
    else:
        st.error("Fbs must be 0 or 1!")

restecg = st.text_input("restecg")
if restecg:
    try:
        inputs["restecg"] = float(restecg)
    except ValueError:
        st.error("restecg must be a number!")

thalach = st.text_input("Thalach")
if thalach:
    try:
        inputs["Thalach"] = float(thalach)
    except ValueError:
        st.error("Thalach must be a number!")

exang = st.text_input("Exang (0 = no; 1 = yes)")
if exang:
    if exang in ["0", "1"]:
        inputs["Exang"] = int(exang)
    else:
        st.error("Exang must be 0 or 1!")

oldpeak = st.text_input("Oldpeak")
if oldpeak:
    try:
        inputs["Oldpeak"] = float(oldpeak)
    except ValueError:
        st.error("Oldpeak must be a number!")

slope = st.text_input("Slope")
if slope:
    try:
        inputs["Slope"] = float(slope)
    except ValueError:
        st.error("Slope must be a number!")

ca = st.text_input("Ca")
if ca:
    try:
        inputs["Ca"] = float(ca)
    except ValueError:
        st.error("Ca must be a number!")

thal = st.text_input("Thal")
if thal:
    try:
        inputs["Thal"] = float(thal)
    except ValueError:
        st.error("Thal must be a number!")

required_keys = ["Age","Gender","Cp","Trestbps","Chol","Fbs",
                 "restecg","Thalach","Exang","Oldpeak","Slope","Ca","Thal"]

if all(key in inputs for key in required_keys):
    if st.button("Predict"):
        X = np.array([inputs[key] for key in required_keys]).reshape(1, -1)
        
        prediction = model.predict(X)[0]
        
        if prediction == 0:
            st.success("Prediction: No Heart Disease ❤️")
        else:
            st.error("Prediction: Heart Disease ⚠️")
else:
    st.info("Please fill all fields to enable prediction.")
