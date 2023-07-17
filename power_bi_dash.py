import dash
from dash import Dash, html, dcc, Output, Input, dash_table, callback   # pip install dash
import dash_bootstrap_components as dbc                                  # pip install dash-bootstrap-components
import plotly.express as px
import pandas as pd
import numpy as np

#app = Dash(__name__, external_stylesheets= [dbc.themes.LUMEN, dbc.icons.FONT_AWESOME])
#server = app.server()

df = pd.read_csv('https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Analytic_Web_Apps/Flights_Analysis/europe-flights-reduced.csv')
#df['Year'] = df['Year'].astype(str)
print(df.head(10))

def create_table(data):
    # pivot table
    pbc = data.groupby(['GEO','PARTNER'])['Value'].sum().reset_index()
    pbc = pbc.pivot(index='GEO', columns='PARTNER')['Value'].reset_index()
    pbc = pbc[pbc['GEO'].isin(['Allemagne','Espagne','France','Grèce','Italie',
                               'Pays-Bas','Portugal','Royaume-Uni','Suisse','Turquie'])]
