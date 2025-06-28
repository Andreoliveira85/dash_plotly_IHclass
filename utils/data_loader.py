import pandas as pd
import plotly.express as px

def load_data():
    df = px.data.gapminder()
    return df[df.year == 2007]


