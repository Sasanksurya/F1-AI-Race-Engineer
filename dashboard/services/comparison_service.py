from data.drivers import DRIVERS



def compare_drivers(

    driver1,

    driver2

):


    d1 = DRIVERS[driver1]

    d2 = DRIVERS[driver2]



    comparison = {


        "driver1": driver1,

        "driver2": driver2,


        "points": {

            driver1: d1["points"],

            driver2: d2["points"]

        },


        "wins": {

            driver1: d1["wins"],

            driver2: d2["wins"]

        },


        "podiums": {

            driver1: d1["podiums"],

            driver2: d2["podiums"]

        },


        "poles": {

            driver1: d1["poles"],

            driver2: d2["poles"]

        }

    }



    if d1["points"] > d2["points"]:

        comparison["advantage"] = driver1

    else:

        comparison["advantage"] = driver2



    return comparison