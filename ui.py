import streamlit as st
import numpy as np
import requests  # We will use requests to call FastAPI

# Streamlit UI
st.title("Breast Cancer Classification")
st.write(
    """
    Enter the tumor features below, and the model will classify the tumor as:
    - **0**: Benign
    - **1**: Malignant
    """
)

# Input fields for tumor features
st.header("Input Tumor Features")
features = []
for i in range(1, 31):
    value = st.number_input(f"Feature {i}", value=0.0, step=0.01)
    features.append(value)

# Classify button
if st.button("Classify"):
    # Send the features to FastAPI for prediction
    api_url = "http://localhost:8000/predict"  # Change to EC2 IP if running on remote server
    response = requests.post(api_url, json={"features": features})

    if response.status_code == 200:
        prediction = response.json()
        # Display result based on prediction
        if prediction["prediction"] == 1:
            st.error("The tumor is predicted to be **Malignant**.")
        else:
            st.success("The tumor is predicted to be **Benign**.")
    else:
        st.error("Failed to get a prediction. Please try again.")
