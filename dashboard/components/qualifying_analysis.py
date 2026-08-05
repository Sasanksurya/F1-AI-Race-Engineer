import streamlit as st
import pandas as pd


from services.fastf1_service import load_session



def render_qualifying_analysis(

    year,

    race_name

):


    st.subheader(

        "Real FastF1 Qualifying Analysis"

    )



    # --------------------------------
    # Load Qualifying Session
    # --------------------------------

    with st.spinner(

        "Loading qualifying data..."

    ):


        session = load_session(

            year,

            race_name,

            "Qualifying"

        )



    if session is None:


        st.warning(

            "Qualifying session unavailable"

        )

        return




    try:


        results = session.results



        if results.empty:


            st.warning(

                "No qualifying results found"

            )

            return



    except Exception as e:


        st.error(

            f"Qualifying data error: {e}"

        )

        return




    # --------------------------------
    # Prepare Qualifying Data
    # --------------------------------


    table = []



    for _, driver in results.iterrows():


        position = driver.get(

            "Position",

            99

        )



        if pd.isna(position):

            position = 99



        lap_time = "N/A"



        try:


            abbreviation = driver.get(

                "Abbreviation",

                None

            )



            if abbreviation:


                laps = session.laps.pick_drivers(

                    abbreviation

                )


                if not laps.empty:


                    fastest = laps.pick_fastest()



                    if fastest is not None:


                        lap_time = str(

                            fastest["LapTime"]

                        )



        except Exception:


            lap_time = "N/A"




        table.append(

            {


                "Position":

                int(position),



                "Driver":

                driver.get(

                    "FullName",

                    "Unknown"

                ),



                "Team":

                driver.get(

                    "TeamName",

                    "Unknown"

                ),



                "Lap Time":

                lap_time


            }

        )




    table = sorted(

        table,

        key=lambda x:x["Position"]

    )



    if not table:


        st.warning(

            "No qualifying information available"

        )

        return




    # --------------------------------
    # Pole Position
    # --------------------------------


    pole = table[0]



    st.success(

        f"""

Pole Position


Driver:

**{pole['Driver']}**


Team:

**{pole['Team']}**


Lap Time:

**{pole['Lap Time']}**

"""

    )



    st.divider()




    # --------------------------------
    # Qualifying Table
    # --------------------------------


    dataframe = pd.DataFrame(

        table

    )



    st.dataframe(

        dataframe,

        use_container_width=True,

        hide_index=True

    )



    st.divider()



    # --------------------------------
    # Qualifying Pace Chart
    # --------------------------------


    chart_data = dataframe.head(10)



    st.bar_chart(

        chart_data.set_index(

            "Driver"

        )["Position"]

    )