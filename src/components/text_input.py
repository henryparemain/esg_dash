from dash import Dash, dcc, html, Input, Output,callback
from src.components import ids

def render(app):
    text_field = html.Div([
    dcc.Input(id='text-input', type='text', value='Initial text'),
    html.Div(id=ids.NEWS_DATES)])