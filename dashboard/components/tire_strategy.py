import streamlit as st
import plotly.graph_objects as go



def render_tire_strategy(

    telemetry,

    circuit,

    driver

):


    st.subheader(

        "AI Tire Strategy Engine"

    )



    # --------------------------------
    # Default Values
    # --------------------------------


    compound = "Medium"

    tyre_age = 0

    wear = 0



    # --------------------------------
    # Telemetry Analysis
    # --------------------------------


    if telemetry is not None:


        try:


            tyre_age = len(telemetry)



            if tyre_age >= 30:


                wear = 90



            elif tyre_age >= 20:


                wear = 70



            elif tyre_age >= 10:


                wear = 45



            else:


                wear = 25



            # Estimate compound

            if wear > 80:


                compound = "Hard"



            elif wear > 50:


                compound = "Medium"



            else:


                compound = "Soft"



        except Exception:


            pass



    # --------------------------------
    # Metrics
    # --------------------------------


    col1,col2,col3,col4 = st.columns(4)



    with col1:


        st.metric(

            "Current Compound",

            compound

        )



    with col2:


        st.metric(

            "Tyre Age",

            f"{tyre_age} laps"

        )



    with col3:


        st.metric(

            "Estimated Wear",

            f"{wear}%"

        )



    with col4:


        if wear >= 80:

            status = "Critical"

        elif wear >= 60:

            status = "Warning"

        else:

            status = "Healthy"



        st.metric(

            "Tyre Status",

            status

        )



    st.divider()



    # --------------------------------
    # Degradation Curve
    # --------------------------------


    laps = list(

        range(

            1,

            max(

                tyre_age,

                30

            )

        )

    )



    degradation = [

        min(

            100,

            15 + lap * 2.8

        )

        for lap in laps

    ]



    fig = go.Figure()



    fig.add_trace(

        go.Scatter(

            x=laps,

            y=degradation,

            mode="lines",

            name="Tyre Wear"

        )

    )



    fig.update_layout(

        title="Tyre Degradation Prediction",

        xaxis_title="Lap",

        yaxis_title="Wear Percentage",

        template="plotly_dark",

        height=350

    )



    st.plotly_chart(

        fig,

        use_container_width=True

    )



    st.divider()



    # --------------------------------
    # AI Recommendation
    # --------------------------------


    if wear >= 80:


        recommendation = (

            "Tyre degradation is critical. "

            "Pit stop recommended immediately."

        )


        strategy = (

            "Switch to Hard compound"

        )



        confidence = "92%"



    elif wear >= 60:


        recommendation = (

            "Tyre performance is dropping. "

            "Prepare pit window."

        )


        strategy = (

            "Medium to Hard strategy"

        )


        confidence = "85%"



    else:


        recommendation = (

            "Tyre performance is stable. "

            "Continue current stint."

        )


        strategy = (

            "Maintain current compound"

        )


        confidence = "80%"



    st.markdown(

        f"""

## AI Tire Recommendation


Driver:

{driver}



Circuit:

{circuit}



Current Compound:

**{compound}**



Recommended Strategy:

**{strategy}**



Analysis:

{recommendation}



Strategy Confidence:

**{confidence}**

"""

    )