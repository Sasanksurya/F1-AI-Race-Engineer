import pandas as pd



def safe_value(value):


    if isinstance(value, pd.Series):

        return float(value.iloc[0])


    return float(value)



def predict_race(features):


    max_speed = safe_value(

        features["max_speed"]

    )


    average_speed = safe_value(

        features["average_speed"]

    )


    throttle = safe_value(

        features["avg_throttle"]

    )


    brake = safe_value(

        features["avg_brake"]

    )


    gear = safe_value(

        features["max_gear"]

    )


    distance = safe_value(

        features["lap_distance"]

    )



    score = 0


    reasons = []



    # Speed Performance

    if max_speed >= 320:

        score += 25

        reasons.append(

            "Excellent top speed performance"

        )


    elif max_speed >= 280:

        score += 18

        reasons.append(

            "Competitive straight line speed"

        )


    else:

        score += 10



    # Race Pace

    if average_speed >= 220:

        score += 25

        reasons.append(

            "Strong average race pace"

        )


    elif average_speed >= 180:

        score += 15



    else:

        score += 5



    # Driver Control

    if throttle >= 70:

        score += 15

        reasons.append(

            "Strong throttle application"

        )


    else:

        score += 8



    # Braking Efficiency

    if brake < 30:

        score += 15

        reasons.append(

            "Efficient braking behaviour"

        )


    else:

        score += 5



    # Gear usage

    if gear >= 8:

        score += 10



    # Telemetry completeness

    if distance > 4000:

        score += 5



    win_probability = min(

        score,

        95

    )



    podium_probability = min(

        score + 15,

        99

    )



    if win_probability >= 80:

        position = 1


    elif win_probability >= 65:

        position = 2


    elif win_probability >= 50:

        position = 3


    else:

        position = 5



    if win_probability >= 80:

        confidence = "High"


    elif win_probability >= 60:

        confidence = "Medium"


    else:

        confidence = "Low"



    return {


        "win_probability": int(win_probability),


        "podium_probability": int(podium_probability),


        "expected_position": position,


        "confidence": confidence,


        "reason":

            ". ".join(reasons)

    }