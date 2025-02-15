import streamlit as st
import requests
import datetime

# Title
st.title("🚖 Taxi Fare Prediction")

st.markdown("Enter your ride details and get an estimated fare instantly!")

# Input Fields
st.subheader("Ride Details")

# Date and Time Selection
date = st.date_input("Pickup Date", datetime.date.today())
time = st.time_input("Pickup Time", datetime.datetime.now().time())

# Location Inputs
pickup_longitude = st.number_input("Pickup Longitude", value=-73.985428, format="%.6f")
pickup_latitude = st.number_input("Pickup Latitude", value=40.748817, format="%.6f")
dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.985428, format="%.6f")
dropoff_latitude = st.number_input("Dropoff Latitude", value=40.748817, format="%.6f")

# Passenger Count
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=6, value=1)

# Convert date & time to the required format
pickup_datetime = f"{date} {time}"

# 🚀 Replace with your own API URL if available
API_URL = "https://taxifare.lewagon.ai/predict"

# Make API request when the user clicks 'Predict Fare'
if st.button("Predict Fare"):
    params = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count,
    }

    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        fare = response.json().get("fare", "N/A")
        st.success(f"💰 Estimated Fare: ${fare:.2f}")
    else:
        st.error("❌ Error fetching prediction. Please try again.")
