from dash import Dash, html, callback, Output, Input
from layout import create_layout
from getData import gitAdvData


def main():
    app = Dash()
    app.title="NBA Analysis Site"
    app.layout = create_layout(app)
    app.run()


# @callback(
#     Output(component_id='controls-and-graph', component_property='figure'),
#     Input(component_id='controls-and-radio-item', component_property='value')
# )
# def update_graph(col_chosen):
#     fig = 0
#     return fig


if __name__ == '__main__':
    main()
