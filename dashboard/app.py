import streamlit as st


from config.theme import get_theme


from components.header import render_header
from components.sidebar import render_sidebar

from components.race_status import render_race_status
from components.weather_analysis import render_weather_analysis
from components.race_incident_analysis import render_race_incident_analysis

from components.race_standings import render_race_standings
from components.championship_standings import render_championship_standings
from components.constructor_standings import render_constructor_standings

from components.qualifying_analysis import render_qualifying_analysis
from components.race_pace_analysis import render_race_pace_analysis
from components.tyre_degradation import render_tyre_degradation
from components.pit_stop_analysis import render_pit_stop_analysis

from components.driver_card import render_driver_card
from components.track_map import render_track_map
from components.race_control import render_race_control

from components.telemetry import render_telemetry
from components.lap_analysis import render_lap_analysis

from components.strategy import render_strategy
from components.tire_strategy import render_tire_strategy

from components.driver_comparison import render_driver_comparison

from components.prediction import render_prediction
from components.ai_engineer import render_ai_engineer


from data.drivers import DRIVERS
from data.session_mapping import SESSION_CODES



# --------------------------------
# Page Configuration
# --------------------------------

st.set_page_config(

    page_title="F1 AI Race Engineer",

    page_icon="F1",

    layout="wide"

)



# --------------------------------
# Theme
# --------------------------------

theme = get_theme()


st.markdown(

    f"""

<style>

.stApp {{

background-color:{theme['background']};

color:white;

}}

</style>

""",

    unsafe_allow_html=True

)



# --------------------------------
# Header
# --------------------------------

render_header()



# --------------------------------
# Sidebar
# --------------------------------

race_config = render_sidebar()



# --------------------------------
# Race Status
# --------------------------------

render_race_status(

    race_config

)


st.divider()



# --------------------------------
# FastF1 Weather Analysis
# --------------------------------

render_weather_analysis(

    race_config["year"],

    race_config["fastf1_name"]

)


st.divider()



# --------------------------------
# FastF1 Race Incident Analysis
# --------------------------------

render_race_incident_analysis(

    race_config["year"],

    race_config["fastf1_name"]

)


st.divider()



# --------------------------------
# FastF1 Race Driver Standings
# --------------------------------

render_race_standings(

    race_config["year"],

    race_config["fastf1_name"]

)


st.divider()



# --------------------------------
# Driver Championship Standings
# --------------------------------

render_championship_standings(

    race_config["year"]

)


st.divider()



# --------------------------------
# Constructor Championship Standings
# --------------------------------

render_constructor_standings(

    race_config["year"]

)


st.divider()



# --------------------------------
# FastF1 Qualifying Analysis
# --------------------------------

render_qualifying_analysis(

    race_config["year"],

    race_config["fastf1_name"]

)


st.divider()



# --------------------------------
# FastF1 Race Pace Analysis
# --------------------------------

render_race_pace_analysis(

    race_config["year"],

    race_config["fastf1_name"]

)


st.divider()



# --------------------------------
# FastF1 Tyre Degradation
# --------------------------------

render_tyre_degradation(

    race_config["year"],

    race_config["fastf1_name"]

)


st.divider()



# --------------------------------
# FastF1 Pit Stop Strategy
# --------------------------------

render_pit_stop_analysis(

    race_config["year"],

    race_config["fastf1_name"]

)


st.divider()



# --------------------------------
# Driver Information
# --------------------------------

selected_driver = race_config["driver"]


driver_data = DRIVERS.get(

    selected_driver

)



if driver_data is None:


    st.error(

        "Driver data unavailable"

    )

    st.stop()



driver_data = driver_data.copy()


driver_data["name"] = selected_driver



# --------------------------------
# Driver Intelligence
# --------------------------------

render_driver_card(

    driver_data

)


st.divider()



# --------------------------------
# Circuit Map
# --------------------------------

render_track_map(

    race_config["circuit"]

)


st.divider()



# --------------------------------
# Real FastF1 Race Control
# --------------------------------

render_race_control(

    race_config["year"],

    race_config["fastf1_name"],

    SESSION_CODES.get(

        race_config["session"],

        "Race"

    )

)


st.divider()



# --------------------------------
# FastF1 Telemetry
# --------------------------------

driver_code = driver_data["code"]


session_code = SESSION_CODES.get(

    race_config["session"],

    "R"

)



telemetry = render_telemetry(

    year=race_config["year"],

    event=race_config["fastf1_name"],

    session=session_code,

    driver=driver_code

)


st.divider()



# --------------------------------
# Lap Analysis
# --------------------------------

render_lap_analysis()


st.divider()



# --------------------------------
# AI Strategy
# --------------------------------

strategy = render_strategy(

    race_config["circuit"],

    race_config["session"],

    selected_driver

)


st.divider()



# --------------------------------
# AI Tire Strategy
# --------------------------------

render_tire_strategy(

    telemetry,

    race_config["circuit"],

    selected_driver

)


st.divider()



# --------------------------------
# AI Driver Comparison
# --------------------------------

render_driver_comparison(

    year=race_config["year"],

    event=race_config["fastf1_name"],

    session=session_code,

    selected_driver=selected_driver

)


st.divider()



# --------------------------------
# AI Prediction
# --------------------------------

prediction = render_prediction(

    telemetry,

    selected_driver,

    driver_data["constructor"]

)


st.divider()



# --------------------------------
# AI Engineer Assistant
# --------------------------------

render_ai_engineer(

    selected_driver,

    race_config["circuit"],

    race_config["session"],

    prediction,

    strategy

)