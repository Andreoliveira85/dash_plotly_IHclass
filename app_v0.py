import dash
import pandas as pd
from dash import dcc, html, Input, Output
import plotly.express as px


## data loader
df = px.data.gapminder()
df = df[df.year ==2007]

## initialize the Dash app
app = dash.Dash(__name__)
app.title = "Global Indicators Dashboard"

## create the layout

app.layout = html.Div([
    html.H1("Global Indicators Dashboard", style={'textAlign': 'center'}),
    
    html.Label("Select a Continent:"),
    dcc.Dropdown(
        id='continent-dropdown',
        options=[{'label': c, 'value': c} for c in df['continent'].unique()],
        value='Asia'
    ),
    
    dcc.Graph(id='life-exp-vs-gdp'),
])

## add interactivity (callback decorators)
@app.callback(
    Output('life-exp-vs-gdp', 'figure'),
    Input('continent-dropdown', 'value')
)
def update_graph(selected_continent):
    filtered_df = df[df['continent'] == selected_continent]
    fig = px.scatter(
        filtered_df,
        x="gdpPercap", y="lifeExp",
        size="pop", color="country",
        hover_name="country", log_x=True,
        title=f"GDP vs Life Expectancy in {selected_continent}"
    )
    return fig


if __name__ =="__main__":
    app.run(debug=True)