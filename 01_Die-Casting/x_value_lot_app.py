import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = pd.read_csv('die-casting_dataset.csv')
drop_menu = df.columns[1:10]

app = Dash(__name__)

app.layout = html.Div(
    className = 'container',
    children = [
        dcc.Graph(id = 'graph'),
        dcc.Dropdown(drop_menu, id = 'dropdown')
    ]
)

@app.callback(
    Output('graph', 'figure'),
    Input('dropdown', 'value')
)
def show_graph(input):
    fig = px.scatter(df, x = 'LOT', y = input)
    return fig


app.run_server(debug = True, port = 3000)