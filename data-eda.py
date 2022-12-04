import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import pandas as pd
from flask import Flask

# df = pd.read_csv('./data_refine/refine-error-lot-die-casting-dataset.csv', index_col=0)
df = pd.read_csv('./data_refine/refine-lot-die-casting-dataset.csv', index_col=0)

server = Flask(__name__)
app = Dash(__name__, server = server)

column_name = df.columns

error_data_column = df.columns[13 : ]
condition_column = df.columns[4: 13]
lot_column = df.columns[:4]

scatter_graph = 'scatter_graph'
scatter_dropcontainer = 'scatter_dropdown_container'
scatter_drop1 = 'error_item_dropdown'
scatter_drop2 = 'condition_dropdown'
scatter_drop3 = 'LOT_x_value_dropdown'


app.layout = html.Div(
    id = 'container',
    children = [
        dcc.Graph(
            id = scatter_graph,
        ),
        html.Div(
            id = scatter_dropcontainer,
            children = [
                html.Div(
                    id = 'error_item_container',
                    children = [
                        html.H3('에러조건 여부 선택'),
                        dcc.Dropdown(
                            id = scatter_drop1,
                            options = [{'label' : item, 'value' : item} for item in error_data_column]
                        ),
                    ]
                ),
                html.Div(
                    id = 'LOT_container',
                    children = [
                        html.H3('생산 분류 조건 선택 [x-좌표]'),
                        dcc.Dropdown(
                            id = scatter_drop3,
                            options = [{'label' : item, 'value' : item} for item in lot_column]
                        ),
                    ]
                ),
                html.Div(
                    id = 'condition_container',
                    children = [
                        html.H3('공정 조건 선택 [y-좌표]'),
                        dcc.Dropdown(
                            id = scatter_drop2,
                            options = [{'label' : item, 'value' : item} for item in condition_column]
                        ),
                    ]
                ),
            ]
        ),
    ]
)


@app.callback(
    Output(scatter_graph, 'figure'),
    Input(scatter_drop1, 'value'),
    Input(scatter_drop2, 'value'),
    Input(scatter_drop3, 'value'),
)
def scatterPlot(error_item, condition, lot_condition):
    fig = px.scatter(df, x = lot_condition, y = condition, color = error_item)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True, port = 2000)

