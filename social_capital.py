from dash import Dash, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc

df = pd.read_csv("https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Good_to_Know/Dash2.0/social_capital.csv")

app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])
mytitle = dcc.Markdown(children='')

mygraph = dcc.Graph(figure={})
dropdown = dcc.Dropdown(options= df.columns.values[2:],
                        value = 'Cesarean Delivery Rate',
                        clearable=False)

#Customize layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([mytitle], width=6)
    ], justify='center'),
    dbc.Row([
        dbc.Col([mygraph], width=6),
        dbc.Col([dropdown], width=6)
    ]),
], fluid=True)

#Callback components
@app.callback(
    Output(mygraph, 'figure'),
    Output(mytitle, 'children'),
    Input(dropdown, 'value')
)

def update_graph(column_name):

    fig = px.line(data_frame=df,
                        x='YEAR',y=column_name,
                        color='STATE',
                        )
    return fig, '# '+column_name

# Run app
if __name__=='__main__':
    app.run_server(debug=True, port=8054)