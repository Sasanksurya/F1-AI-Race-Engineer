import streamlit as st


from data.drivers import DRIVERS



# --------------------------------
# FastF1 Race Configuration
# --------------------------------

RACE_CONFIG = {


    "Bahrain Grand Prix": {

        "country": "Bahrain",

        "circuit": "Bahrain International Circuit",

        "fastf1_name": "Bahrain"

    },


    "Saudi Arabian Grand Prix": {

        "country": "Saudi Arabia",

        "circuit": "Jeddah Corniche Circuit",

        "fastf1_name": "Saudi Arabian Grand Prix"

    },


    "Australian Grand Prix": {

        "country": "Australia",

        "circuit": "Albert Park Circuit",

        "fastf1_name": "Australian Grand Prix"

    },


    "Japanese Grand Prix": {

        "country": "Japan",

        "circuit": "Suzuka International Racing Course",

        "fastf1_name": "Japanese Grand Prix"

    },


    "Monaco Grand Prix": {

        "country": "Monaco",

        "circuit": "Circuit de Monaco",

        "fastf1_name": "Monaco Grand Prix"

    },


    "British Grand Prix": {

        "country": "United Kingdom",

        "circuit": "Silverstone Circuit",

        "fastf1_name": "British Grand Prix"

    },


    "Belgian Grand Prix": {

        "country": "Belgium",

        "circuit": "Circuit de Spa-Francorchamps",

        "fastf1_name": "Belgian Grand Prix"

    },


    "Italian Grand Prix": {

        "country": "Italy",

        "circuit": "Autodromo Nazionale Monza",

        "fastf1_name": "Italian Grand Prix"

    }

}





def render_sidebar():



    # --------------------------------
    # Sidebar Styling
    # --------------------------------


    st.sidebar.markdown(

        """

<style>


.sidebar-title {

color:#ff1e1e;

font-size:28px;

font-weight:900;

}


.sidebar-card {

background:#111111;

border:1px solid #ff1e1e;

border-radius:12px;

padding:15px;

margin-top:10px;

}


.sidebar-label {

color:#aaaaaa;

font-size:14px;

}


.sidebar-value {

color:white;

font-size:18px;

font-weight:bold;

}


</style>

        """,

        unsafe_allow_html=True

    )



    # --------------------------------
    # Header
    # --------------------------------


    st.sidebar.markdown(

        """

<div class="sidebar-title">

F1 COMMAND CENTER

</div>


<br>

Race Engineer Configuration

        """,

        unsafe_allow_html=True

    )



    st.sidebar.divider()



    # --------------------------------
    # Season
    # --------------------------------


    year = st.sidebar.selectbox(

        "Championship Season",

        [

            2024,

            2025,

            2026

        ]

    )



    # --------------------------------
    # Grand Prix
    # --------------------------------


    grand_prix = st.sidebar.selectbox(

        "Grand Prix",

        list(RACE_CONFIG.keys())

    )



    race_info = RACE_CONFIG[grand_prix]



    country = race_info["country"]

    circuit = race_info["circuit"]

    fastf1_name = race_info["fastf1_name"]



    # --------------------------------
    # Race Information Card
    # --------------------------------


    st.sidebar.markdown(

        f"""

<div class="sidebar-card">


<div class="sidebar-label">

Country

</div>


<div class="sidebar-value">

{country}

</div>


<br>


<div class="sidebar-label">

Circuit

</div>


<div class="sidebar-value">

{circuit}

</div>


</div>

        """,

        unsafe_allow_html=True

    )



    st.sidebar.divider()



    # --------------------------------
    # Session
    # --------------------------------


    session = st.sidebar.selectbox(

        "Race Session",

        [

            "Practice 1",

            "Practice 2",

            "Practice 3",

            "Qualifying",

            "Race"

        ]

    )



    st.sidebar.divider()



    # --------------------------------
    # Driver Selection
    # --------------------------------


    driver = st.sidebar.selectbox(

        "Driver",

        list(DRIVERS.keys())

    )



    driver_info = DRIVERS[driver]



    constructor = driver_info["constructor"]

    nationality = driver_info["nationality"]

    driver_country = driver_info["country"]



    # --------------------------------
    # Driver Card
    # --------------------------------


    st.sidebar.markdown(

        f"""

<div class="sidebar-card">


<div class="sidebar-label">

Selected Driver

</div>


<div class="sidebar-value">

{driver}

</div>



<br>


<div class="sidebar-label">

Constructor

</div>


<div class="sidebar-value">

{constructor}

</div>



<br>


<div class="sidebar-label">

Country

</div>


<div class="sidebar-value">

{driver_country}

</div>



<br>


<div class="sidebar-label">

Nationality

</div>


<div class="sidebar-value">

{nationality}

</div>


</div>

        """,

        unsafe_allow_html=True

    )



    st.sidebar.divider()



    # --------------------------------
    # System Status
    # --------------------------------


    st.sidebar.success(

        "FastF1 Telemetry System Connected"

    )


    st.sidebar.info(

        "AI Race Engineer Online"

    )



    return {


        "year": year,


        "grand_prix": grand_prix,


        "country": country,


        "circuit": circuit,


        "fastf1_name": fastf1_name,


        "driver": driver,


        "constructor": constructor,


        "nationality": nationality,


        "session": session

    }