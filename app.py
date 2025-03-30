from dash import Dash, html, callback, Output, Input
from layout import create_layout
from getData import gitAdvData


def main():
    app = Dash()
    app.title="NBA Analysis Site"
    app.layout = create_layout(app)
    app.run()


if __name__ == '__main__':
    main()
