import fastf1
import pandas as pd
import streamlit as st
import os



# --------------------------------
# FastF1 Cache Setup
# --------------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


CACHE_DIR = os.path.join(
    BASE_DIR,
    "fastf1_cache"
)


os.makedirs(
    CACHE_DIR,
    exist_ok=True
)


fastf1.Cache.enable_cache(
    CACHE_DIR
)



# --------------------------------
# Load F1 Session
# --------------------------------

@st.cache_resource(show_spinner=False)
def load_session(
    year,
    event,
    session_type
):

    try:

        session = fastf1.get_session(
            year,
            event,
            session_type
        )


        session.load(

            laps=True,

            telemetry=True,

            weather=True,

            messages=True,

            car_data=True,

            position_data=True

        )


        return session



    except Exception as e:


        st.error(

            f"FastF1 session loading failed: {e}"

        )


        return None





# --------------------------------
# Race Results
# --------------------------------

def get_race_results(session):


    try:


        if session is None:

            return None



        results = session.results



        if results.empty:

            return None



        columns = [

            "FullName",

            "TeamName",

            "Position",

            "Points"

        ]



        available = [

            col

            for col in columns

            if col in results.columns

        ]



        data = results[available].copy()



        data.rename(

            columns={

                "FullName":"Driver",

                "TeamName":"Team",

                "Position":"Position",

                "Points":"Points"

            },

            inplace=True

        )



        if "Position" in data.columns:


            data["Position"] = (

                data["Position"]

                .fillna(99)

                .astype(int)

            )


            data.sort_values(

                "Position",

                inplace=True

            )


        return data.reset_index(drop=True)



    except Exception as e:


        st.warning(

            f"Race result error: {e}"

        )


        return None





# --------------------------------
# Driver Laps
# --------------------------------

def get_driver_laps(

    session,

    driver

):


    try:


        if session is None:

            return None



        laps = session.laps



        driver_laps = laps.pick_drivers(

            driver

        )


        return driver_laps



    except Exception as e:


        st.warning(

            f"Lap extraction failed: {e}"

        )


        return None





# --------------------------------
# Driver Telemetry
# --------------------------------

def get_driver_telemetry(

    session,

    driver

):


    try:


        if session is None:

            return None



        laps = session.laps



        driver_laps = laps.pick_drivers(

            driver

        )



        if driver_laps.empty:

            return None



        fastest_lap = driver_laps.pick_fastest()



        telemetry = fastest_lap.get_telemetry()



        if telemetry.empty:

            return None



        return telemetry



    except Exception as e:


        st.warning(

            f"Telemetry extraction failed: {e}"

        )


        return None





# --------------------------------
# Tyre Strategy
# --------------------------------

def get_tyre_strategy(

    session,

    driver

):


    try:


        if session is None:

            return None



        laps = session.laps.pick_drivers(

            driver

        )



        if laps.empty:

            return None



        stints = laps.groupby(

            "Stint"

        ).agg(

            {

                "Compound":"first",

                "LapNumber":[

                    "min",

                    "max"

                ]

            }

        )



        stints.columns = [

            "Compound",

            "Start Lap",

            "End Lap"

        ]



        return stints.reset_index()



    except Exception as e:


        st.warning(

            f"Tyre strategy failed: {e}"

        )


        return None





# --------------------------------
# Weather Data
# --------------------------------

def get_weather(session):


    try:


        if session is None:

            return None



        return session.weather_data



    except Exception:


        return None





# --------------------------------
# Race Control Messages
# --------------------------------

def get_race_control_messages(session):


    try:


        if session is None:

            return None



        return session.race_control_messages



    except Exception:


        return None





# --------------------------------
# Session Information
# --------------------------------

def get_session_info(session):


    try:


        if session is None:

            return None



        return {


            "Event":

            session.event.EventName,


            "Country":

            session.event.Country,


            "Location":

            session.event.Location,


            "Year":

            session.event.year


        }



    except Exception:


        return None