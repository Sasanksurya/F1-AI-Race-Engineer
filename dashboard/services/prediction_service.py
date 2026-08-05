from services.feature_engineering import create_race_features

from models.race_prediction_model import predict_race



def generate_prediction(

    telemetry,

    driver,

    constructor

):


    try:


        features = create_race_features(

            telemetry,

            driver,

            constructor

        )



        prediction = predict_race(

            features

        )



        if prediction is None:


            return {


                "win_probability":0,

                "podium_probability":0,

                "expected_position":10,

                "confidence":"Low",

                "reason":"Prediction model returned no result."

            }



        return prediction



    except Exception as e:


        return {


            "win_probability":0,

            "podium_probability":0,

            "expected_position":10,

            "confidence":"Low",

            "reason":f"Prediction failed: {str(e)}"

        }