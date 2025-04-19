from dash import Dash, dcc, html
import graph
import styles
import dash_bootstrap_components as dbc

def create_layoutV2(app):
    return html.Div([
        html.Div(
            [html.H1('NBA Rebound Analysis')],
            style=styles.DASH_TITLE
        ),            
        html.Div([#This is start of the top division styling
            html.Div([ #This is start of the top left division styling
                graph.rendorCombinedORBTrends(app)
            ],
                style=styles.LEFT_MAIN_DIV
            ),
            html.Div([
                graph.rendorYearSlider(app),
                graph.rendorRBvRtgTrends(app),
                html.Div(),
                html.Div()
            ],
                style=styles.RIGHT_MAIN_DIV
            )
        ],
        style=styles.TOP_HALF_DIV
        ),
        html.Div([
            graph.rendorHistRI(app),
            graph.rendorHistograms(app)
        ],
        style=styles.BOTTOM_HALF_DIV
        )
    ],
    style={
        'background':'brown',
        'display':'grid'
    }
    )