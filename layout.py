from dash import Dash, dcc, html
import graph
import styles
import dash_bootstrap_components as dbc

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

# def create_layoutV2(app):
#     return dbc.Container([
#         html.Div([
#             html.Div(
#                 [html.H1('NBA Rebound Analysis')],
#                 style=styles.DASH_TITLE
#             ),
#             graph.rendorCombinedORBTrends(app),
#             graph.rendorHistRI(app)
#         ],
#             style=styles.LEFT_MAIN_DIV
#         ),
#         html.Div([
#             graph.rendorYearSlider(app),
#             html.Div(),
#             html.Div(),
#             html.Div()
#         ],
#             style=styles.RIGHT_MAIN_DIV
#         )
#     ],
#     fluid=False,
#     style={'display':'flex'}, #flex didn't work here, but neither did inline-block
#     className='dashboard-container'
#     )

#04/12 YBZ - adding copying layout function as backup - adding new lower division to the mapping
# def create_layoutV2(app):
#     return html.Div([
#         html.Div([
#             html.Div(
#                 [html.H1('NBA Rebound Analysis')],
#                 style=styles.DASH_TITLE
#             ),
#             graph.rendorCombinedORBTrends(app),
#             graph.rendorHistRI(app)
#         ],
#             style=styles.LEFT_MAIN_DIV
#         ),
#         html.Div([
#             graph.rendorYearSlider(app),
#             graph.rendorRBvRtgTrends(app),
#             html.Div(),
#             html.Div()
#         ],
#             style=styles.RIGHT_MAIN_DIV
#         )
#     ],
#     style=styles.TOP_HALF_DIV
#     )


def create_layoutV2(app):
    return html.Div([
        html.Div([#This is start of the top division styling
            html.Div([ #This is start of the top left division styling
                html.Div(
                    [html.H1('NBA Rebound Analysis')],
                    style=styles.DASH_TITLE
                ),
                graph.rendorCombinedORBTrends(app),
                graph.rendorHistRI(app)
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
        ],
        style=styles.BOTTOM_HALF_DIV
        )
    ],
    style={
        'background':'brown',
        'display':'grid'
    }
    )