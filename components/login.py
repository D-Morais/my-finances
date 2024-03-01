from dash import html, dcc, State
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import template_from_url, ThemeChangerAIO
from app import app

layout = dbc.Col([
    dbc.Row(dbc.Col(html.H1("Tela de Login"), width={"size": 6, "offset": 3}), className="mb-4"),
    dbc.Row(dbc.Col(dcc.Input(id='username-input', type='text', placeholder='Digite seu usuário'), width={"size": 6, "offset": 3}), className="mb-4"),
    dbc.Row(dbc.Col(dcc.Input(id='password-input', type='password', placeholder='Digite sua senha'), width={"size": 6, "offset": 3}), className="mb-4"),
    dbc.Row(dbc.Col(dbc.Button("Login", id='login-button', color="primary", className="mr-1"), width={"size": 6, "offset": 3}), className="mb-4"),
    dbc.Row(dbc.Col(html.Div(id='login-output'), width={"size": 6, "offset": 3}))
])


@app.callback(
    Output('login-output', 'children'),
    [Input('login-button', 'n_clicks')],
    [State('username-input', 'value'),
     State('password-input', 'value')]
)
def check_login(n_clicks, username, password):
    if n_clicks is not None:
        if username == 'usuario' and password == 'senha':
            return 'Login bem-sucedido!'
        else:
            return 'Credenciais inválidas.'
    return ''


if __name__ == '__main__':
    app.run_server(debug=True)
