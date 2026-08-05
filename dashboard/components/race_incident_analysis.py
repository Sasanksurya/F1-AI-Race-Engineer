import streamlit as st
import pandas as pd
import plotly.graph_objects as go


from services.fastf1_service import load_session



# --------------------------------
# Extract Race Incidents
# --------------------------------

def get_race_incidents(session):

    try:

        messages = session.race_control_messages

    except Exception:

        return []


    if messages is None or messages.empty:

        return []


    incidents = []


    for _, row in messages.iterrows():

        message = str(

            row.get(

                "Message",

                ""

            )

        )


        category = None



        if "SAFETY CAR" in message.upper():

            category = "Safety Car"



        elif "VIRTUAL SAFETY CAR" in message.upper():

            category = "Virtual Safety Car"



        elif "YELLOW" in message.upper():

            category = "Yellow Flag"



        elif "RED FLAG" in message.upper():

            category = "Red Flag"



        if category is None:

            continue



        incidents.append(

            {

                "lap": row.get(

                    "Lap",

                    0

                ),

                "type": category,

                "message": message

            }

        )


    return incidents





# --------------------------------
# Streamlit Component
# --------------------------------

def render_race_incident_analysis(

    year,

    event

):


    st.subheader(

        "Safety Car and Race Incident Analysis"

    )



    try:


        session = load_session(

            year,

            event,

            "R"

        )


    except Exception as e:


        st.warning(

            f"FastF1 session loading issue: {e}"

        )

        return



    if session is None:


        st.warning(

            "Unable to load race session"

        )

        return



    incidents = get_race_incidents(

        session

    )



    if not incidents:


        st.success(

            "No major race incidents detected for this race."

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
    # Incident Table
    # --------------------------------


    df = pd.DataFrame(

        incidents

    )



    df.rename(

        columns={

            "lap":"Lap",

            "type":"Event",

            "message":"Message"

        },

        inplace=True

    )



    st.dataframe(

        df,

        use_container_width=True,

        hide_index=True

    )



    st.divider()



    # --------------------------------
    # Incident Timeline
    # --------------------------------


    impact_values = []



    for item in incidents:


        if item["type"] == "Red Flag":


            impact_values.append(4)



        elif item["type"] == "Safety Car":


            impact_values.append(3)



        elif item["type"] == "Virtual Safety Car":


            impact_values.append(2)



        else:


            impact_values.append(1)



    fig = go.Figure()



    fig.add_trace(

        go.Scatter(

            x=[

                item["lap"]

                for item in incidents

            ],

            y=impact_values,

            mode="lines+markers",

            name="Incident Impact"

        )

    )



    fig.update_layout(

        title="Race Incident Timeline",

        xaxis_title="Lap",

        yaxis_title="Impact Level",

        template="plotly_dark",

        height=350

    )



    st.plotly_chart(

        fig,

        use_container_width=True

    )



    st.divider()



    # --------------------------------
    # AI Analysis
    # --------------------------------


    safety_car_count = sum(

        1

        for item in incidents

        if item["type"] == "Safety Car"

    )



    vsc_count = sum(

        1

        for item in incidents

        if item["type"] == "Virtual Safety Car"

    )



    red_flag_count = sum(

        1

        for item in incidents

        if item["type"] == "Red Flag"

    )



    if red_flag_count > 0:


        recommendation = (

            "Red flag detected. "

            "Aggressive restart strategy required."

        )



    elif safety_car_count > 0:


        recommendation = (

            "Safety Car detected. "

            "Flexible pit strategy recommended."

        )



    elif vsc_count > 0:


        recommendation = (

            "Virtual Safety Car detected. "

            "Monitor reduced pace opportunities."

        )



    else:


        recommendation = (

            "Low incident impact detected. "

            "Normal race strategy recommended."

        )



    st.success(

        f"""

AI Race Engineer Incident Analysis


{recommendation}



Safety Car Events:

{safety_car_count}



Virtual Safety Car Events:

{vsc_count}



Red Flag Events:

{red_flag_count}

"""

    )