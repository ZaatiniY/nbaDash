from plotly import graph_objects as go 
from dash import Dash, dcc, html
import pandas as pd
import ids
from getData import gitAdvData
import util
import ids


def makeORBGraph(app):
    advDF = gitAdvData() 
    fig=go.Figure()
    relevantYears = (util.uniqueYears(advDF['Season Year']))
    relevantYears.pop(0) #removing the first item from the last since it's not a concluded data point 
    averageYearlyORBP = util.calcAvgYearlyStat(advDF,relevantYears,columnName = 'ORB%')
    fig.add_trace(go.Scatter(
        y = averageYearlyORBP,
        x = relevantYears,
        name = "Average ORB% per season",
        mode = 'lines+markers',
        line = {'color':'cadetblue'}
        )
        )
        # fig.update_layout(
        #     title = {'text':'Playoff Team Offensive Ratings By Season'}, 
        #     plot_bgcolor = "white",
        #     xaxis={'title':'Regular Season Year'},
        #     yaxis={'title':'Average ORB %','showgrid':True, 'griddash':'solid','gridcolor':'black'}
        #     )
    fig.update_layout(
        title = {'text':'Playoff Team Offensive Ratings By Season'}, 
        plot_bgcolor = "white",
        xaxis={'title':'Regular Season Year'},
        yaxis={'title':'Average ORB %','showgrid':True, 'griddash':'solid','gridcolor':'black'},
        width=800,
        height=800
        )

    return dcc.Graph(figure=fig,id=ids.YEARLY_ORB,style={'display':'inline-block'})
    #return dcc.Graph(figure={'data':data,'layout':},id=ids.YEARLY_ORB,style={'display':'inline-block'})

def makeORBvOFtg(app):
    advDF = gitAdvData()
    uniqueSeasonNames = [advDF['Team'][x] + ' '+ str(advDF['Season Year'][x]) for x in range(len(advDF['Team']))]  
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            y = advDF['ORtg'],
            x = advDF['ORB%'],
            name = "ORtg vs ORB",
            text = uniqueSeasonNames,
            mode = 'markers',
            line = {'color':'cadetblue'}
        )
    )
    fig.update_layout(
        title = {'text':'Playoff Team Offensive Ratings By Season'}, 
        plot_bgcolor = "white",
        xaxis={'title':'Regular Season Year'},
        yaxis={'title':'Average ORB %'},
        width=800,height=800
        )
    fig.add_trace(makeRegressionScatter(advDF['ORB%'],advDF['ORtg']))
    # fig.add_shape(
    #      type='rect',
    #      xref='x domain',yref='y domain',
    #      x0=0.70,x1=1.0,y0=0.80,y1=0.9
    # )

    fig.add_annotation(
        text="This is my box",
         xref='x domain',
         yref='y domain',
         x=0.8,
         y=0.8,
         borderwidth=2,
         bordercolor='black'
    )

    return dcc.Graph(figure=fig,id=ids.ORB_ORtg,style={'display':'inline-block'})

def rendorCombinedORBTrends(app):
    return html.Div(children=[
        makeORBGraph(app),makeORBvOFtg(app)
    ])


#inputs of xValue and yValue need to be dataframes 
def makeRegressionScatter(xValue,yValue):
        slope,intercept = util.linearRegCalc(xValue,yValue)
        sortedX = xValue.tolist()
        sortedX.sort()
        sortedY = [(slope*i)+intercept for i in sortedX]
        return go.Scatter(
            x = sortedX,
            y = sortedY,
            name = 'ORtg Regression',
            mode = 'lines',
            line =  {'color':'black','dash':'dot'}
        )