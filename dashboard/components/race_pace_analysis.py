import streamlit as st
import pandas as pd
import plotly.graph_objects as go


from services.fastf1_service import load_session



# ---------------------------------------------
# Convert seconds to lap format
# ---------------------------------------------

def convert_time(seconds):

    if pd.isna(seconds):

        return "N/A"


    minutes = int(seconds // 60)

    sec = seconds % 60


    return f"{minutes}:{sec:06.3f}"




# ---------------------------------------------
# Calculate Race Pace
# ---------------------------------------------

def calculate_race_pace(session):


    laps = session.laps.copy()



    laps = laps.dropna(

        subset=[

            "LapTime",

            "Driver"

        ]

    )



    laps["LapSeconds"] = (

        laps["LapTime"]

        .dt.total_seconds()

    )



    results = session.results



    driver_names = {}

    teams = {}



    for _, row in results.iterrows():

        driver_names[row["Abbreviation"]] = row["FullName"]

        teams[row["Abbreviation"]] = row["TeamName"]




    drivers = []



    for driver in laps["Driver"].unique():


        driver_laps = laps[

            laps["Driver"]

            ==

            driver

        ]



        # Remove pit laps

        if "PitInTime" in driver_laps.columns:

            driver_laps = driver_laps[

                driver_laps["PitInTime"].isna()

            ]



        if len(driver_laps) < 5:

            continue




        average_lap = (

            driver_laps["LapSeconds"]

            .mean()

        )



        fastest_lap = (

            driver_laps["LapSeconds"]

            .min()

        )



        consistency = (

            driver_laps["LapSeconds"]

            .std()

        )



        consistency_score = max(

            100 - int(consistency * 20),

            0

        )



        pace_score = max(

            100 -

            int(

                (average_lap - fastest_lap)

                * 15

            ),

            0

        )



        overall_score = int(

            (

                pace_score +

                consistency_score

            )

            /

            2

        )



        drivers.append(

            {


                "driver":

                driver_names.get(

                    driver,

                    driver

                ),


                "team":

                teams.get(

                    driver,

                    "Unknown"

                ),


                "average_lap":

                average_lap,


                "fastest_lap":

                fastest_lap,


                "pace_score":

                pace_score,


                "consistency":

                consistency_score,


                "overall":

                overall_score


            }

        )



    return sorted(

        drivers,

        key=lambda x:x["overall"],

        reverse=True

    )




# ---------------------------------------------
# Streamlit Component
# ---------------------------------------------

def render_race_pace_analysis(

    year,

    event

):


    st.subheader(

        "Real FastF1 Race Pace Analysis"

    )



    with st.spinner(

        "Analyzing race pace..."

    ):


        session = load_session(

            year,

            event,

            "Race"

        )



    if session is None:


        st.warning(

            "Race session unavailable"

        )

        return




    results = calculate_race_pace(

        session

    )



    if not results:


        st.warning(

            "No race pace data available"

        )

        return




    st.markdown(

        f"""

Selected Race:

**{event}**

"""

    )



    st.divider()



    table = []



    for driver in results:


        table.append(

            {


            "Driver":

            driver["driver"],


            "Team":

            driver["team"],


            "Average Lap":

            convert_time(

                driver["average_lap"]

            ),


            "Fastest Lap":

            convert_time(

                driver["fastest_lap"]

            ),


            "Pace Score":

            driver["pace_score"],


            "Consistency":

            f'{driver["consistency"]}%',


            "Overall Score":

            driver["overall"]


            }

        )



    df = pd.DataFrame(table)



    st.dataframe(

        df,

        use_container_width=True,

        hide_index=True

    )



    st.divider()



    fig = go.Figure()



    fig.add_trace(

        go.Bar(

            x=df["Driver"],

            y=df["Overall Score"],

            name="Performance Score"

        )

    )



    fig.update_layout(

        title="AI Race Pace Performance Ranking",

        template="plotly_dark",

        height=400

    )



    st.plotly_chart(

        fig,

        use_container_width=True

    )



    st.divider()



    best = results[0]



    st.success(

        f"""

AI Race Engineer Analysis


Best Race Pace Driver:

**{best['driver']}**


Team:

**{best['team']}**


Performance Score:

**{best['overall']}/100**


The ranking considers:

- Average race pace

- Fastest lap capability

- Lap consistency

- Long run performance


"""

    )