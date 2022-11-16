import plotly
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import pandas as pd
from flask import Flask

df = pd.read_csv("./data/die-casting_dataset.csv")

server = Flask(__name__)
app = Dash(__name__, server = server)

column_name = df.columns

error_data_column = df.columns[10 : ]
condition_column = df.columns[1: 10]


scatter_graph = 'scatter_graph'
scatter_dropcontainer = 'scatter_dropdown_container'
scatter_drop1 = 'scatter_drop1'
scatter_drop2 = 'scatter_drop2' 



app.layout = html.Div(
    id = 'container',
    children = [
        dcc.Graph(
            id = scatter_graph,
        ),
        html.Div(
            id = scatter_dropcontainer,
            children = [
                dcc.Dropdown(
                    id = scatter_drop1,
                    options = [{'label' : item, 'value' : item} for item in error_data_column]
                ),
                dcc.Dropdown(
                    id = scatter_drop2,
                    options = [{'label' : item, 'value' : item} for item in condition_column]
                )
            ]
        ),
    ]
)

@app.callback(
    Output(scatter_graph, 'figure'),
    Input(scatter_drop1, 'value'),
    Input(scatter_drop2, 'value')
)
def scatterPlot(drop1 , drop2):
    fig = px.scatter(df, x = drop1, y = drop2)
    return fig



if __name__ == '__main__':
    app.run_server(debug=True)


