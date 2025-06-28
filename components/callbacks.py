# components/callbacks.py
from dash import Input, Output
import plotly.express as px

def register_callbacks(app, df):

    @app.callback(
        Output('life-exp-vs-gdp', 'figure'),
        Input('continent-dropdown', 'value')
    )
    def update_scatter(continent):
        filtered_df = df[df['continent'] == continent]
        fig = px.scatter(
            filtered_df, x="gdpPercap", y="lifeExp",
            size="pop", color="country", hover_name="country",
            log_x=True, title=f"GDP vs Life Expectancy in {continent}"
        )
        return fig

    @app.callback(
        Output('population-bar', 'figure'),
        Input('continent-dropdown', 'value')
    )
    def update_bar(continent):
        filtered_df = df[df['continent'] == continent]
        fig = px.bar(
            filtered_df, x="country", y="pop",
            title=f"Population by Country in {continent}"
        )
        return fig