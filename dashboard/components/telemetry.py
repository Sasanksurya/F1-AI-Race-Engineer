import streamlit as st
import plotly.graph_objects as go


from services.fastf1_service import (
    load_session,
    get_driver_telemetry
)



def render_telemetry(

    year,

    event,

    session,

    driver

):


    st.subheader(

        "Real FastF1 Telemetry"

    )



    # --------------------------------
    # Load FastF1 Session
    # --------------------------------

    try:


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

            return None



    except Exception as e:


        st.error(

            f"FastF1 loading error: {e}"

        )

        return None





    # --------------------------------
    # Driver Telemetry
    # --------------------------------


    telemetry = get_driver_telemetry(

        f1_session,

        driver

    )



    if telemetry is None or telemetry.empty:


        st.warning(

            f"No telemetry available for {driver}"

        )

        return None





    # --------------------------------
    # Telemetry Calculations
    # --------------------------------


    max_speed = telemetry["Speed"].max()


    avg_speed = telemetry["Speed"].mean()



    max_rpm = (

        telemetry["RPM"].max()

        if "RPM" in telemetry.columns

        else 0

    )



    max_gear = (

        telemetry["nGear"].max()

        if "nGear" in telemetry.columns

        else 0

    )



    drs_status = "N/A"



    if "DRS" in telemetry.columns:


        drs_status = (

            "OPEN"

            if telemetry["DRS"].max() > 0

            else

            "CLOSED"

        )





    # --------------------------------
    # Telemetry Metrics
    # --------------------------------


    col1,col2,col3,col4,col5 = st.columns(5)



    with col1:


        st.metric(

            "Top Speed",

            f"{max_speed:.0f} km/h"

        )



    with col2:


        st.metric(

            "Average Speed",

            f"{avg_speed:.0f} km/h"

        )



    with col3:


        st.metric(

            "Max RPM",

            f"{max_rpm:.0f}"

        )



    with col4:


        st.metric(

            "Highest Gear",

            int(max_gear)

        )



    with col5:


        st.metric(

            "DRS",

            drs_status

        )



    st.divider()





    # --------------------------------
    # Speed Analysis
    # --------------------------------


    if "Distance" in telemetry.columns:


        speed_fig = go.Figure()



        speed_fig.add_trace(

            go.Scatter(

                x=telemetry["Distance"],

                y=telemetry["Speed"],

                mode="lines",

                name="Speed"

            )

        )



        speed_fig.update_layout(

            title="Speed Performance Trace",

            template="plotly_dark",

            height=400,

            xaxis_title="Distance (m)",

            yaxis_title="Speed km/h"

        )



        st.plotly_chart(

            speed_fig,

            use_container_width=True

        )





    # --------------------------------
    # RPM Analysis
    # --------------------------------


    if (

        "RPM" in telemetry.columns

        and

        "Distance" in telemetry.columns

    ):


        rpm_fig = go.Figure()



        rpm_fig.add_trace(

            go.Scatter(

                x=telemetry["Distance"],

                y=telemetry["RPM"],

                mode="lines",

                name="RPM"

            )

        )



        rpm_fig.update_layout(

            title="Engine RPM Analysis",

            template="plotly_dark",

            height=350

        )



        st.plotly_chart(

            rpm_fig,

            use_container_width=True

        )





    # --------------------------------
    # Driver Control Analysis
    # --------------------------------


    if "Distance" in telemetry.columns:


        control_fig = go.Figure()



        if "Throttle" in telemetry.columns:


            control_fig.add_trace(

                go.Scatter(

                    x=telemetry["Distance"],

                    y=telemetry["Throttle"],

                    mode="lines",

                    name="Throttle"

                )

            )



        if "Brake" in telemetry.columns:


            control_fig.add_trace(

                go.Scatter(

                    x=telemetry["Distance"],

                    y=telemetry["Brake"],

                    mode="lines",

                    name="Brake"

                )

            )



        control_fig.update_layout(

            title="Throttle and Brake Analysis",

            template="plotly_dark",

            height=400

        )



        st.plotly_chart(

            control_fig,

            use_container_width=True

        )





    # --------------------------------
    # Return Telemetry
    # --------------------------------


    return telemetry