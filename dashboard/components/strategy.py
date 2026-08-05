import streamlit as st


from services.strategy_service import generate_strategy



def render_strategy(

    circuit,

    session,

    driver

):


    st.subheader(

        "AI Race Strategy Engine"

    )



    strategy = generate_strategy(

        circuit,

        session,

        driver

    )



    tyre = strategy.get(

        "tyre",

        "Medium → Hard"

    )


    pit_window = strategy.get(

        "pit_window",

        "Lap 20 - 25"

    )


    reason = strategy.get(

        "reason",

        "Strategy generated from race conditions."

    )


    risk = strategy.get(

        "risk",

        "Medium"

    )


    confidence = strategy.get(

        "confidence",

        80

    )



    st.divider()



    # --------------------------------
    # Strategy Metrics
    # --------------------------------


    col1,col2,col3,col4 = st.columns(4)



    with col1:

        st.metric(

            "Recommended Tyre",

            tyre

        )



    with col2:

        st.metric(

            "Pit Window",

            pit_window

        )



    with col3:

        st.metric(

            "Risk Level",

            risk

        )



    with col4:

        st.metric(

            "AI Confidence",

            f"{confidence}%"

        )



    st.divider()



    # --------------------------------
    # Engineer Recommendation
    # --------------------------------


    st.markdown(

        f"""

## Race Engineer Recommendation


### Strategy

{tyre}


### Pit Window

{pit_window}


### Risk Assessment

{risk}


### Analysis

{reason}

"""

    )



    st.divider()



    # --------------------------------
    # Strategy Context
    # --------------------------------


    col1,col2 = st.columns(2)



    with col1:


        st.info(

            f"""

Driver

{driver}


Circuit

{circuit}


Session

{session}

"""

        )



    with col2:


        st.success(

            f"""

AI Strategy Factors


- Weather conditions

- Track temperature

- Tyre degradation

- Pit stop history

- Race incidents


Confidence:

{confidence}%

"""

        )



    st.divider()



    return strategy