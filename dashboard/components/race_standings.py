import streamlit as st


from services.fastf1_service import (
    load_session,
    get_race_results
)



def render_race_standings(

    year,

    race_name

):


    st.subheader(

        "Real Race Driver Standings"

    )



    # --------------------------------
    # Load FastF1 Race Session
    # --------------------------------

    with st.spinner(

        "Loading real F1 race results..."

    ):


        session = load_session(

            year,

            race_name,

            "Race"

        )



    if session is None:


        st.warning(

            f"Race data unavailable for {race_name}"

        )

        return



    # --------------------------------
    # Get Results
    # --------------------------------

    results = get_race_results(

        session

    )



    if results is None or results.empty:


        st.warning(

            "No race results found"

        )

        return



    # --------------------------------
    # Data Cleaning
    # --------------------------------


    if "Position" in results.columns:


        results["Position"] = (

            results["Position"]

            .fillna(99)

            .astype(int)

        )



        results = results.sort_values(

            by="Position",

            ascending=True

        )



    results = results.reset_index(

        drop=True

    )



    # --------------------------------
    # Race Information
    # --------------------------------


    st.markdown(

        f"""

Selected Race:

### {race_name}

"""

    )


    st.divider()



    # --------------------------------
    # Results Table
    # --------------------------------


    st.dataframe(

        results,

        use_container_width=True,

        hide_index=True

    )



    st.divider()



    # --------------------------------
    # Winner Analysis
    # --------------------------------


    winner = results.iloc[0]



    st.success(

        f"""

Race Winner


Driver:

**{winner['Driver']}**


Team:

**{winner['Team']}**


Points:

**{winner['Points']}**

"""

    )