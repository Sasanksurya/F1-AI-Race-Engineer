import pandas as pd



def get_race_results(session):


    if session is None:

        return None



    results = session.results



    if results is None:

        return None



    data = results[

        [

            "FullName",

            "TeamName",

            "Position",

            "Points"

        ]

    ].copy()



    data.columns = [

        "Driver",

        "Team",

        "Position",

        "Points"

    ]



    return data