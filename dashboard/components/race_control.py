import streamlit as st


from services.fastf1_service import load_session




def analyze_race_control(session):


    data = {


        "safety_car":0,

        "virtual_safety_car":0,

        "yellow_flag":0,

        "red_flag":0

    }



    try:


        messages = session.race_control_messages



        if messages is None or messages.empty:

            return data



        for _, row in messages.iterrows():


            message = str(

                row.get(

                    "Message",

                    ""

                )

            ).upper()



            if "SAFETY CAR" in message:

                data["safety_car"] += 1



            elif "VIRTUAL SAFETY CAR" in message:

                data["virtual_safety_car"] += 1



            elif "YELLOW" in message:

                data["yellow_flag"] += 1



            elif "RED FLAG" in message:

                data["red_flag"] += 1



    except Exception:


        pass



    return data





def render_race_control(

    year,

    event,

    session_type

):


    st.subheader(

        "Real FastF1 Race Control Dashboard"

    )



    session = load_session(

        year,

        event,

        session_type

    )



    if session is None:


        st.warning(

            "Race control data unavailable"

        )

        return



    incidents = analyze_race_control(

        session

    )



    st.markdown(

        f"""

Selected Event:

**{event}**


Session:

**{session_type}**

"""

    )


    st.divider()



    # --------------------------------
    # Race Control Metrics
    # --------------------------------


    col1,col2,col3,col4 = st.columns(4)



    with col1:


        st.metric(

            "Safety Cars",

            incidents["safety_car"]

        )



    with col2:


        st.metric(

            "Virtual Safety Cars",

            incidents["virtual_safety_car"]

        )



    with col3:


        st.metric(

            "Yellow Flags",

            incidents["yellow_flag"]

        )



    with col4:


        st.metric(

            "Red Flags",

            incidents["red_flag"]

        )



    st.divider()



    # --------------------------------
    # Race Impact Analysis
    # --------------------------------


    total_incidents = sum(

        incidents.values()

    )



    if incidents["red_flag"] > 0:


        message = (

            "Major disruption detected. "

            "Restart strategy required."

        )


    elif incidents["safety_car"] > 0:


        message = (

            "Safety Car deployment detected. "

            "Pit strategy opportunities created."

        )


    elif incidents["virtual_safety_car"] > 0:


        message = (

            "Virtual Safety Car detected. "

            "Teams should monitor pace changes."

        )


    else:


        message = (

            "No major race control events detected."

        )



    st.success(

        f"""

AI Race Control Analysis:


{message}



Total Race Control Events:

{total_incidents}

"""

    )