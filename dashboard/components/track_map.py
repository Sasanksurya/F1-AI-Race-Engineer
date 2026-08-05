import streamlit as st
import plotly.graph_objects as go


def render_track_map(circuit):


    st.subheader(
        f"{circuit} - Circuit Analysis"
    )


    # Circuit coordinates

    tracks = {


        "Monaco Circuit": {

            "x":[0,2,4,6,8,10,8,5,3,1,0],

            "y":[0,2,4,3,1,-1,-3,-4,-3,-2,0]

        },


        "Silverstone Circuit": {

            "x":[0,3,6,9,12,15,13,8,4,1,0],

            "y":[0,4,5,3,0,-2,-5,-6,-4,-2,0]

        },


        "Monza Circuit": {

            "x":[0,5,10,15,20,15,10,5,0],

            "y":[0,5,5,0,-5,-10,-5,0,0]

        },


        "Suzuka Circuit": {

            "x":[0,3,6,9,12,10,7,4,1,0],

            "y":[0,4,6,4,0,-4,-6,-4,-2,0]

        }

    }



    data = tracks.get(

        circuit,

        tracks["Monaco Circuit"]

    )



    fig = go.Figure()



    # Track line

    fig.add_trace(

        go.Scatter(

            x=data["x"],

            y=data["y"],

            mode="lines",

            line=dict(

                color="#FFFFFF",

                width=8

            ),

            name="Circuit"

        )

    )



    # Driver position marker

    fig.add_trace(

        go.Scatter(

            x=[data["x"][4]],

            y=[data["y"][4]],

            mode="markers+text",

            marker=dict(

                size=20,

                color="#E10600"

            ),

            text=[

                "Max Verstappen"

            ],

            textposition="top center"

        )

    )



    fig.update_layout(

        height=500,

        paper_bgcolor="#050505",

        plot_bgcolor="#050505",

        xaxis=dict(

            visible=False

        ),

        yaxis=dict(

            visible=False

        ),

        margin=dict(

            l=0,

            r=0,

            t=30,

            b=0

        )

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )



    # Circuit Information

    col1,col2,col3 = st.columns(3)


    with col1:

        st.metric(

            "Track Length",

            "5.891 km"

        )


    with col2:

        st.metric(

            "Corners",

            "18"

        )


    with col3:

        st.metric(

            "Track Type",

            "Technical"

        )