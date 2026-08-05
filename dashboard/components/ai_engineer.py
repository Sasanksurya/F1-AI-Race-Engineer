import streamlit as st



def calculate_race_risk(

    prediction,

    strategy

):


    risk_score = 0



    win_probability = prediction.get(

        "win_probability",

        50

    )



    if win_probability < 40:

        risk_score += 40


    elif win_probability < 60:

        risk_score += 25



    else:

        risk_score += 10





    strategy_risk = strategy.get(

        "risk",

        "Medium"

    )



    if strategy_risk == "High":

        risk_score += 40


    elif strategy_risk == "Medium":

        risk_score += 25


    else:

        risk_score += 10




    if risk_score >= 70:

        return "High"



    elif risk_score >= 40:

        return "Medium"



    else:

        return "Low"





def render_ai_engineer(

    driver,

    circuit,

    session,

    prediction,

    strategy

):


    st.subheader(

        "AI Race Engineer Assistant"

    )



    # --------------------------------
    # Safety Handling
    # --------------------------------


    if prediction is None:


        prediction = {


            "win_probability":50,

            "podium_probability":70,

            "expected_position":5,

            "confidence":"Low",

            "reason":
            "Prediction unavailable"

        }





    if strategy is None:


        strategy = {


            "tyre":
            "Medium → Hard",


            "pit_window":
            "Lap 20-25",


            "reason":
            "Balanced race strategy",


            "confidence":
            "Medium",


            "risk":
            "Medium"

        }




    # --------------------------------
    # Calculate Overall Risk
    # --------------------------------


    race_risk = calculate_race_risk(

        prediction,

        strategy

    )





    # --------------------------------
    # Engineer Overview
    # --------------------------------


    st.markdown(

        f"""

## Race Engineer Summary


Driver:

**{driver}**


Circuit:

**{circuit}**


Session:

**{session}**



The AI race engineer analysed:


- FastF1 telemetry

- Driver performance

- Race prediction model

- Tyre strategy

- Pit window

- Circuit characteristics

- Race conditions


"""

    )



    st.divider()





    # --------------------------------
    # Prediction Dashboard
    # --------------------------------


    st.markdown(

        "## AI Race Prediction"

    )



    col1,col2,col3,col4 = st.columns(4)



    with col1:


        st.metric(

            "Win Probability",

            f"{prediction['win_probability']}%"

        )



    with col2:


        st.metric(

            "Podium Probability",

            f"{prediction['podium_probability']}%"

        )



    with col3:


        st.metric(

            "Expected Finish",

            f"P{prediction['expected_position']}"

        )



    with col4:


        st.metric(

            "Prediction Confidence",

            prediction.get(

                "confidence",

                "Medium"

            )

        )





    st.divider()




    # --------------------------------
    # Strategy Intelligence
    # --------------------------------


    st.markdown(

        "## AI Strategy Recommendation"

    )



    col1,col2 = st.columns(2)



    with col1:


        st.info(

            f"""

Recommended Tyre:


**{strategy.get('tyre')}**



Pit Window:


**{strategy.get('pit_window')}**



Reason:


{strategy.get('reason')}

"""

        )



    with col2:


        st.success(

            f"""

Strategy Confidence:


**{strategy.get('confidence')}**



Strategy Risk:


**{strategy.get('risk')}**

"""

        )




    st.divider()




    # --------------------------------
    # AI Decision Engine
    # --------------------------------


    win_probability = prediction.get(

        "win_probability",

        50

    )




    if win_probability >= 80:


        recommendation = (

            "Driver has race-winning potential. "

            "Maintain aggressive pace and protect tyre life."

        )



    elif win_probability >= 55:


        recommendation = (

            "Competitive performance detected. "

            "Strategy execution will decide the result."

        )



    else:


        recommendation = (

            "Focus on consistency, tyre preservation "

            "and minimizing performance loss."

        )





    st.markdown(

        "## Final AI Engineering Decision"

    )



    col1,col2 = st.columns(2)



    with col1:


        st.success(

            f"""

Race Recommendation:


{recommendation}

"""

        )



    with col2:


        st.warning(

            f"""

Current Race Risk:


**{race_risk}**



Risk Factors:


- Driver performance

- Tyre degradation

- Strategy timing

- Weather conditions

- Race incidents

"""

        )




    st.divider()




    # --------------------------------
    # AI Explanation
    # --------------------------------


    st.markdown(

        f"""

## AI Explanation


Prediction Analysis:


{prediction.get(

    "reason",

    "Telemetry based prediction completed."

)}



Strategy Analysis:


{strategy.get(

    "reason",

    "Race strategy generated."

)}

"""

    )




    st.divider()




    # --------------------------------
    # Final Engineer Instruction
    # --------------------------------


    st.markdown(

        """

## Final Engineer Instruction


The driver should:


- Follow the calculated tyre strategy

- Monitor tyre degradation

- Adapt to weather changes

- React to safety car periods

- Maintain race pace consistency



The AI engineer continuously evaluates race conditions and updates recommendations.

"""

    )