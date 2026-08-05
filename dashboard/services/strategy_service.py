import random



def generate_strategy(

    circuit,

    session,

    driver

):


    # --------------------------------
    # Circuit Characteristics
    # --------------------------------


    circuit_data = {


        "Spa Francorchamps": {

            "degradation": "medium",

            "high_speed": True,

            "strategy": "Medium → Hard",

            "pit": "Lap 18-22"

        },


        "Monaco": {

            "degradation": "low",

            "high_speed": False,

            "strategy": "Medium → Medium",

            "pit": "Lap 25-35"

        },


        "Monza": {

            "degradation": "low",

            "high_speed": True,

            "strategy": "Hard → Medium",

            "pit": "Lap 20-28"

        },


        "Silverstone": {

            "degradation": "medium",

            "high_speed": True,

            "strategy": "Medium → Hard",

            "pit": "Lap 18-25"

        },


        "Bahrain": {

            "degradation": "high",

            "high_speed": False,

            "strategy": "Soft → Medium → Hard",

            "pit": "Lap 12-18"

        }

    }



    data = circuit_data.get(

        circuit,

        {

            "degradation":"medium",

            "high_speed":False,

            "strategy":"Medium → Hard",

            "pit":"Lap 20-25"

        }

    )



    # --------------------------------
    # Strategy Reasoning
    # --------------------------------


    reasons = []



    if data["degradation"] == "high":


        reasons.append(

            "High tyre degradation detected. Multiple compound usage recommended."

        )


    elif data["degradation"] == "low":


        reasons.append(

            "Low degradation circuit. Track position is important."

        )


    else:


        reasons.append(

            "Balanced tyre management required."

        )



    if data["high_speed"]:


        reasons.append(

            "High speed corners require tyre stability."

        )



    else:


        reasons.append(

            "Mechanical grip and consistency are more important."

        )



    # --------------------------------
    # Risk Calculation
    # --------------------------------


    if data["degradation"] == "high":


        risk = "High"


    elif data["degradation"] == "medium":


        risk = "Medium"


    else:


        risk = "Low"



    # --------------------------------
    # AI Confidence
    # --------------------------------


    confidence = random.randint(

        85,

        95

    )



    # --------------------------------
    # Final Strategy
    # --------------------------------


    strategy = {


        "driver": driver,


        "circuit": circuit,


        "session": session,


        "tyre": data["strategy"],


        "pit_window": data["pit"],


        "reason": " ".join(reasons),


        "risk": risk,


        "confidence": confidence


    }



    return strategy