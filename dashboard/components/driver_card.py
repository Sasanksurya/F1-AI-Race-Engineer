import streamlit as st
import os



def render_driver_card(driver_data):


    # --------------------------------
    # CSS Styling
    # --------------------------------


    st.markdown(

        """

<style>


.driver-wrapper {


    background:

    linear-gradient(

        135deg,

        #101010,

        #1c1c1c

    );


    border-radius:18px;


    padding:25px;


    margin-top:20px;


}



.driver-name {


    color:white;


    font-size:38px;


    font-weight:900;


}



.driver-team {


    color:#ff1e1e;


    font-size:22px;


    font-weight:700;


}



.driver-info {


    color:#bdbdbd;


    font-size:16px;


}



.image-box {


    height:260px;


    width:220px;


    border-radius:12px;


    border:1px solid #333;


    display:flex;


    align-items:center;


    justify-content:center;


    color:#888;


}



.logo-box {


    height:140px;


    width:140px;


    border-radius:12px;


    border:1px solid #333;


    display:flex;


    align-items:center;


    justify-content:center;


    color:#888;


}



.stat-card {


    background:#151515;


    border-radius:12px;


    padding:18px;


    text-align:center;


    border:1px solid #333;


}



.stat-title {


    color:#888;


    font-size:14px;


}



.stat-value {


    color:white;


    font-size:28px;


    font-weight:700;


}



</style>

        """,

        unsafe_allow_html=True

    )



    st.subheader(

        "Driver Intelligence Center"

    )



    # --------------------------------
    # Driver Data
    # --------------------------------


    name = driver_data["name"]

    team = driver_data["team"]

    nationality = driver_data["nationality"]

    country = driver_data["country"]

    constructor = driver_data["constructor"]


    image = driver_data.get(

        "image",

        None

    )


    logo = driver_data.get(

        "logo",

        None

    )



    # --------------------------------
    # Asset Paths
    # --------------------------------


    base_path = os.path.dirname(

        os.path.dirname(

            __file__

        )

    )


    image_path = None

    logo_path = None



    if image:

        temp_path = os.path.join(

            base_path,

            image

        )


        if os.path.isfile(temp_path):

            image_path = temp_path



    if logo:

        temp_path = os.path.join(

            base_path,

            logo

        )


        if os.path.isfile(temp_path):

            logo_path = temp_path



    # --------------------------------
    # Performance Rating
    # --------------------------------


    rating = min(

        100,

        int(

            (

                driver_data["points"] / 6

                +

                driver_data["wins"] / 2

                +

                driver_data["podiums"] / 5

            )

        )

    )



    # --------------------------------
    # Driver Profile
    # --------------------------------


    col1,col2,col3 = st.columns(

        [1.5,3,1.2]

    )



    # Driver Image

    with col1:


        if image_path:


            try:


                st.image(

                    image_path,

                    width=260

                )


            except Exception:


                st.markdown(

                    """

<div class="image-box">

Driver Image

</div>

                    """,

                    unsafe_allow_html=True

                )


        else:


            st.markdown(

                """

<div class="image-box">

Driver Image

</div>

                """,

                unsafe_allow_html=True

            )



    # Driver Information

    with col2:


        st.markdown(

            f"""

<div class="driver-wrapper">


<div class="driver-name">

{name}

</div>


<br>


<div class="driver-team">

{team}

</div>


<br>


<div class="driver-info">

Country:

{country}

</div>


<br>


<div class="driver-info">

Nationality:

{nationality}

</div>


<br>


<div class="driver-info">

Constructor:

{constructor}

</div>


</div>

            """,

            unsafe_allow_html=True

        )



    # Team Logo

    with col3:


        if logo_path:


            try:


                st.image(

                    logo_path,

                    width=140

                )


            except Exception:


                st.markdown(

                    """

<div class="logo-box">

Team Logo

</div>

                    """,

                    unsafe_allow_html=True

                )


        else:


            st.markdown(

                """

<div class="logo-box">

Team Logo

</div>

                """,

                unsafe_allow_html=True

            )



    st.divider()



    # --------------------------------
    # Championship Statistics
    # --------------------------------


    col1,col2,col3,col4 = st.columns(4)



    metrics = [


        (

            "Championship Position",

            f"P{driver_data['position']}"

        ),


        (

            "Points",

            driver_data["points"]

        ),


        (

            "Wins",

            driver_data["wins"]

        ),


        (

            "Podiums",

            driver_data["podiums"]

        )

    ]



    for col,item in zip(

        [col1,col2,col3,col4],

        metrics

    ):


        with col:


            st.markdown(

                f"""

<div class="stat-card">


<div class="stat-title">

{item[0]}

</div>


<br>


<div class="stat-value">

{item[1]}

</div>


</div>

                """,

                unsafe_allow_html=True

            )



    st.divider()



    # --------------------------------
    # Additional Performance
    # --------------------------------


    col1,col2 = st.columns(2)



    with col1:


        st.info(

            f"""

AI Performance Rating


{rating}/100



Pole Positions:

{driver_data["poles"]}



Fastest Laps:

{driver_data["fastest_laps"]}

"""

        )



    with col2:


        st.success(

            """

Driver Analysis Active


Data Sources:


- Driver statistics

- Championship performance

- Race history

- Constructor data

"""

        )