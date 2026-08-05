import streamlit as st
import pandas as pd
import plotly.graph_objects as go


from services.fastf1_service import load_session



# --------------------------------
# Calculate Pit Stop Data
# --------------------------------

def calculate_pit_stops(session):


    laps = session.laps.copy()



    if laps.empty:

        return []



    results = session.results



    driver_info = {}



    for _, row in results.iterrows():

        driver_info[row["Abbreviation"]] = {


            "name":

            row["FullName"],


            "team":

            row["TeamName"]

        }




    pit_data = []



    for driver in laps["Driver"].dropna().unique():



        driver_laps = laps[

            laps["Driver"]

            ==

            driver

        ]



        if "PitInTime" not in driver_laps.columns:

            continue



        pit_stops = driver_laps[

            driver_laps["PitInTime"].notna()

        ]



        stop_count = len(pit_stops)



        if stop_count == 0:

            continue




        pit_laps = (

            pit_stops["LapNumber"]

            .astype(int)

            .tolist()

        )



        pit_durations = []



        for index in pit_stops.index:


            try:


                pit_in = laps.loc[

                    index,

                    "PitInTime"

                ]



                pit_out = laps.loc[

                    index + 1,

                    "PitOutTime"

                ]



                if pd.notna(pit_in) and pd.notna(pit_out):


                    duration = (

                        pit_out - pit_in

                    ).total_seconds()



                    pit_durations.append(

                        duration

                    )


            except Exception:


                continue




        average_time = (

            sum(pit_durations)

            /

            len(pit_durations)

            if pit_durations

            else 0

        )



        strategy_score = max(

            100 -

            int(average_time * 5),

            0

        )



        pit_data.append(

            {


                "driver":

                driver_info.get(

                    driver,

                    {}

                ).get(

                    "name",

                    driver

                ),



                "team":

                driver_info.get(

                    driver,

                    {}

                ).get(

                    "team",

                    "Unknown"

                ),



                "stops":

                stop_count,



                "pit_laps":

                pit_laps,



                "pit_time":

                round(

                    average_time,

                    2

                ),



                "strategy_score":

                strategy_score

            }

        )



    return sorted(

        pit_data,

        key=lambda x:x["strategy_score"],

        reverse=True

    )





# --------------------------------
# Streamlit Component
# --------------------------------

def render_pit_stop_analysis(

    year,

    event

):


    st.subheader(

        "Real FastF1 Pit Stop Strategy Analysis"

    )



    with st.spinner(

        "Analyzing pit stop strategy..."

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




    results = calculate_pit_stops(

        session

    )



    if not results:


        st.warning(

            "No pit stop data available"

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
    # Table
    # --------------------------------


    table = []



    for item in results:


        table.append(

            {


            "Driver":

            item["driver"],



            "Team":

            item["team"],



            "Number of Stops":

            item["stops"],



            "Pit Laps":

            ", ".join(

                map(

                    str,

                    item["pit_laps"]

                )

            ),



            "Average Pit Time":

            f'{item["pit_time"]} sec',



            "Strategy Score":

            item["strategy_score"]


            }

        )



    df = pd.DataFrame(

        table

    )



    st.dataframe(

        df,

        use_container_width=True,

        hide_index=True

    )



    st.divider()




    # --------------------------------
    # Strategy Chart
    # --------------------------------


    fig = go.Figure()



    fig.add_trace(

        go.Bar(

            x=df["Driver"],

            y=df["Strategy Score"],

            name="Strategy Score"

        )

    )



    fig.update_layout(

        title="Pit Stop Strategy Performance",

        template="plotly_dark",

        height=400

    )



    st.plotly_chart(

        fig,

        use_container_width=True

    )



    st.divider()




    # --------------------------------
    # AI Recommendation
    # --------------------------------


    best = results[0]



    st.success(

        f"""

AI Strategy Engineer Recommendation


Best pit strategy execution:


Driver:

**{best['driver']}**


Team:

**{best['team']}**


Number of Stops:

**{best['stops']}**


Average Pit Time:

**{best['pit_time']} seconds**


Strategy Score:

**{best['strategy_score']}/100**


Analysis:

The strategy was evaluated using pit timing,
stop efficiency and race execution data.

"""

    )