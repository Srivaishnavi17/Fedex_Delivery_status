import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open(r"Fedex.pkl",'rb'))
#st.image("innomatics-research-labs-logo-squared.png")
#st.image("fedex_logo.jpg")
st.title("FedEx  Delivery Status")

numerical_features = ['Carrier_Num', 'Distance'] 
categorical_features = {
    'Year': [2008], 
    'Month': [1, 2, 3, 4, 5, 6],  
    'DayofMonth': list(range(1, 32)),
    'DayOfWeek': list(range(1, 8)),  
    'Carrier_Name': ['WN', 'XE', 'YV', 'OH', 'OO', 'UA', 'US', 'DL', 'EV', 'F9', 'FL',
       'HA', 'MQ', 'NW', '9E', 'AA', 'AQ', 'AS', 'B6', 'CO']
}
categories = ['Source', 'Destination']


input_data = {}

for feature, options in categorical_features.items():
    input_data[feature] = st.selectbox(f'Select {feature}', options)

for feature in numerical_features:
    input_value = st.number_input(f'Enter {feature}', min_value=0, step=1)
    input_data[feature] = int(input_value)

for feature in categories:
    input_data[feature] = st.text_input(" Enter  : {}".format(feature))

st.write("Enter Actual Shipment Time")
hours1 = st.selectbox("Select hours", list(range(0, 24)), key="hours1")
minutes1 = st.selectbox("Select minutes", list(range(0, 60)), key="minutes1")
total_minutes1 = hours1 * 60 + minutes1

st.write("Enter Planned Shipment Time")
hours2 = st.selectbox("Select hours", list(range(0, 24)), key="hours2")
minutes2 = st.selectbox("Select minutes", list(range(0, 60)), key="minutes2")
total_minutes2 = hours2 * 60 + minutes2

st.write("Enter Planned Delivery Time")
hours3 = st.selectbox("Select hours", list(range(0, 24)), key="hours3")
minutes3 = st.selectbox("Select minutes", list(range(0, 60)), key="minutes3")
total_minutes3 = hours3 * 60 + minutes3

st.write("Enter Planned Time of Travel")
hours4 = st.selectbox("Select hours", list(range(0, 12)), key="hours4")
minutes4 = st.selectbox("Select minutes", list(range(0, 60)), key="minutes4")
total_minutes4 = hours4 * 60 + minutes4

st.write("Enter Shipment Delay Time")
hours5 = st.selectbox("Select hours", list(range(0, 43)), key="hours5")
minutes5 = st.selectbox("Select minutes", list(range(0, 60)), key="minutes5")
total_minutes5 = hours5 * 60 + minutes5


input_data['Actual_Shipment_Time'] = total_minutes1
input_data['Planned_Shipment_Time'] = total_minutes2
input_data['Planned_Delivery_Time'] = total_minutes3
input_data['Planned_TimeofTravel'] = total_minutes4
input_data['Shipment_Delay'] = total_minutes5


input_df = pd.DataFrame([input_data])


if st.button('Predict'):
    prediction = model.predict(input_df)

    if prediction[0] == 0:
        st.write('Status: Not Delivered')
        #st.image("not_delivered.jpeg",width=400)

    else:
        st.write('Status: Delivered')