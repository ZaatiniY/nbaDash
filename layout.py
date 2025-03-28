from dash import Dash, dcc, html
import graph

def create_layout(app: Dash):
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            graph.rendorCombinedORBTrends(app)
        ]
    )