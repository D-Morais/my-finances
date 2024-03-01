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

    # ========= Tabela de Receita ========= #
    dbc.Row([
        html.Legend("Tabela de receitas"),
        html.Div(id="tabela-receitas", className="dbc")
    ]),

    # ========= Seção de Receitas ========= #
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='graph-receitas', style={"margin-right": "20px"})
        ], width=9),

        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Receitas"),
                    html.Legend("R$ -", id="valor-receita-card", style={'font-size': '60px'}),
                    html.H6("Total de receitas")
                ], style={'text-align': 'center'})
            ], color="success")
        ], width=3, style={"margin-top": "70px"})
    ])
], style={"padding": "10px"})


# =========  Callbacks  =========== #
# Tabela
@app.callback(
    Output('tabela-receitas', 'children'),
    Input('store-receitas', 'data')
)
def show_table(data):
    df = pd.DataFrame(data)

    df.loc[df['Efetuado'] == 0, 'Efetuado'] = 'Não'
    df.loc[df['Efetuado'] == 1, 'Efetuado'] = 'Sim'

    df.loc[df['Fixo'] == 0, 'Fixo'] = 'Não'
    df.loc[df['Fixo'] == 1, 'Fixo'] = 'Sim'

    df = df.fillna('-')

    df.sort_values(by='Data', ascending=False)

    tabela = dash_table.DataTable(
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": False, "hideable": True}
            if i == "Descrição" or i == "Fixo" or i == "Efetuado"
            else {"name": i, "id": i, "deletable": False, "selectable": False}
            for i in df.columns
        ],

        data=df.to_dict('records'),
        sort_action="native",
        sort_mode="single",
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current=0,
        page_size=10,
    ),

    return tabela
