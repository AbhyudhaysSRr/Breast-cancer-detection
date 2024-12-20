from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
import threading
import numpy as np
import joblib

# Load the trained Logistic Regression model
model = joblib.load("best_logistic_regression_model.pkl")

# FastAPI Application
fastapi_app = FastAPI()

# Pydantic schema for FastAPI
class PredictionInput(BaseModel):
    features: list[float]  # List of 30 feature values

@fastapi_app.post("/predict")
async def predict(input_data: PredictionInput):
    # Convert input features to a numpy array
    input_array = np.array(input_data.features).reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(input_array)
    
    return JSONResponse(content={"prediction": int(prediction[0])})

# Threading to run Streamlit and FastAPI together
def start_fastapi():
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)

def start_streamlit():
    import subprocess
    import os
    # Ensure we are running Streamlit from the correct directory
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current working directory
    streamlit_cmd = ["streamlit", "run", os.path.join(current_dir, "ui.py")]
    subprocess.run(streamlit_cmd)

if __name__ == "__main__":
    # Start FastAPI in one thread
    fastapi_thread = threading.Thread(target=start_fastapi)
    fastapi_thread.start()

    # Start Streamlit in another thread
    streamlit_thread = threading.Thread(target=start_streamlit)
    streamlit_thread.start()

    # Wait for both threads to finish
    fastapi_thread.join()
    streamlit_thread.join()