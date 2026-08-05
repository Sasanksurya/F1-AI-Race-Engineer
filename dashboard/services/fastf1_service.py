import fastf1
import pandas as pd
import streamlit as st
import os



# =====================================
# FastF1 Cache Configuration
# =====================================

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



# =====================================
# Load FastF1 Session
# =====================================

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


        # Correct FastF1 loading
        session.load()


        return session



    except Exception as e:


        st.error(
            f"FastF1 session loading failed: {e}"
        )


        return None





# =====================================
# Race Results
# =====================================

def get_race_results(session):

    try:

        if session is None:
            return None


        results = session.results


        if results is None or results.empty:
            return None



        columns = [

            "FullName",

            "TeamName",

            "Position",

            "Points"

        ]



        available_columns = [

            col

            for col in columns

            if col in results.columns

        ]



        data = results[available_columns].copy()



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

                pd.to_numeric(

                    data["Position"],

                    errors="coerce"

                )

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





# =====================================
# Driver Laps
# =====================================

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



        if driver_laps.empty:
            return None



        return driver_laps



    except Exception as e:


        st.warning(
            f"Lap extraction failed: {e}"
        )


        return None





# =====================================
# Driver Telemetry
# =====================================

def get_driver_telemetry(

    session,

    driver

):

    try:


        driver_laps = get_driver_laps(

            session,

            driver

        )



        if driver_laps is None:

            return None



        fastest_lap = driver_laps.pick_fastest()



        if fastest_lap is None:

            return None



        telemetry = fastest_lap.get_telemetry()



        if telemetry is None or telemetry.empty:

            return None



        return telemetry



    except Exception as e:


        st.warning(

            f"Telemetry extraction failed: {e}"

        )


        return None





# =====================================
# Tyre Strategy
# =====================================

def get_tyre_strategy(

    session,

    driver

):

    try:


        laps = get_driver_laps(

            session,

            driver

        )



        if laps is None:

            return None



        if "Compound" not in laps.columns:

            return None



        strategy = (

            laps.groupby("Stint")

            .agg(

                {

                    "Compound":"first",

                    "LapNumber":[

                        "min",

                        "max"

                    ]

                }

            )

        )



        strategy.columns = [

            "Compound",

            "Start Lap",

            "End Lap"

        ]



        return strategy.reset_index()



    except Exception as e:


        st.warning(

            f"Tyre strategy failed: {e}"

        )


        return None





# =====================================
# Weather Data
# =====================================

def get_weather(session):

    try:

        if session is None:
            return None



        return session.weather_data



    except Exception:


        return None





# =====================================
# Race Control Messages
# =====================================

def get_race_control_messages(session):

    try:

        if session is None:
            return None



        return session.race_control_messages



    except Exception:


        return None





# =====================================
# Session Information
# =====================================

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