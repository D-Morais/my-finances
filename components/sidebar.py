from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO
from datetime import datetime, date
import pandas as pd

from app import app

# ========= Layout ========= #
layout = dbc.Card([
    html.H1("Minhas", className="text-primary", style={"text-align": "center"}),
    html.H1("Finanças", className='text-primary', style={"text-align": "center"}),
    html.Hr(),

    # ========= Seleção de Perfil ========= #
    dbc.Button(id='botao_avatar',
               children=[html.Img(src="/assets/img_hom.png", id="avatar_change", alt="Avatar", className='perfil_avatar'
                                  )],
               style={'background-color': 'transparent', 'border-color': 'transparent'}
               ),
    html.Hr(),

    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Acessar Perfil"), close_button=False),
        dbc.ModalBody([
            dbc.Col([
                dbc.Card([
                    dbc.CardImg(src="/assets/img_hom.png", className='perfil_avatar', top=True),
                    dbc.CardBody([
                        dbc.Row(dbc.Col(html.H3("Meu Usuário"), width={"size": 6, "offset": 4}), className="mb-4"),
                        dbc.FormFloating([
                            dbc.Input(
                                    type="text", id="username-input", placeholder="Usuário"
                            ),
                            dbc.Label("Usuário", html_for="example-email-row", width=7)
                        ], style={"margin": "20px"}),
                        dbc.FormFloating([
                            dbc.Input(
                                type="password", id="password-input", placeholder="Senha",
                            ),
                            dbc.Label("Senha", html_for="example-password-row", width=5)
                        ], style={"margin": "20px"}),
                        dbc.Row([
                            dbc.Col([
                                dbc.Button("Acessar", id='login-button', color="primary", className="mr-1"),
                                dbc.Button("Adicionar usuário", id='adc', color="success")
                            ], style={"display": "flex", "justify-content": "space-between"})
                        ], style={"margin": "20px"})
                    ])
                ])
            ], width=6),
        ], style={"display": "flex", "justify-content": "center"})
    ],
        style={"background-color": "rgba(0, 0, 0, 0.5)"},
        id="modal-perfil",
        size="lg",
        is_open=True,
        fullscreen=True,
        backdrop=False
    ),

    # ========= Seleção de Perfil ========= #
    dbc.Row([
        dbc.Col([
            dbc.Button(color="success", id="open-novo-receita", children=["+ Receita"]),
        ], width=6),

        dbc.Col([
            dbc.Button(color="danger", id="open-novo-despesa", children=["+ Despesa"]),
        ], width=6)
    ], style={"margin-left": "20px", "margin-top": "10px", "margin-bottom": "10px"}),

    # ========= Modal Receita ========= #
    html.Div([
        dbc.Modal([
            dbc.ModalHeader(dbc.ModalTitle("Adicionar receita")),
            dbc.ModalBody([
                dbc.Row([
                    dbc.Col([
                        dbc.Label("Descrição: "),
                        dbc.Input(placeholder="Ex.: dividendos da bolsa, herança...", id="txt-receita"),
                    ], width=6, style={"padding": "2px"}),
                    dbc.Col([
                        dbc.Label("Valor: "),
                        dbc.Input(placeholder="$100.00", id="valor_receita", value="")
                    ], width=6, style={"padding": "2px"})
                ]),

                dbc.Row([
                    dbc.Col([
                        dbc.Label("Data: "),
                        dcc.DatePickerSingle(id='date-receitas',
                                             min_date_allowed=date(2020, 1, 1),
                                             max_date_allowed=date(2030, 12, 31),
                                             date=datetime.today(),
                                             style={"width": "100%"},
                                             display_format='D/M/Y'
                                             )
                    ], width=4),

                    dbc.Col([
                        dbc.Label("Extras"),
                        dbc.Checklist(
                            options=[{"label": "Foi recebida", "value": 1},
                                     {"label": "Receita Recorrente", "value": 2}],
                            value=[1],
                            id="switches-input-receita",
                            switch=True
                        )
                    ], width=4),

                    dbc.Col([
                        html.Label("Categoria da receita"),
                        dbc.Select(id="select_receita",
                                   # options=[{"label": i, "value": i} for i in cat_receita],
                                   # value=cat_receita[0]
                                   )
                    ], width=4)
                ], style={"margin-top": "25px"}),

                dbc.Row([
                    dbc.Accordion([
                        dbc.AccordionItem(children=[
                            dbc.Row([
                                dbc.Col([
                                    html.Legend(
                                        "Adicionar categoria", style={'color': 'green', "text-align": "center"}
                                    ),
                                    dbc.Input(type="text", placeholder="Nova categoria...", id="input-add-receita",
                                              value=""),
                                    html.Br(),
                                    dbc.Button("Adicionar", className="btn btn-success", id="add-category-receita",
                                               style={"margin-top": "20px"}),
                                    html.Br(),
                                    html.Div(id="category-div-add-receita", style={}),
                                ], width=6, style={"padding": "5px"}),

                                dbc.Col([
                                    html.Legend("Excluir categorias", style={'color': 'red', "text-align": "center"}),
                                    dbc.Checklist(
                                        id="checklist-selected-style-receita",
                                        # options=[{"label": i, "value": i} for i in cat_receita],
                                        value=[],
                                        label_checked_style={"color": "red"},
                                        input_checked_style={"backgroundColor": "#fa7268",
                                                             "borderColor": "#ea6258"},
                                    ),
                                    dbc.Button("Remover", color="danger", id="remove-category-receita",
                                               style={"margin-top": "20px"}),
                                ], width=6, style={"padding": "5px"})
                            ]),
                        ], title="Adicionar/Remover Categorias", ),
                    ], flush=True, start_collapsed=True, id='accordion-receita'),

                    html.Div(id="id_teste_receita", style={"padding-top": "20px"}),

                    dbc.ModalFooter([
                        dbc.Button("Adicionar Receita", id="salvar_receita", color="success"),
                        dbc.Popover(dbc.PopoverBody("Receita Salva"), target="salvar_receita", placement="left",
                                    trigger="click"),
                    ])
                ], style={"margin-top": "25px"}),
            ])
        ],
            style={"background-color": "rgba(17, 140, 79, 0.05)"},
            id="modal-novo-receita",
            size="lg",
            is_open=False,
            centered=True,
            backdrop=True)
    ]),

    # ========= Modal Despesa ========= #
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Adicionar despesa")),
        dbc.ModalBody([
            dbc.Row([
                dbc.Col([
                    dbc.Label("Descrição: "),
                    dbc.Input(placeholder="Ex.: dividendos da bolsa, herança...", id="txt-despesa"),
                ], width=6, style={"padding": "2px"}),
                dbc.Col([
                    dbc.Label("Valor: "),
                    dbc.Input(placeholder="$100.00", id="valor_despesa", value="")
                ], width=6, style={"padding": "2px"})
            ]),

            dbc.Row([
                dbc.Col([
                    dbc.Label("Data: "),
                    dcc.DatePickerSingle(id='date-despesas',
                                         min_date_allowed=date(2020, 1, 1),
                                         max_date_allowed=date(2030, 12, 31),
                                         date=datetime.today(),
                                         style={"width": "100%"},
                                         display_format='D/M/Y'
                                         ),
                ], width=4),

                dbc.Col([
                    dbc.Label("Opções Extras"),
                    dbc.Checklist(
                        options=[{"label": "Foi recebida", "value": 1},
                                 {"label": "despesa Recorrente", "value": 2}],
                        value=[1],
                        id="switches-input-despesa",
                        switch=True)
                ], width=4),

                dbc.Col([
                    html.Label("Categoria da despesa"),
                    dbc.Select(id="select_despesa", options=[0])
                    # dbc.Select(id="select_despesa", options=[{"label": i, "value": i} for i in cat_despesa])
                ], width=4)
            ], style={"margin-top": "25px"}),

            dbc.Row([
                dbc.Accordion([
                    dbc.AccordionItem(children=[
                        dbc.Row([
                            dbc.Col([
                                html.Legend("Adicionar categoria", style={'color': 'green', "text-align": "center"}),
                                dbc.Input(type="text", placeholder="Nova categoria...", id="input-add-despesa",
                                          value=""),
                                html.Br(),
                                dbc.Button("Adicionar", className="btn btn-success", id="add-category-despesa",
                                           style={"margin-top": "20px"}),
                                html.Br(),
                                html.Div(id="category-div-add-despesa", style={})
                            ], width=6, style={"padding": "5px"}),

                            dbc.Col([
                                html.Legend("Excluir categorias", style={'color': 'red', "text-align": "center"}),
                                dbc.Checklist(
                                    id="checklist-selected-style-despesa",
                                    # options=[{"label": i, "value": i} for i in cat_despesa],
                                    value=[],
                                    label_checked_style={"color": "red"},
                                    input_checked_style={"backgroundColor": "#fa7268",
                                                         "borderColor": "#ea6258"},
                                ),
                                dbc.Button("Remover", color="danger", id="remove-category-despesa",
                                           style={"margin-top": "20px"}),
                            ], width=6, style={"padding": "5px"})
                        ]),
                    ], title="Adicionar/Remover Categorias",
                    )
                ], flush=True, start_collapsed=True, id='accordion-despesa'),
                html.Hr(),
                dbc.ModalFooter([
                    dbc.Button("Adicionar Despesa", color="danger", id="salvar_despesa", value="despesa"),
                    dbc.Popover(dbc.PopoverBody("Despesa Salva"), target="salvar_despesa", placement="left",
                                trigger="click"),
                ])
            ], style={"margin-top": "25px"}),
        ])
    ],
        style={"background-color": "rgba(17, 140, 79, 0.05)"},
        id="modal-novo-despesa",
        size="lg",
        is_open=False,
        centered=True,
        backdrop=True),

    # ========= Seção de Navegação Lateral ========= #
    html.Hr(),
    dbc.Nav([
        dbc.NavLink("Dashboard", href="/dashboards", active="exact"),
        dbc.NavLink("Despesas", href="/despesas", active="exact"),
        dbc.NavLink("Receitas", href="/receitas", active="exact")
    ], vertical=True, pills=True, id="nav_buttons", style={"margin-botton": "50px"}),
    html.Hr(),
    ThemeChangerAIO(aio_id="theme", radio_props={"value": dbc.themes.CYBORG})
], id='sidebar_completa', style={"height": "98%", "margin": "10px"})
