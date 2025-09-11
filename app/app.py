import streamlit as st
import joblib
import pandas as pd

st.title("🏠 House Price Predictor")

model = joblib.load("C:/Users/Admin/OneDrive/Desktop/Puneeth/houseprice-ml-lab/model.pkl")

with st.form("predict"):
    locality = st.selectbox("Locality (e.g., BTM Layout)", ["BTM Layout", "Yalahanka", "Indiranagar", "Electronic City", "Marathahalli","K R Puram","Attibele","Jayanagar"])
    area = st.number_input("Area", value=1000)
    rent = st.number_input("Monthly Rent", value=15000)
    facing = st.text_input("Facing (North/South/East/West)", "North")
    BHK = st.number_input("Bedrooms", value=2, min_value=0, max_value=10, step=1)
    bathrooms = st.number_input("Bathrooms", value=2, min_value=0, max_value=10, step=1)
    parking = st.selectbox("Parking (Bike/Car/Both)", ["Bike", "Car", "Bike and Car", "None"])
    submitted = st.form_submit_button("Predict")

if submitted:
    X = pd.DataFrame([{
        "rent": rent,
        "area": area,
        "locality": locality if locality else "Missing",
        "BHK": BHK,
        "bathrooms": bathrooms,
        "facing": facing if facing else "Missing",
        "parking": parking if parking else "Missing"
    }])
    pred = model.predict(X)[0]
    st.success(f"Predicted Price: {pred:,.2f}")
