import streamlit as st
import joblib

model = joblib.load("credit_card_model.pkl")

st.title("Credit Card Fraud Detection")

data = st.text_input("Enter 30 values separated by commas")

if st.button("Predict"):
    values = [float(x) for x in data.split(",")]
    prediction = model.predict([values])

    if prediction[0] == 0:
        st.success("Normal Transaction")
    else:
        st.error("Fraudulent Transaction")