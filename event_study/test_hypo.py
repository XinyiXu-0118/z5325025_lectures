{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf600
{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl280\partightenfactor0

\f0\fs24 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 """ test_hypo.py\
\
Utilities to test the hypothesis in the study\
"""\
\
import pandas as pd\
\
\
# --------------------------------------------------------\
#   Function to calculate t-stats\
# --------------------------------------------------------\
def calc_tstats(event_cars):\
    """ Compute a t-stat for each event type in dataframe `event_df`.\
\
    Parameters\
    ----------\
    event_cars : dataframe\
        Dataframe with event types and CARs for each event in the sample.\
\
    """\
    # Separate between upgrades and downgrades\
    groups = event_cars.groupby('event_type')['car']\
    print(groups.describe())\
    # Mean\
    car_bar = groups.mean()\
    # Standard error for mean (sem)\
    car_sem = groups.sem()\
    car_t = car_bar/car_sem\
    # collect the number of obs in each group\
    car_n = groups.count()\
    # Construct the result data frame\
    res = pd.DataFrame(\{'car_bar':car_bar, 'car_t': car_t, 'n_obs': car_n\})\
    return res\
}