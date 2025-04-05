from dash import Dash, dcc, html
import graph

def create_layout(app: Dash):
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            graph.rendorCombinedORBTrends(app),
            html.Hr(),
            html.H4('Trying a Dropdown'),
            html.Div(className='dropdown-container',
                children=[
                    graph.rendorORBDD(app)
                ]),
            graph.rendorORBSeasonGraph(app),
            html.Hr(),
            graph.rendorCombinedDRBTrends(app),
            html.Hr(),
            graph.rendorDRBSeasonGraph(app),
            html.Hr(),
            graph.rendorRBRegressionPlots(app),
            html.Hr(),
            # graph.rendorHistRI(app),
            # graph.rendorHistograms(app),
            graph.rendorYearSlider(app)
        ]
    )