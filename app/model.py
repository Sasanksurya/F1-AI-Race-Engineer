import joblib
import pandas as pd


model = joblib.load(
    "models/xgboost_podium_model.pkl"
)


def predict_podium(data):

    input_data = pd.DataFrame(
        [{
            "year": data.year,
            "round": data.round,
            "driverId": data.driverId,
            "constructorId": data.constructorId,
            "circuitId": data.circuitId,
            "grid": data.grid,
            "qualifying_position": data.qualifying_position,

            # default values for engineered features
            "driver_experience": 5,
            "constructor_experience": 5,
            "grid_advantage": data.grid - data.qualifying_position,
            "qualifying_advantage": data.qualifying_position - data.grid,

            "driver_avg_points": 5,
            "driver_podium_rate": 0.1,
            "constructor_podium_rate": 0.1,

            "recent_driver_points": 5,
            "recent_constructor_points": 5
        }]
    )


    probability = model.predict_proba(
        input_data
    )[0][1]


    return float(probability)