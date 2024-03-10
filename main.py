import pandas as pd
from dash import html, dcc
from dash.dependencies import Input, Output

from app import *
from components import sidebar, dashboards, despesas, receitas, login

# =========  Layout  =========== #
content = html.Div(id="page-content")

app.layout = dbc.Container(children=[

    dbc.Row([
        dbc.Col([
            dcc.Location(id='url'),
            sidebar.layout
        ], md=3),

        dbc.Col([
            html.Div(id="page-content")
        ], md=9),
    ])

], fluid=True, style={"padding": "0px"}, className="dbc")


@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def render_page(pathname):
    if pathname == '/' or pathname == '/dashboards':
        return dashboards.layout

    if pathname == '/despesas':
        return despesas.layout

    if pathname == '/receitas':
        return receitas.layout


if __name__ == '__main__':
    app.run_server(debug=True)
