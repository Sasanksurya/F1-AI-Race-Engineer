import streamlit as st
import plotly.graph_objects as go



def render_lap_analysis():


    st.subheader(
        "Lap Performance Analysis"
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Fastest Lap",
            "1:14.532"
        )


    with col2:

        st.metric(
            "Average Lap",
            "1:15.821"
        )


    with col3:

        st.metric(
            "Consistency",
            "94%"
        )


    st.divider()



    sectors = [

        "Sector 1",
        "Sector 2",
        "Sector 3"

    ]


    performance = [

        98,
        85,
        92

    ]


    fig = go.Figure()



    fig.add_trace(

        go.Bar(

            x=sectors,

            y=performance,

            name="Performance"

        )

    )


    fig.update_layout(

        title="Sector Performance",

        template="plotly_dark",

        height=350

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )