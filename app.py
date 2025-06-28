import dash
from dash import Dash
from components.layout import get_layout
from components.callbacks import register_callbacks 
from utils.data_loader import load_data

## entire pipeline to create the page

## load and store the data
df = load_data()

## initialize the app
app = Dash(__name__)
app.title = "Global Indicators Dashboard"
app.layout = get_layout(df)

## register the callbacks
register_callbacks(app, df)

if __name__ == "__main__":
    app.run(debug=True)



