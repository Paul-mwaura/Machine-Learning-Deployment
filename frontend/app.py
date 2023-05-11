# Streamlit user interface for the model
import requests
import streamlit as st


# Streamlit app title
st.title("Car Price Prediction Web Application") 
st.write("This web application predicts the price of a car based on its features.")


# Input feature 1: Buying Price
buying = st.radio("Buying Price", ("vhigh", "high", "med", "low"))

# Input feature 2: Maintenance Price
maintenance = st.radio("Maintenance Price", ("vhigh", "high", "med", "low"))

# Input feature 3: Number of Doors
doors = st.radio("Number of Doors", ("2", "3", "4", "5more"))

# Input feature 4: Capacity
capacity = st.radio("Capacity", ("2", "4", "more"))

# Input feature 5: Size of Luggage Boot
lug_boot = st.radio("Size of Luggage Boot", ("small", "med", "big"))

# Input feature 6: Estimated Safety of the Car
safety = st.radio("Estimated Safety of the Car", ("low", "med", "high"))

# Class values to be returned by the model
class_values = {
    0: "unacceptable",
    1: "acceptable",
    2: "good",
    3: "very good"
}

# When 'Submit' button is pressed, run the following code
if st.button("Submit"):
    # Inputs to the model
    inputs ={
        "inputs": [
            {
                "buying": buying,
                "maintenance": maintenance,
                "doors": doors,
                "capacity": capacity,
                "lug_boot": lug_boot,
                "safety": safety
            }
        ]
    } 
    
# Posting inputs to the model and getting back the predicted class
response = requests.post("http://localhost:8000/predict", json=inputs)
json_response = response.json()
prediction = class_values[json_response.get("predictions")[0]]

st.subheader(f"The predicted class is {prediction}")