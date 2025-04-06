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

histOptions=['Pts per Rebound %','Correlation'] #EDIT - this is being referenced in the graph file for attributing the callback Input 
def makeReboundRadioSelect():
    menuOptions=['Pts per Rebound %','Correlation']
    return dcc.RadioItems(
        id=ids.HISTOGRAM_SELECTION,
        options=menuOptions,
        value='Pts per Rebound %',inline=True
    )

def makeSlider(relevantYears):
    yearMarkers={year:year for year in relevantYears}
    relevantYears[5]
    print(yearMarkers)
    return dcc.Slider(
        step=None,
        marks=yearMarkers,
        value=relevantYears[0],
        id=ids.YEAR_SLIDER
    )
    
