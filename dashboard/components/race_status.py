import streamlit as st


def render_race_status(race_config):

    st.markdown(
        """
        <style>

        .status-box {

            border-bottom:1px solid #333;
            padding:20px 0px;
            margin-bottom:30px;

        }


        .status-title {

            color:#ffffff;
            font-size:18px;
            font-weight:600;

        }


        .status-value {

            color:#ffffff;
            font-size:32px;
            font-weight:500;

        }


        .green {

            color:#00ff88;
            font-weight:bold;

        }


        </style>

        """,
        unsafe_allow_html=True
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.markdown(
            f"""
            <div class="status-box">

            <div class="status-title">
            Session
            </div>

            <div class="status-value">
            {race_config['session']}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
            f"""
            <div class="status-box">

            <div class="status-title">
            Circuit
            </div>

            <div class="status-value">
            {race_config['circuit']}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col3:

        st.markdown(
            f"""
            <div class="status-box">

            <div class="status-title">
            Season
            </div>

            <div class="status-value">
            {race_config['year']}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col4:

        st.markdown(
            f"""
            <div class="status-box">

            <div class="status-title">
            Status
            </div>

            <div class="status-value green">
            GREEN FLAG
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )