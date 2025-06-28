# components/layout.py
from dash import html, dcc

def get_layout(df):
    return html.Div([
        html.H1("🌍 Global Indicators Dashboard", style={'textAlign': 'center'}),

        html.Div([
            html.Label("Select a Continent:"),
            dcc.Dropdown(
                id='continent-dropdown',
                options=[{'label': c, 'value': c} for c in df['continent'].unique()],
                value='Asia'
            ),
        ], style={'width': '40%', 'margin': 'auto'}),

        dcc.Graph(id='life-exp-vs-gdp'),
        dcc.Graph(id='population-bar'),
    ])