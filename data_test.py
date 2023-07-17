import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Output, Input
import plotly.express as px
import pandas as pd

data = pd.read_csv("D:\Dash Plotly Dashboard/premium_bottled_water.csv")

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}])

app.layout = dbc.Container([
    dbc.Row(
        dbc.Col(html.H1("Sample Dashboard",
                        className='text-center text-primary mb-4')
                )
    ),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id='my-dpdn',
                    multi=False,
                    value='Attribute',
                    options=[{'label': x, 'value': x} for x in sorted(data['Attribute'].unique())],
                    placeholder='Year'

            )
        ], width=2),
        dbc.Col([
            dcc.Graph(id='bar-chart', figure={})

        ], width=5)
    ]),


            
    dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id='my-dpdn2',
                    multi=False,
                    value='Country',
                    options=[{'label': x, 'value': x} for x in sorted(data['Country'].unique())],
                    placeholder='Country'
                ),
                width=2,
                align='start'
            ),
        ]
    ),html.Br(),
    dbc.Row(
        [
            dbc.Col(
                dcc.Dropdown(
                    id='my-dpdn3',
                    multi=False,
                    value='Segment',
                    options=[{'label': x, 'value': x} for x in sorted(data['Segment'].unique())],
                    placeholder='Segment'
                ),
                width=2,
                align='start'
            ),
        ]
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8000)
