import pandas as pd
import pickle as pk
import streamlit as st

model = pk.load(open(r"C:\Users\hema\Downloads\NEW_FOLDER\PROJECT\House_prediction_model.pkl", "rb"))

st.header("House Price Predictor")
data = pd.read_csv(r"C:\Users\hema\Downloads\NEW_FOLDER\PROJECT\Cleaned_data.csv")
beds = st.selectbox("Choose no of bedrooms", data["bedrooms"].unique())
baths = st.selectbox("Choose no of bathrooms", data["bathrooms"].unique())
sqft = st.selectbox("Choose no of sqft", data["sqft_living"].unique())
floors = st.selectbox("Choose no of floors", data["floors"].unique())
above = st.selectbox("Choose no of sqft_above", data["sqft_above"].unique())
basement = st.selectbox("Choose no of sft_basement", data["sqft_basement"].unique())
year = st.selectbox("Choose no of yr_built", data["yr_built"].unique())

input = pd.DataFrame([[beds,baths,sqft,floors,above,basement,year]], columns = ["bedrooms","bathrooms","sqft_living","floors","sqft_above","sqft_basement","yr_built"])

if st.button("Predict Price"):
    predicted_price = model.predict(input)[0]
    price_in_lakhs = predicted_price / 10000
    st.write(f"Predicted House Price: {price_in_lakhs:.2f} lakhs")