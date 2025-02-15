import streamlit as st
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')


#collect user input

st.markdown("## Enter Ride Details:")

pickup_date = st.date_input('Pickup Date')
pickup_time = st.time_input('Pickup Time')
pickup_longitude = st.number_input('Pickup Longitude')
pickup_latitude = st.number_input('Pickup Latitude')
dropoff_longitude = st.number_input('Dropoff Longitude')
dropoff_latitude = st.number_input('Dropoff Latitude')
passenger_count = st.number_input('Passenger Count', min_value=1, max_value=8, step=1)


url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


params = {
    'pickup_datetime': f'{pickup_date} {pickup_time}',
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': passenger_count
    }

api_url = 'https://taxifare.lewagon.ai/predict'

response = requests.get(api_url, params=params)

#st.write(f'The estimated fare is: ${fare}')
#st.write('The estimated fare is: $10.0')

fare = response.json().get("fare")
