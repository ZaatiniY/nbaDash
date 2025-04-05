from dash import Dash, html, dcc
from plotly import graph_objects as go 
import numpy as np
import ids

#One issue running into - graph.py is turning into the file where all the data gets
#   pushed to different functions 
def makeORBDD(relevantYears,menuItems):
    menuOptions=[]
    for year in relevantYears:
        menuOptions.append({item:year for item in menuItems})
    return dcc.Dropdown(
        id=ids.SEASONS_DD,
        options=menuOptions,
        value=menuOptions[0]['value'], #sets the initial dropdown menu option to the first year in the relevantYears selections
        multi=False
    )

histOptions=['Pts per Rebound %','Correlation']
def makeReboundRadioSelect():
    menuOptions=['Pts per Rebound %','Correlation']
    return dcc.RadioItems(
        id=ids.HISTOGRAM_SELECTION,
        options=menuOptions,
        value='Pts per Rebound %',inline=True
    )