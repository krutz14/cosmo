import streamlit as st
import requests

st.title("Health Monitoring Dashboard")

# Fetch health data from Flask app
response = requests.get("http://127.0.0.1:5000/health")
health_data = response.json()

st.write("### Current Health Metrics")
st.write(f"Heart Rate: {health_data['heart_rate']} bpm")
st.write(f"Steps: {health_data['steps']} steps")
st.write(f"Sleep Duration: {health_data['sleep_duration']} hours")
st.write(f"Weight: {health_data['weight']} kg")
st.write(f"Blood Pressure: {health_data['blood_pressure']}")

# Update health metrics
new_steps = st.number_input("Update Steps", value=health_data['steps'])
if st.button("Update"):
    requests.post("http://127.0.0.1:5000/health", json={"steps": new_steps})
    st.success("Steps updated!")
