import streamlit as st


from services.fastf1_service import (
    load_session,
    get_race_results
)



def render_constructor_standings(

    year

):


    st.subheader(

        "🏎️ Real F1 Constructor Championship Standings"

    )



    # --------------------------------
    # Season Races
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



    constructors = {}



    progress = st.progress(0)



    # --------------------------------
    # Collect Constructor Results
    # --------------------------------


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


                    team = driver["Team"]



                    if team not in constructors:


                        constructors[team] = {


                            "Points": 0,

                            "Wins": 0,

                            "Podiums": 0


                        }



                    constructors[team]["Points"] += driver["Points"]



                    if driver["Position"] == 1:


                        constructors[team]["Wins"] += 1



                    if driver["Position"] <= 3:


                        constructors[team]["Podiums"] += 1



        progress.progress(

            (index + 1) / len(races)

        )



    progress.empty()



    if not constructors:


        st.warning(

            "No constructor championship data available"

        )

        return



    # --------------------------------
    # Sort Constructors
    # --------------------------------


    standings = sorted(

        constructors.items(),

        key=lambda x:x[1]["Points"],

        reverse=True

    )



    # --------------------------------
    # Display Table
    # --------------------------------


    table = []



    for position,(team,data) in enumerate(

        standings,

        start=1

    ):


        table.append(

            {


                "Position": position,

                "Constructor": team,

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

🏆 Constructor Championship Leader


Team:

**{leader[0]}**


Points:

**{leader[1]['Points']}**


Wins:

**{leader[1]['Wins']}**

"""

    )