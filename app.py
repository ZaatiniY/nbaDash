from dash import Dash, html, callback, Output, Input
from layout import create_layout
from getData import gitAdvData
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template



def main():
    load_figure_template('LUX')
    app = Dash(external_stylesheets=[dbc.themes.LUX])
    app.title="NBA Analysis Site"
    app.layout = create_layout(app)
    app.run()


if __name__ == '__main__':
    main()
