from dash import Dash, dcc, html, Input, Output,callback, dash_table
from src.components import ids

def render(app):
    text_field = html.Div([
    dcc.Input(id='text-input', type='text', value='Please enter company name'),
    html.Div(id=ids.NEWS_COMPANY),
    dash_table.DateTable(id='output-data-table')
    ]
    )
    

    @app.callback(
        Output('output-data-table','data'),
        Input(ids.NEWS_COMPANY,'value'))
    
    def show_df(va)
    dcc.Input(id='text-input', type='text', value='Initial text'),
    html.Div(id=ids.NEWS_DATES)])


    this is a random test
    lets pretend this is a new feature and I am pushing it to the repo to be merged. I will then go back to the other branch and try compare the differences 
between files using this new extension. 

