import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import dash_table
from dash import dcc
from dash import html
from dash_bootstrap_templates import template_from_url, ThemeChangerAIO

from app import app


# =========  Layout  =========== #
layout = dbc.Col([

    # ========= Tabela de Despesa ========= #
    dbc.Row([
        html.Legend("Tabela de despesas"),
        html.Div(id="tabela-despesas", className="dbc")
    ]),

    # ========= Seção de Despesas ========= #
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='graph-despesas', style={"margin-right": "20px"})
        ], width=9),

        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Despesas"),
                    html.Legend("R$ -", id="valor-despesa-card", style={'font-size': '60px'}),
                    html.H6("Total de despesas")
                ], style={'text-align': 'center'})
            ], color="danger")
        ], width=3, style={"margin-top": "70px"})
    ])
], style={"padding": "10px"})

# =========  Callbacks  =========== #
