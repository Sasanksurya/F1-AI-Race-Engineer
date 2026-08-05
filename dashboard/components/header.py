import streamlit as st



def render_header():


    st.markdown(

        """

<style>


.f1-header {


    background:

    linear-gradient(

        135deg,

        #0b0b0b,

        #181818

    );


    border:1px solid #ff1e1e;


    border-radius:18px;


    padding:30px;


    margin-bottom:20px;


}



.f1-title {


    color:white;

    font-size:42px;

    font-weight:900;

    letter-spacing:1px;


}



.f1-subtitle {


    color:#a0a0a0;

    font-size:18px;


}



.status-container {


    display:flex;

    gap:15px;

    margin-top:20px;


}



.status-card {


    background:#111;

    border:1px solid #333;

    border-radius:8px;

    padding:12px 20px;

    color:#ddd;

    font-size:15px;


}


.status-active {


    color:#00c853;

    font-weight:600;

}


</style>



<div class="f1-header">


<div class="f1-title">

F1 AI Race Engineer

</div>



<div class="f1-subtitle">

Formula 1 Performance Analysis, Strategy Optimization and Race Intelligence Platform

</div>



<div class="status-container">


<div class="status-card">

<span class="status-active">

Active

</span>

&nbsp; Race Analysis

</div>



<div class="status-card">

AI Strategy Engine Online

</div>



<div class="status-card">

Telemetry System Connected

</div>



</div>


</div>

        """,

        unsafe_allow_html=True

    )