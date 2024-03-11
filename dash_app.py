import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Cálculo Estoque'),

    dcc.Graph(id='graph1'),
    dcc.Graph(id='graph2'),

    html.Div(id='output'),

    dcc.Interval(
        id='interval-component',
        interval=1*1000, # in milliseconds
        n_intervals=0
    )
])

@app.callback(
    Output('graph1', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph1(n):
    with open('data.txt', 'r') as f:
        stock, sold_per_day, sold_per_month = map(int, f.read().split(','))

    figure = {
        'data': [
            {'labels': ['Estoque Inicial', 'Vendido por Mês'], 'values': [stock, sold_per_month], 'type': 'pie'}
        ],
        'layout': {
            'title': 'Estoque vs Vendas'
        }
    }

    return figure

@app.callback(
    Output('graph2', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph2(n):
    with open('data.txt', 'r') as f:
        stock, sold_per_day, sold_per_month = map(int, f.read().split(','))

    figure = {
        'data': [
            {'labels': ['Estoque Inicial', 'Vendido por Dia'], 'values': [stock, sold_per_day], 'type': 'pie'}
        ],
        'layout': {
            'title': 'Estoque vs Vendas Diárias'
        }
    }

    return figure

@app.callback(
    Output('output', 'children'),
    Input('interval-component', 'n_intervals')
)
def update_output(n):
    with open('data.txt', 'r') as f:
        stock, sold_per_day, sold_per_month = map(int, f.read().split(','))

    # Calcular a porcentagem de estoque que precisa ser reabastecido
    replenish_percentage = (stock - sold_per_month) / stock * 100

    output = f'Você precisa reabastecer {replenish_percentage}% do seu estoque.'

    return output

if __name__ == '__main__':
    app.run_server(debug=True)