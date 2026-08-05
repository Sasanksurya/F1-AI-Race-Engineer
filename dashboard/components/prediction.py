import streamlit as st
import plotly.graph_objects as go


from services.prediction_service import generate_prediction



def render_prediction(

    telemetry,

    driver,

    constructor

):


    st.subheader(

        "AI Race Prediction Engine"

    )


    try:


        result = generate_prediction(

            telemetry,

            driver,

            constructor

        )


    except Exception as e:


        st.error(

            f"Prediction system error: {e}"

        )

        return None



    if result is None:


        st.warning(

            "Prediction data unavailable"

        )

        return None



    win = result.get(

        "win_probability",

        0

    )


    podium = result.get(

        "podium_probability",

        0

    )


    position = result.get(

        "expected_position",

        10

    )


    confidence = result.get(

        "confidence",

        "Medium"

    )


    reason = result.get(

        "reason",

        "Prediction generated from race performance data."

    )



    # --------------------------------
    # Metrics
    # --------------------------------


    col1,col2,col3,col4 = st.columns(4)



    with col1:


        st.metric(

            "Driver",

            driver

        )



    with col2:


        st.metric(

            "Win Probability",

            f"{win}%"

        )



    with col3:


        st.metric(

            "Podium Probability",

            f"{podium}%"

        )



    with col4:


        st.metric(

            "Expected Finish",

            f"P{position}"

        )



    st.divider()



    # --------------------------------
    # AI Analysis
    # --------------------------------


    st.info(

        f"""

AI Engineer Prediction


{reason}



Prediction Confidence:

{confidence}

"""

    )



    st.divider()



    # --------------------------------
    # Probability Chart
    # --------------------------------


    fig = go.Figure()



    fig.add_trace(

        go.Bar(

            x=[

                "Win",

                "Podium",

                "Top 10"

            ],


            y=[

                win,

                podium,

                max(

                    0,

                    100-position*5

                )

            ],

            name="Probability"

        )

    )



    fig.update_layout(

        title="Race Outcome Probability",

        template="plotly_dark",

        height=350

    )



    st.plotly_chart(

        fig,

        use_container_width=True

    )



    st.divider()



    # --------------------------------
    # Summary
    # --------------------------------


    st.markdown(

        f"""

## Race Prediction Summary


Driver:

**{driver}**


Constructor:

**{constructor}**


Expected Position:

**P{position}**


Factors Evaluated:

- Telemetry performance

- Race pace

- Tyre management

- Constructor strength

- Race conditions


"""

    )


    return result