import pandas as pd



def create_race_features(

    telemetry,

    driver,

    constructor

):


    features = {}


    features["driver"] = driver

    features["constructor"] = constructor



    if telemetry is not None and not telemetry.empty:


        features["max_speed"] = float(

            telemetry["Speed"].max()

        )


        features["average_speed"] = float(

            telemetry["Speed"].mean()

        )


        features["avg_throttle"] = float(

            telemetry["Throttle"].mean()

        )


        features["avg_brake"] = float(

            telemetry["Brake"].mean()

        )



        if "nGear" in telemetry.columns:


            features["max_gear"] = int(

                telemetry["nGear"].max()

            )

        else:


            features["max_gear"] = 0



        # New features


        if "Distance" in telemetry.columns:


            features["lap_distance"] = float(

                telemetry["Distance"].max()

            )

        else:


            features["lap_distance"] = 0



    else:


        features["max_speed"] = 0

        features["average_speed"] = 0

        features["avg_throttle"] = 0

        features["avg_brake"] = 0

        features["max_gear"] = 0

        features["lap_distance"] = 0



    return pd.DataFrame(

        [features]

    )