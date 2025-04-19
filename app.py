from dash import Dash, html, callback, Output, Input
from getData import gitAdvData
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from layout import create_layoutV2

def main():
    # load_figure_template('LUX')
    # app = Dash(external_stylesheets=[dbc.themes.LUX])
    app=Dash() #this is us testing with v2 of create_layout
    app.title="NBA Analysis Site"
    app.layout = create_layoutV2(app)
    app.run()


if __name__ == '__main__':
    main()
