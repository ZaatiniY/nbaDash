from plotly import graph_objects as go 
from dash import Dash, dcc, html
from dash.dependencies import Input,Output
import pandas as pd
import ids
from getData import gitAdvData
import util
import ids
import elements
import dash_bootstrap_templates as dbt
dbt.load_figure_template(['lux'])

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

#changing so that you need to input which DF you want to use 
#deleted the relevantID variable; will still be keeping the DF variable
#id is being added as a parameter to know whether or not we want to add a regression line to the charts 
def makeORBvOFtg(app,DF,id):
    copiedDF=DF.copy()
    uniqueSeasonNames = [copiedDF['Team'][x] + ' '+ str(copiedDF['Season Year'][x]) for x in copiedDF.index.tolist()]
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            y = copiedDF['ORtg'],
            x = copiedDF['ORB%'],
            name = "ORtg vs ORB",
            text = uniqueSeasonNames,
            mode = 'markers',
            line = {'color':'cadetblue'}
        )
    )
    fig.update_layout(
        title = {'text':'ORtg vs ORB% - Regular Seasons'}, 
        plot_bgcolor = "white",
        xaxis={'title':'ORB%'},
        yaxis={'title':'ORtg'},
        width=800,height=800
        )
    if id in ids.REGRESSION_TRACES:
        fig.add_trace(makeRegressionScatter(copiedDF['ORB%'],copiedDF['ORtg']))

    # #taking out annotations around ORtg vs ORB%, for some reaseon they look inversely related - will look into it more    
    # # (slope,intercept)=util.linearRegCalc(advDF['ORB%'],advDF['ORtg'])
    # # annotationText=f'{slope} Increase in ORtg per % ORB'
    # fig.add_annotation(
    #     #text=annotationText,
    #      xref='x domain',
    #      yref='y domain',
    #      x=0.8,
    #      y=0.8,
    #      borderwidth=2,
    #      bordercolor='black',
    #      showarrow=False
    # )

    return fig

# def rendorCombinedORBTrends(app):
#     return html.Div(children=[
#         makeORBGraph(app),makeORBvOFtg(app,DF=gitAdvData(),relevantID=ids.ORB_ORtg)
#     ])

def rendorCombinedORBTrends(app):
    return html.Div(children=[
        makeORBGraph(app),dcc.Graph(figure=makeORBvOFtg(app,DF=gitAdvData(),id=ids.ORB_ORtg),id=ids.ORB_ORtg,style={'display':'inline-block'})
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

def rendorORBSeasonGraph(app):
    @app.callback(
        Output(ids.SEASONS_ORB_GRAPH,"figure"),
        [Input(ids.SEASONS_DD,'value')]
    )
    def updateORBSeasonPlot(season):
        # print('In update ORBSeason Plot:') #DELETE
        # print(f"Your selected season - {season}")
        advDF=gitAdvData()
        selectDF=advDF.loc[advDF['Season Year']==season]
        fig=makeORBvOFtg(app,selectDF,id=ids.SEASONS_ORB_GRAPH)
        fig.update_layout(width=1200)
        return fig
    return html.Div(dcc.Graph(id=ids.SEASONS_ORB_GRAPH))

#DELETE - remove this function later it's to test if the DD is rendoring by itself
def rendorORBDD(app):
    advDF=gitAdvData()
    years=util.uniqueYears(advDF['Season Year'])
    visualElement = elements.makeORBDD(years,menuItems=['label','value'])
    return html.Div(children=visualElement)


#--------------------------------------------------------------------------------------------------

def makeDRBGraph(app):
    advDF = gitAdvData() 
    fig=go.Figure()
    relevantYears = (util.uniqueYears(advDF['Season Year']))
    relevantYears.pop(0) #removing the first item from the last since it's not a concluded data point 
    averageYearlyDRBP = util.calcAvgYearlyStat(advDF,relevantYears,columnName = 'DRB%')
    fig.add_trace(go.Scatter(
        y = averageYearlyDRBP,
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
        yaxis={'title':'Average DRB %','showgrid':True, 'griddash':'solid','gridcolor':'black'},
        width=800,
        height=800
        )

    return dcc.Graph(figure=fig,id=ids.YEARLY_DRB,style={'display':'inline-block'})
    #return dcc.Graph(figure={'data':data,'layout':},id=ids.YEARLY_ORB,style={'display':'inline-block'})

#changing so that you need to input which DF you want to use 
#deleted the relevantID variable; will still be keeping the DF variable
#id is being added as a parameter to know whether or not we want to add a regression line to the charts 
def makeDRBvDFtg(app,DF,id):
    copiedDF=DF.copy()
    uniqueSeasonNames = [copiedDF['Team'][x] + ' '+ str(copiedDF['Season Year'][x]) for x in copiedDF.index.tolist()]
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            y = copiedDF['DRtg'],
            x = copiedDF['DRB%'],
            name = "ORtg vs ORB",
            text = uniqueSeasonNames,
            mode = 'markers',
            line = {'color':'cadetblue'}
        )
    )
    fig.update_layout(
        title = {'text':'ORtg vs ORB% - Regular Seasons'}, 
        plot_bgcolor = "white",
        xaxis={'title':'ORB%'},
        yaxis={'title':'ORtg'},
        width=800,height=800
        )
    if id==ids.SEASONS_ORB_GRAPH:
        fig.add_trace(makeRegressionScatter(copiedDF['ORB%'],copiedDF['ORtg']))

    if id==ids.SEASONS_DRB_GRAPH:
        fig.add_trace(makeRegressionScatter(copiedDF['DRB%'],copiedDF['DRtg']))
    
    return fig

# def rendorCombinedORBTrends(app):
#     return html.Div(children=[
#         makeORBGraph(app),makeORBvOFtg(app,DF=gitAdvData(),relevantID=ids.ORB_ORtg)
#     ])

def rendorCombinedDRBTrends(app):
    return html.Div(children=[
        makeDRBGraph(app),dcc.Graph(figure=makeDRBvDFtg(app,DF=gitAdvData(),id=ids.DRB_DRtg),id=ids.DRB_DRtg,style={'display':'inline-block'})
    ])




def rendorDRBSeasonGraph(app):
    @app.callback(
        Output(ids.SEASONS_DRB_GRAPH,"figure"),
        [Input(ids.SEASONS_DD,'value')]
    )
    def updateORBSeasonPlot(season):
        # print('In update ORBSeason Plot:') #DELETE
        # print(f"Your selected season - {season}")
        advDF=gitAdvData()
        selectDF=advDF.loc[advDF['Season Year']==season]
        fig=makeDRBvDFtg(app,selectDF,id=ids.SEASONS_DRB_GRAPH)
        fig.update_layout(width=1200)
        return fig
    return html.Div(dcc.Graph(id=ids.SEASONS_DRB_GRAPH))


#this function is so ugly lol
def makeRBCorrelations(app):
    advDF=gitAdvData()
    relevantYears = util.uniqueYears(advDF['Season Year'])
    print(relevantYears)
    DRBSlopes=[]
    ORBSlopes=[]
    for year in relevantYears:
        currDF = advDF.copy()
        print(currDF)
        currDF=currDF.loc[advDF['Season Year']==year]
        DRBSlopes=util.assignRegSlopeValue(currDF,'DRtg','DRB%',ORBSlopes)
        ORBSlopes=util.assignRegSlopeValue(currDF,'ORtg','ORB%',ORBSlopes)
    