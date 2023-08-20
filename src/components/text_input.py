from dash import Dash, dcc, html, Input, Output,callback
from src.components import ids

def render(app):
    text_field = html.Div([
    dcc.Input(id='text-input', type='text', value='Initial text'),
    html.Div(id=ids.NEWS_DATES)])


    this is a random test
    lets pretend this is a new feature and I am pushing it to the repo to be merged. I will then go back to the other branch and try compare the differences 
between files using this new extension. 

