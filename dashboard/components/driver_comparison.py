import streamlit as st
import plotly.graph_objects as go


from services.fastf1_service import (
    load_session,
    get_driver_telemetry
)


from data.drivers import DRIVERS




# --------------------------------
# Calculate Driver Metrics
# --------------------------------

def calculate_driver_metrics(telemetry):


    if telemetry is None or telemetry.empty:

        return None



    metrics = {}



    if "Speed" in telemetry.columns:


        metrics["max_speed"] = round(

            telemetry["Speed"].max(),

            2

        )


        metrics["average_speed"] = round(

            telemetry["Speed"].mean(),

            2

        )


    else:


        metrics["max_speed"] = 0

        metrics["average_speed"] = 0




    if "Throttle" in telemetry.columns:


        metrics["throttle"] = round(

            telemetry["Throttle"].mean(),

            2

        )

    else:


        metrics["throttle"] = 0




    if "Brake" in telemetry.columns:


        metrics["brake"] = round(

            telemetry["Brake"].mean(),

            2

        )

    else:


        metrics["brake"] = 0




    if "nGear" in telemetry.columns:


        metrics["gear"] = int(

            telemetry["nGear"].max()

        )

    else:


        metrics["gear"] = 0



    return metrics





# --------------------------------
# Driver Comparison Component
# --------------------------------

def render_driver_comparison(

    year,

    event,

    session,

    selected_driver

):


    st.subheader(

        "AI Driver Comparison and Rival Analysis"

    )



    drivers = list(

        DRIVERS.keys()

    )



    default_index = drivers.index(

        selected_driver

    )



    col1,col2 = st.columns(2)



    with col1:


        driver_1 = st.selectbox(

            "Select Driver 1",

            drivers,

            index=default_index

        )




    with col2:


        driver_options = [

            d

            for d in drivers

            if d != driver_1

        ]


        driver_2 = st.selectbox(

            "Select Driver 2",

            driver_options

        )




    st.divider()



    # --------------------------------
    # Load FastF1 Session
    # --------------------------------


    with st.spinner(

        "Loading FastF1 telemetry..."

    ):


        f1_session = load_session(

            year,

            event,

            session

        )



    if f1_session is None:


        st.warning(

            "FastF1 session unavailable"

        )

        return





    # --------------------------------
    # Driver Codes
    # --------------------------------


    code_1 = DRIVERS[driver_1]["code"]

    code_2 = DRIVERS[driver_2]["code"]





    # --------------------------------
    # FIXED TELEMETRY CALL
    # --------------------------------


    telemetry_1 = get_driver_telemetry(

        f1_session,

        code_1

    )



    telemetry_2 = get_driver_telemetry(

        f1_session,

        code_2

    )






    metrics_1 = calculate_driver_metrics(

        telemetry_1

    )


    metrics_2 = calculate_driver_metrics(

        telemetry_2

    )



    if metrics_1 is None or metrics_2 is None:


        st.warning(

            "Driver telemetry unavailable"

        )

        return





    # --------------------------------
    # Driver Comparison Cards
    # --------------------------------


    col1,col2 = st.columns(2)



    with col1:


        st.markdown(

            f"""

## {driver_1}


Team:

{DRIVERS[driver_1]["team"]}



Maximum Speed:

{metrics_1["max_speed"]} km/h



Average Speed:

{metrics_1["average_speed"]} km/h



Throttle Efficiency:

{metrics_1["throttle"]}%



Brake Usage:

{metrics_1["brake"]}%



Maximum Gear:

{metrics_1["gear"]}

"""

        )





    with col2:


        st.markdown(

            f"""

## {driver_2}


Team:

{DRIVERS[driver_2]["team"]}



Maximum Speed:

{metrics_2["max_speed"]} km/h



Average Speed:

{metrics_2["average_speed"]} km/h



Throttle Efficiency:

{metrics_2["throttle"]}%



Brake Usage:

{metrics_2["brake"]}%



Maximum Gear:

{metrics_2["gear"]}

"""

        )





    st.divider()




    # --------------------------------
    # Performance Comparison Chart
    # --------------------------------


    categories = [

        "Max Speed",

        "Average Speed",

        "Throttle",

        "Gear"

    ]



    values_1 = [

        metrics_1["max_speed"],

        metrics_1["average_speed"],

        metrics_1["throttle"],

        metrics_1["gear"]

    ]



    values_2 = [

        metrics_2["max_speed"],

        metrics_2["average_speed"],

        metrics_2["throttle"],

        metrics_2["gear"]

    ]




    fig = go.Figure()



    fig.add_trace(

        go.Bar(

            name=driver_1,

            x=categories,

            y=values_1

        )

    )



    fig.add_trace(

        go.Bar(

            name=driver_2,

            x=categories,

            y=values_2

        )

    )



    fig.update_layout(

        title="Real FastF1 Telemetry Comparison",

        barmode="group",

        template="plotly_dark",

        height=400

    )



    st.plotly_chart(

        fig,

        use_container_width=True

    )





    st.divider()




    # --------------------------------
    # AI Rival Analysis
    # --------------------------------


    score_1 = (

        metrics_1["average_speed"]

        +

        metrics_1["throttle"]

    )



    score_2 = (

        metrics_2["average_speed"]

        +

        metrics_2["throttle"]

    )




    if score_1 > score_2:


        winner = driver_1


    else:


        winner = driver_2





    difference = round(

        abs(score_1-score_2),

        2

    )




    st.success(

        f"""

AI Driver Engineer Analysis



Performance Advantage:

**{winner}**



Performance Difference Score:

{difference}



Evaluation Factors:

- Average speed

- Maximum speed

- Throttle efficiency

- Braking behaviour

- Gear performance

- FastF1 telemetry data

"""

    )