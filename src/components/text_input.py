from dash import Dash, dcc, html, Input, Output,callback, dash_table
from src.components import ids

def render(app):
    text_field = html.Div([


=======
    dcc.Input(id='text-input', type='text', value='Please enter company name'),
    html.Div(id=ids.NEWS_COMPANY),
    dash_table.DateTable(id='output-data-table')
    ]
    )
    

    @app.callback(
        Output('output-data-table','data'),
        Input(ids.NEWS_COMPANY,'value'))
    
    def show_df(va)
