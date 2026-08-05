import streamlit as st
import pandas as pd
import plotly.graph_objects as go


from services.fastf1_service import load_session




# --------------------------------
# Calculate Tyre Degradation
# --------------------------------

def calculate_degradation(session):


    laps = session.laps.copy()



    required_columns = [

        "LapTime",

        "Compound",

        "Driver",

        "Stint",

        "LapNumber"

    ]


    for col in required_columns:

        if col not in laps.columns:

            return []



    laps = laps.dropna(

        subset=[

            "LapTime",

            "Compound"

        ]

    )



    laps["LapSeconds"] = (

        laps["LapTime"]

        .dt.total_seconds()

    )



    results = session.results



    driver_info = {}



    for _, row in results.iterrows():

        driver_info[row["Abbreviation"]] = {

            "name": row["FullName"],

            "team": row["TeamName"]

        }




    degradation_data = []



    for driver in laps["Driver"].unique():



        driver_laps = laps[

            laps["Driver"]

            ==

            driver

        ]



        for stint in driver_laps["Stint"].dropna().unique():



            stint_laps = driver_laps[

                driver_laps["Stint"]

                ==

                stint

            ]



            if len(stint_laps) < 5:

                continue



            first_laps = stint_laps.head(5)

            last_laps = stint_laps.tail(5)



            first_average = (

                first_laps["LapSeconds"]

                .mean()

            )



            last_average = (

                last_laps["LapSeconds"]

                .mean()

            )



            stint_length = len(stint_laps)



            degradation = (

                last_average -

                first_average

            ) / stint_length



            degradation = round(

                degradation,

                3

            )



            tyre_score = max(

                100 -

                int(degradation * 100),

                0

            )



            degradation_data.append(

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



                    "compound":

                    stint_laps["Compound"]

                    .iloc[0],



                    "start_lap":

                    int(

                        stint_laps["LapNumber"]

                        .min()

                    ),



                    "end_lap":

                    int(

                        stint_laps["LapNumber"]

                        .max()

                    ),



                    "degradation":

                    degradation,



                    "tyre_score":

                    tyre_score

                }

            )



    return degradation_data





# --------------------------------
# Streamlit Component
# --------------------------------

def render_tyre_degradation(

    year,

    event

):


    st.subheader(

        "Real FastF1 Tyre Degradation Analysis"

    )



    with st.spinner(

        "Analyzing tyre performance..."

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



    results = calculate_degradation(

        session

    )



    if not results:


        st.warning(

            "No tyre degradation data available"

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


    dataframe = pd.DataFrame(

        results

    )



    display_df = dataframe.copy()



    display_df["Lap Range"] = (

        display_df["start_lap"]

        .astype(str)

        +

        " - "

        +

        display_df["end_lap"]

        .astype(str)

    )



    display_df["Degradation"] = (

        display_df["degradation"]

        .astype(str)

        +

        " sec/lap"

    )



    display_df = display_df[

        [

            "driver",

            "team",

            "compound",

            "Lap Range",

            "Degradation",

            "tyre_score"

        ]

    ]



    display_df.columns = [

        "Driver",

        "Team",

        "Compound",

        "Lap Range",

        "Degradation",

        "Tyre Score"

    ]



    st.dataframe(

        display_df,

        use_container_width=True,

        hide_index=True

    )



    st.divider()




    # --------------------------------
    # Degradation Chart
    # --------------------------------


    fig = go.Figure()



    fig.add_trace(

        go.Bar(

            x=dataframe["driver"],

            y=dataframe["degradation"],

            name="Tyre Degradation"

        )

    )



    fig.update_layout(

        title="Tyre Degradation Rate",

        yaxis_title="Seconds Lost Per Lap",

        template="plotly_dark",

        height=400

    )



    st.plotly_chart(

        fig,

        use_container_width=True

    )



    st.divider()




    # --------------------------------
    # AI Tyre Engineer
    # --------------------------------


    best = min(

        results,

        key=lambda x:x["degradation"]

    )



    st.success(

        f"""

AI Tyre Engineer Recommendation


Best tyre management:


Driver:

**{best['driver']}**


Team:

**{best['team']}**


Compound:

**{best['compound']}**


Degradation:

**{best['degradation']} sec/lap**


Tyre Score:

**{best['tyre_score']}/100**


Recommendation:

Maintain similar tyre management strategy.

"""

    )