def calculate_tire_strategy(

    telemetry,

    circuit,

    driver

):


    tyre_wear = 70


    # Analyse telemetry if available

    if telemetry is not None:

        try:

            if "Speed" in telemetry.columns:


                avg_speed = telemetry["Speed"].mean()


                if avg_speed > 250:

                    tyre_wear = 82


                elif avg_speed > 200:

                    tyre_wear = 65


                else:

                    tyre_wear = 50


        except Exception:


            tyre_wear = 70



    # Strategy decision


    if tyre_wear >= 75:


        strategy = {


            "current_tyre": "Medium",

            "wear": tyre_wear,

            "recommended": "Hard",

            "pit_window": "Lap 18-22",

            "reason":
            "High tyre degradation detected. Hard compound recommended for race finish."

        }



    elif tyre_wear >= 50:


        strategy = {


            "current_tyre": "Medium",

            "wear": tyre_wear,

            "recommended": "Medium → Hard",

            "pit_window": "Lap 22-28",

            "reason":
            "Balanced tyre performance detected. One-stop strategy recommended."

        }



    else:


        strategy = {


            "current_tyre": "Soft",

            "wear": tyre_wear,

            "recommended": "Medium",

            "pit_window": "Lap 15-20",

            "reason":
            "Low degradation detected. Medium compound provides consistency."

        }



    return strategy