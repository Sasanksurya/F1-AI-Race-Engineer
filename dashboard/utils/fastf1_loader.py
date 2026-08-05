import fastf1
import streamlit as st



@st.cache_data

def load_fastf1_session(

    year,

    event,

    session

):


    fastf1.Cache.enable_cache(

        "fastf1_cache"

    )


    f1_session = fastf1.get_session(

        year,

        event,

        session

    )


    f1_session.load()


    return f1_session