def generate_engineer_message(

    driver,

    circuit,

    session,

    prediction,

    strategy

):


    message = f"""

Race Engineer Report


Driver:

{driver}


Circuit:

{circuit}


Session:

{session}



Strategy Recommendation:

{strategy["tyre"]}


Pit Window:

{strategy["pit_window"]}



Prediction:

Win Probability:

{prediction["win_probability"]}%


Podium Probability:

{prediction["podium_probability"]}%



Engineer Analysis:


Strong performance analysis completed.

Focus on:

- Tyre management
- Consistent lap pace
- Sector performance


"""


    return message