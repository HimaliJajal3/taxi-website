import streamlit as st
import requests


st.markdown('''
Enter your ride details to estimate the fare.
''')


#collect user input

st.markdown("## Enter Ride Details:")

pickup_date = st.date_input('Pickup Date')
pickup_time = st.time_input('Pickup Time')
pickup_longitude = st.number_input('Pickup Longitude', format="%.6f")
pickup_latitude = st.number_input('Pickup Latitude', format="%.6f")
dropoff_longitude = st.number_input('Dropoff Longitude', format="%.6f")
dropoff_latitude = st.number_input('Dropoff Latitude', format="%.6f")
passenger_count = st.number_input('Passenger Count', min_value=1, max_value=8, step=1)


api_url = 'https://taxifare.lewagon.ai/predict'

# Prediction button
if st.button('Get Fare Estimate'):
    params = {
        'pickup_datetime': f'{pickup_date} {pickup_time}',
        'pickup_longitude': pickup_longitude,
        'pickup_latitude': pickup_latitude,
        'dropoff_longitude': dropoff_longitude,
        'dropoff_latitude': dropoff_latitude,
        'passenger_count': passenger_count
    }

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an error for bad responses

        fare = response.json().get("fare")
        if fare is not None:
            st.success(f'The estimated fare is: **${fare:.2f}**')
        else:
            st.error('Could not fetch the fare estimate. Please check your inputs.')

    except requests.exceptions.RequestException as e:
        st.error(f"API request failed: {e}")
