import streamlit as st
import pandas as pd
import plotly.graph_objects as go


from services.fastf1_service import load_session




# --------------------------------
# Weather Data Processing
# --------------------------------

def process_weather(session):


    try:


        weather = session.weather_data.copy()



        if weather.empty:

            return None



        weather = weather.fillna(0)



        latest = weather.iloc[-1]



        data = {


            "air_temperature":

            latest.get(

                "AirTemp",

                0

            ),



            "track_temperature":

            latest.get(

                "TrackTemp",

                0

            ),



            "humidity":

            latest.get(

                "Humidity",

                0

            ),



            "wind_speed":

            latest.get(

                "WindSpeed",

                0

            ),



            "rainfall":

            latest.get(

                "Rainfall",

                0

            ),



            "history":

            weather

        }



        return data



    except Exception:


        return None





# --------------------------------
# Weather Analysis Component
# --------------------------------

def render_weather_analysis(

    year,

    event

):


    st.subheader(

        "Real FastF1 Weather and Track Condition Analysis"

    )



    with st.spinner(

        "Loading FastF1 weather data..."

    ):


        session = load_session(

            year,

            event,

            "Race"

        )



    if session is None:


        st.warning(

            "Unable to load race session"

        )

        return




    weather = process_weather(

        session

    )



    if weather is None:


        st.warning(

            "No weather data available"

        )

        return




    st.markdown(

        f"""

Selected Race:

**{event}**

"""

    )



    st.divider()




    # --------------------------------
    # Weather Metrics
    # --------------------------------


    col1, col2, col3, col4 = st.columns(4)



    with col1:


        st.metric(

            "Track Temperature",

            f"{weather['track_temperature']:.1f} °C"

        )



    with col2:


        st.metric(

            "Air Temperature",

            f"{weather['air_temperature']:.1f} °C"

        )



    with col3:


        st.metric(

            "Humidity",

            f"{weather['humidity']:.1f}%"

        )



    with col4:


        st.metric(

            "Wind Speed",

            f"{weather['wind_speed']:.1f} m/s"

        )



    st.divider()




    # --------------------------------
    # Weather Status
    # --------------------------------


    rainfall = weather["rainfall"]



    if rainfall > 0:


        condition = "Rain detected"


    else:


        condition = "Dry conditions"




    col1, col2 = st.columns(2)



    with col1:


        if rainfall > 0:


            st.warning(

                f"""

Track Condition:

{condition}


Rainfall:

{rainfall}

"""

            )


        else:


            st.success(

                f"""

Track Condition:

{condition}


Rainfall:

No Rain

"""

            )




    with col2:


        temperature = weather["track_temperature"]



        if temperature > 40:


            message = (

                "High track temperature detected. "

                "Tyre degradation risk is increased."

            )


        elif temperature < 25:


            message = (

                "Cold track detected. "

                "Tyre warm-up may become difficult."

            )


        else:


            message = (

                "Normal track temperature conditions."

            )



        st.info(

            f"""

Track Analysis:


{message}

"""

        )



    st.divider()




    # --------------------------------
    # Weather Trend Chart
    # --------------------------------


    history = weather["history"]



    if "TrackTemp" in history.columns:


        fig = go.Figure()



        fig.add_trace(

            go.Scatter(

                x=history.index,

                y=history["TrackTemp"],

                mode="lines",

                name="Track Temperature"

            )

        )



        fig.update_layout(

            title="Track Temperature Trend",

            template="plotly_dark",

            height=350

        )



        st.plotly_chart(

            fig,

            use_container_width=True

        )



    st.divider()




    # --------------------------------
    # AI Weather Engineer
    # --------------------------------


    if rainfall > 0:


        recommendation = (

            "Rain detected. Prepare intermediate tyres "

            "and flexible pit strategy."

        )


    elif weather["track_temperature"] > 40:


        recommendation = (

            "High temperature conditions. "

            "Prioritize tyre management."

        )


    else:


        recommendation = (

            "Stable weather conditions. "

            "Standard race strategy recommended."

        )



    st.success(

        f"""

AI Weather Engineer Recommendation:


{recommendation}


Analysis factors:

- Track temperature

- Rain conditions

- Humidity

- Wind conditions

- Tyre degradation impact

"""

    )