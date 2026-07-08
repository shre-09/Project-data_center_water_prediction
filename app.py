import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("water_prediction_model.pkl")

st.set_page_config(page_title="AI Data Center Water Prediction", layout="centered")

st.title("💧 AI Data Center Water Consumption Prediction")
st.write("Enter the details below to predict water consumption.")

# Numeric Inputs
gpu = st.number_input("GPU Utilization (%)", 0, 100, 70)
power = st.number_input("Power Consumption (kW)", 0, 1000, 350)
machine_temp = st.number_input("Machine Temperature (°C)", 0, 100, 45)
ambient_temp = st.number_input("Ambient Temperature (°C)", 0, 60, 30)
humidity = st.number_input("Humidity (%)", 0, 100, 50)
active_servers = st.number_input("Active Servers", 1, 500, 50)

# Categorical Inputs
season = st.selectbox(
    "Season",
    ["Monsoon", "Spring", "Summer", "Winter"]
)

cooling = st.selectbox(
    "Cooling Method",
    ["Air", "Evaporative", "Liquid"]
)

# One-Hot Encoding
season_monsoon = 1 if season == "Monsoon" else 0
season_spring = 1 if season == "Spring" else 0
season_summer = 1 if season == "Summer" else 0
season_winter = 1 if season == "Winter" else 0

cooling_evaporative = 1 if cooling == "Evaporative" else 0
cooling_liquid = 1 if cooling == "Liquid" else 0

# Input DataFrame
input_df = pd.DataFrame({
    "GPU_Utilization (%)":[gpu],
    "Power_Consumption (kW)":[power],
    "Machine_Temperature (°C)":[machine_temp],
    "Ambient_Temperature (°C)":[ambient_temp],
    "Humidity (%)":[humidity],
    "Active_Servers":[active_servers],
    "Season_Monsoon":[season_monsoon],
    "Season_Spring":[season_spring],
    "Season_Summer":[season_summer],
    "Season_Winter":[season_winter],
    "Cooling_Method_Evaporative":[cooling_evaporative],
    "Cooling_Method_Liquid":[cooling_liquid]
})

if st.button("Predict Water Consumption"):

    prediction = model.predict(input_df)

    st.success(f"💧 Predicted Water Consumption: {prediction[0]:.2f} L/hr")
