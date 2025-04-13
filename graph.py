from plotly import graph_objects as go 
from dash import Dash, dcc, html
import plotly.figure_factory as ff 
import plotly.express as px
from dash.dependencies import Input,Output
import pandas as pd
import ids
from getData import gitAdvData
import styles
import util
import ids
import elements
import dash_bootstrap_templates as dbt
import graphFonts
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
    #Removing the title and background color of the graph
    fig.update_layout(
        # title = {'text':'Playoff Team Offensive Ratings By Season'}, 
        # plot_bgcolor = "white",
        xaxis={'title':'Regular Season Year'},
        yaxis={'title':'Average ORB %','showgrid':True, 'griddash':'solid','gridcolor':'black'},
        width=500,
        height=550
        # margin={
        #     't':15,'b':15,'l':40,'r':15
        # }
        )

    return dcc.Graph(figure=fig,id=ids.YEARLY_ORB)

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
        title = {'text':'ORtg vs ORB% - Regular Seasons','automargin':True}, 
        plot_bgcolor = "white",
        xaxis={'title':'ORB%'},
        yaxis={'title':'ORtg'},
        width=700,
        margin={'t':30,'l':0,'r':0,'b':0},
        showlegend=False
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


def rendorCombinedORBTrends(app):
    return html.Div(children=[
        makeORBGraph(app)
    ],
    style=styles.RB_OVER_TIME)

# def rendorCombinedORBTrends(app):
#     return html.Div(children=[
#         makeORBGraph(app),dcc.Graph(figure=makeORBvOFtg(app,DF=gitAdvData(),id=ids.ORB_ORtg),id=ids.ORB_ORtg,style={'display':'inline-block'})
#     ])



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
        # fig.update_layout(width=1200)
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
        yaxis={'title':'Average DRB %','showgrid':True, 'griddash':'solid','gridcolor':'black'}
        # width=800,
        # height=800
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
        title = {'text':'ORtg vs ORB% - Regular Seasons','automargin':False}, 
        plot_bgcolor = "white",
        xaxis={'title':'ORB%'},
        yaxis={'title':'ORtg'},
        width=700,
        margin={'t':30,'l':0,'r':0,'b':0},
        showlegend=False
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
    def updateDRBSeasonPlot(season):
        # print('In update ORBSeason Plot:') #DELETE
        # print(f"Your selected season - {season}")
        advDF=gitAdvData()
        selectDF=advDF.loc[advDF['Season Year']==season]
        fig=makeDRBvDFtg(app,selectDF,id=ids.SEASONS_DRB_GRAPH)
        # fig.update_layout(width=1200)
        return fig
    return html.Div(dcc.Graph(id=ids.SEASONS_DRB_GRAPH))


#rendorRBvsRtgTrends will change the display of the ORB/DRB vs ORtg/DRtg depending on the slider selection on the app display
def rendorRBvRtgTrends(app):
    @app.callback(
       [
            Output(ids.SEASONS_ORB_GRAPH,'figure'),
            Output(ids.SEASONS_DRB_GRAPH,'figure')
       ],
        Input(ids.YEAR_SLIDER,'value')
    )
    def updateRBSeasonPlots(season):
        advDF=gitAdvData()
        selectDFORB=advDF.loc[advDF['Season Year']==season]
        selectDFDRB=advDF.loc[advDF['Season Year']==season]
        figORB=makeORBvOFtg(app,selectDFORB,id=ids.SEASONS_ORB_GRAPH)
        figDRB=makeDRBvDFtg(app,selectDFDRB,id=ids.SEASONS_DRB_GRAPH)
        return figORB,figDRB
    #This commented out return initially was applying inline-block styling to each of the paired graphs; instead, going to try inline-flex on the parent div
    #return html.Div(children=[dcc.Graph(id=ids.SEASONS_ORB_GRAPH,style={'display':'inline-block'}),dcc.Graph(id=ids.SEASONS_DRB_GRAPH,style={'display':'inline-block'})])
    return html.Div(children=[dcc.Graph(id=ids.SEASONS_ORB_GRAPH,style={'display':'inline-block'}),dcc.Graph(id=ids.SEASONS_DRB_GRAPH,style={'display':'inline-block'})],style=styles.DUAL_RB_GRAPHS)

#-----------------------------------------------------------
#EDIT - consider splitting up functionality here to make more readible 
def makeRBCorrelations(advDF):
    relevantYears = util.uniqueYears(advDF['Season Year'])
    DRBSlopes=util.assignRegSlopeValue(advDF,relevantYears,'DRtg','DRB%',container=[])
    ORBSlopes=util.assignRegSlopeValue(advDF,relevantYears,'ORtg','ORB%',container=[])
    figORB=go.Figure()
    figDRB=go.Figure()
    figORB=drawRBRegPlot(ORBSlopes,relevantYears,figORB)
    figDRB=drawRBRegPlot(DRBSlopes,relevantYears,figDRB)
    return[figORB,figDRB]

def drawRBRegPlot(rbRegStats,seasonYears,fig):
    fig.add_trace(
        go.Scatter(
            x=seasonYears,
            y=rbRegStats,
            mode='markers'
        )
    )
    return fig


