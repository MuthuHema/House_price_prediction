import pandas as pd
import pickle as pk
import streamlit as st

# Corrected file path using raw string (r"")
model = pk.load(open(r"C:\Users\hema\Documents\PythonProject\.ipynb_checkpoints\House_prediction_model.pkl", "rb"))

st.header("House Price Predictor")

# Corrected file path for CSV
data = pd.read_csv(r"C:\Users\hema\Documents\PythonProject\.ipynb_checkpoints\Cleaned_data.csv")

loc = st.selectbox("Choose the location", data["location"].unique())
sqft = st.number_input("Enter total sqft")
beds = st.number_input("Enter No of Bedrooms")
bath = st.number_input("Enter No of Bathrooms")
balc = st.number_input("Enter No of Balconies")

input_df = pd.DataFrame([[loc, sqft, bath, balc, beds]], columns=['location', 'total_sqft', 'bath', 'balcony', 'bedrooms'])

if st.button("Predict Price"):
    output = model.predict(input_df)
    st.write(f"Price of the House is ₹{output[0] * 100000:.2f}")

