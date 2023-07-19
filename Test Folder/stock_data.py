import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Output, Input
import plotly.express as px
import pandas as pd
import pandas_datareader.data as web
import datetime


# https://stooq.com/
start = datetime.datetime(2020, 1, 1)
end = datetime.datetime(2020, 12, 3)
df = web.DataReader(['AMZN','GOOGL','FB','PFE','MRNA','BNTX'],
                    'stooq', start=start, end=end)
# df=df.melt(ignore_index=False, value_name="price").reset_index()
df = df.stack().reset_index()
print(df[:15])
print(type(df))

app = dash.Dash(__name__, external_stylesheets= dbc.themes.BOOTSTRAP,
                meta_tags= [{'name' : 'viewport',
                             'content' : 'width=device-width,initial-scale=1.0'}])



