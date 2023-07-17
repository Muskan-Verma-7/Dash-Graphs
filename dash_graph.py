from dash import Dash, dcc, Output, Input  # pip install dash
import dash_bootstrap_components as dbc    # pip install dash-bootstrap-components
import plotly.express as px
import dash_mantine_components as dmc

# data source
df = px.data.medals_long()

#Build Components of App
app = Dash(__name__, external_stylesheets=[dbc.themes.VAPOR])
mytitle = dcc.Markdown(children='# Analyzing Olympic Medals')
alert = dmc.Alert(children='')
mygraph = dcc.Graph(figure={})
dropdown = dcc.Dropdown(options=['Bar Plot','Scatter Plot'],
                    value='Bar Plot',
                    clearable=False)

#Customizing Layout
app.layout = dbc.Container([mytitle, mygraph, dropdown])

@app.callback(
    Output(mygraph, component_property='figure'),
    Output(alert, 'children'),
    Input(dropdown, component_property='value')
)

def update_graph(user_input):
    if user_input == 'Bar Plot':
        fig = "The data for the bar graph is highly confidential."

    elif user_input == 'Scatter Plot':
        fig = "The scatter plot is believed to have been first published in 1833"

    return fig     # returned objects are assigned to the component property of the Output

# Run app
if __name__=='__main__':
    app.run_server()