#DELETE - these scatterplots will be deleted; currently being used to experiment with graph placement by moving the location
def rendorRBRegressionPlots(app):
    reboundRegressionFigs=makeRBCorrelations(advDF=gitAdvData()) #please note - index 0 represents offensive rebounds; index 1 reprsents defensive rebounds
    reboundRegressionFigs[0].update_layout(
        title={'text':'Offensive Rebound Percentage Value to ORtg'},
        yaxis={'title':'ORtg increase per ORB % [PP 100/%]'},
        xaxis={'title':'Season Year'},
    )
    reboundRegressionFigs[1].update_layout(
        title={'text':'Defensive Rebound Percentage Value to DRtg'},
        yaxis={'title':'DRtg increase per ORB % [PP 100/%]'},
        xaxis={'title':'Season Year'},
    )
    return html.Div(
        children=[
            dcc.Graph(figure=reboundRegressionFigs[0],id=ids.ORB_REGRESSION_STATS_GRAPH,style={'display':'inline-block'}),
            dcc.Graph(figure=reboundRegressionFigs[1],id=ids.DRB_REGRESSION_STATS_GRAPH,style={'display':'inline-block'})
        ]
    )

def getCorrelationHist(advDF):
    histFigs=[]
    histLabels=['ORB% v. OFRtg - Correlations','DRB% v. DFRtg - Correlations']
    relevantYears = util.uniqueYears(advDF['Season Year'])
    ORBCorrelations=util.getCorrelationValues(advDF,relevantYears,'ORtg','ORB%')
    DRBCorrelations=util.getCorrelationValues(advDF,relevantYears,'DRtg','DRB%')
    correlations = [ORBCorrelations,DRBCorrelations]
    for count,correlation in enumerate(correlations): #use the enumerate function instead here to make neater
        data=[correlation]
        tempFig=ff.create_distplot(data,[histLabels[count]],bin_size=0.025)
        maxHistValue=max(data[0])
        minHistValue=min(data[0])
        xHighRange=1.1*maxHistValue#DELETE - no longer necessary once you get static axis range 
        xLowRange=0.9*minHistValue#DELETE - no longer necessary once you get static axis range 
        xHighRange=0.75
        xLowRange=-0.75
        tempFig.update_layout(
            title={'text':histLabels[count]},
            xaxis={'range':[xLowRange,xHighRange]}
        )
        histFigs.append(tempFig)
    return histFigs

def getRegressionHist(advDF):
    histFigs=[]
    histLabels=['ORB% v. OFRtg - Regression Slopes','DRB% v. DFRtg - Regression Slopes']
    relevantYears = util.uniqueYears(advDF['Season Year'])
    DRBSlopes=util.assignRegSlopeValue(advDF,relevantYears,'DRtg','DRB%',container=[])
    ORBSlopes=util.assignRegSlopeValue(advDF,relevantYears,'ORtg','ORB%',container=[])
    for count,slopeValue in enumerate([ORBSlopes,DRBSlopes]):
        data=[slopeValue]
        tempFig=ff.create_distplot(data,[histLabels[count]],bin_size=0.025)
        maxHistValue=max(data[0])
        minHistValue=min(data[0])
        xHighRange=1.1*maxHistValue#DELETE - no longer necessary once you get static axis range 
        xLowRange=0.9*minHistValue#DELETE - no longer necessary once you get static axis range 
        xHighRange=0.75
        xLowRange=-0.75
        tempFig.update_layout(
            title={'text':histLabels[count]},
            xaxis={'range':[xLowRange,xHighRange]}
        )
        histFigs.append(tempFig)

    return histFigs

def rendorHistRI(app):
    return html.Div(
        [elements.makeReboundRadioSelect()],
        style=styles.RI_HIST_BUTTONS
    )

def rendorHistograms(app):
    @app.callback(
        [
            Output(ids.ORB_HISTOGRAM,'figure'),
            Output(ids.DRB_HISTOGRAM,'figure')
        ],
        [
            Input(ids.HISTOGRAM_SELECTION,'value')
        ]
    )
    def updateHistograms(menuSelection):
        if menuSelection==elements.histOptions[0]:
            selectedHists=getRegressionHist(advDF=gitAdvData())
        if menuSelection==elements.histOptions[1]:
            selectedHists=getCorrelationHist(advDF=gitAdvData())
        for fig in selectedHists:
            fig.update_layout(
                width=1500,
                height=300,
                showlegend=False,
                margin={
                    't':30,'b':0
                },
            )
            pass
        return selectedHists[0],selectedHists[1] #EDIT - probably can just return a list or a tuple of sorts, instead of specifying the index of each figure in the list
    return html.Div(children=[dcc.Graph(id=ids.ORB_HISTOGRAM),dcc.Graph(id=ids.DRB_HISTOGRAM)],style=styles.HISTOGRAMS)


def rendorYearSlider(app):
    df=gitAdvData()
    relevantYears=util.uniqueYears(df['Season Year'])
    return html.Div(
        [elements.makeSlider(relevantYears)],
        style=styles.TIMELINE
    )



