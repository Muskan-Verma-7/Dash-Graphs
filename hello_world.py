from dash import Dash, dcc, Output, Input
import dash_bootstrap_components as dbc

#Component
app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
mytext = dcc.Markdown(children = '')
myinput = dbc.Input(value="Hi There")

#Customize layout
app.layout = dbc.Container([mytext,myinput])

#Callback allows to interact
@app.callback(
    Output(mytext, component_property='children'),
    Input(myinput, component_property='value')
)

def update_title(user_input): 
    return user_input




#Run App
if __name__ == '__main__':
    app.run_server()