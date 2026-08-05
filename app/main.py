from fastapi import FastAPI

from app.schemas import PredictionInput
from app.model import predict_podium


app = FastAPI(
    title="F1 AI Racing API",
    version="1.0"
)


@app.get("/")
def home():

    return {
        "message": "F1 AI Racing API Running Successfully"
    }


@app.post("/predict")
def predict(
    data: PredictionInput
):

    probability = predict_podium(data)

    return {
        "model": "XGBoost Podium Prediction",
        "podium_probability": round(probability, 4),
        "podium_percentage": round(probability * 100, 2)
    }