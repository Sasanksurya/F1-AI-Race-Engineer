import fastf1
import pandas as pd


fastf1.Cache.enable_cache(
    "fastf1_cache"
)



def load_session(year, event, session_type):


    session = fastf1.get_session(
        year,
        event,
        session_type
    )


    session.load()


    return session



def get_driver_list(session):


    drivers = session.results["FullName"].tolist()


    return drivers



def get_laps(session, driver):


    laps = session.laps.pick_driver(driver)


    return laps



def get_telemetry(session, driver):


    laps = session.laps.pick_driver(driver)


    telemetry = laps.get_telemetry()


    return telemetry