import streamlit as st


from services.fastf1_service import (
    load_session,
    get_race_results
)



def render_championship_standings(

    year

):


    st.subheader(

        "🏆 Real F1 Championship Standings"

    )



    # --------------------------------
    # Load Season Races
    # --------------------------------


    races = [

        "Bahrain",

        "Saudi Arabia",

        "Australia",

        "Japan",

        "Miami",

        "Monaco",

        "Spain",

        "Canada",

        "Great Britain",

        "Austria",

        "Belgium",

        "Hungary",

        "Netherlands",

        "Italy",

        "Singapore",

        "USA",

        "Mexico",

        "Brazil",

        "Las Vegas",

        "Qatar",

        "Abu Dhabi"

    ]



    championship = {}



    # --------------------------------
    # Collect Race Results
    # --------------------------------


    progress = st.progress(0)



    for index, race in enumerate(races):


        session = load_session(

            year,

            race,

            "Race"

        )



        if session is not None:


            results = get_race_results(

                session

            )



            if results is not None:


                for _, driver in results.iterrows():


                    name = driver["Driver"]


                    if name not in championship:


                        championship[name] = {


                            "Team": driver["Team"],

                            "Points": 0,

                            "Wins": 0,

                            "Podiums": 0


                        }



                    championship[name]["Points"] += driver["Points"]



                    if driver["Position"] == 1:

                        championship[name]["Wins"] += 1



                    if driver["Position"] <= 3:

                        championship[name]["Podiums"] += 1



        progress.progress(

            (index + 1) / len(races)

        )



    progress.empty()



    if not championship:


        st.warning(

            "No championship data available"

        )

        return



    # --------------------------------
    # Sort Championship
    # --------------------------------


    standings = sorted(

        championship.items(),

        key=lambda x:x[1]["Points"],

        reverse=True

    )



    # --------------------------------
    # Display Table
    # --------------------------------


    table = []



    for position,(driver,data) in enumerate(

        standings,

        start=1

    ):


        table.append(

            {


                "Position": position,

                "Driver": driver,

                "Team": data["Team"],

                "Points": data["Points"],

                "Wins": data["Wins"],

                "Podiums": data["Podiums"]


            }

        )



    st.dataframe(

        table,

        use_container_width=True,

        hide_index=True

    )



    st.divider()



    # --------------------------------
    # Championship Leader
    # --------------------------------


    leader = standings[0]



    st.success(

        f"""

🏆 Championship Leader


Driver:

**{leader[0]}**


Team:

**{leader[1]['Team']}**


Points:

**{leader[1]['Points']}**

"""

    )