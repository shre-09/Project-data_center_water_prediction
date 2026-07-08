import streamlit as st
import pandas as pd
import joblib

# 1. Load Model
model = joblib.load("water_prediction_model.pkl")

st.set_page_config(page_title="AI Data Center Water Prediction", layout="centered")

st.title("💧 AI Data Center Water Consumption Prediction")
st.write("Enter the details below to predict water consumption.")

# 2. Numeric Inputs (Sirf wahi 6 features jo model training me use hue the)
gpu = st.number_input("GPU Utilization (%)", 0, 100, 70)
power = st.number_input("Power Consumption (kW)", 0, 1000, 350)
machine_temp = st.number_input("Machine Temperature (°C)", 0, 100, 45)
ambient_temp = st.number_input("Ambient Temperature (°C)", 0, 60, 30)
humidity = st.number_input("Humidity (%)", 0, 100, 50)
active_servers = st.number_input("Active Servers", 1, 500, 50)

# 3. Input DataFrame (Exact wahi sequence aur 6 columns jo notebook me the)
input_df = pd.DataFrame({
    "GPU_Utilization (%)": [gpu],
    "Machine_Temperature (°C)": [machine_temp],
    "Ambient_Temperature (°C)": [ambient_temp],
    "Humidity (%)": [humidity],
    "Active_Servers": [active_servers],
    "Power_Consumption (kW)": [power]
})

# 4. Prediction Button
if st.button("Predict Water Consumption"):
    prediction = model.predict(input_df)
    st.success(f"💧 Predicted Water Consumption: {prediction[0]:.2f} L/hr")
