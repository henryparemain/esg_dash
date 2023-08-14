from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP
from dash import Dash, html, dcc, dash_table
from dash.dependencies import Input, Output, State
from src.components import ids
from src.components.layout import create_layout
import pandas as pd

app = Dash(external_stylesheets=[BOOTSTRAP])
df = pd.read_csv('./data/mosquito_data.csv')

def render(app):
    dropdown = html.Div([
        dcc.Dropdown(
        options=['Year','Week','Block'],
        value=None,
        placeholder="Show all columns", id='dropdown-selection')
            ])
    
    @app.callback(
        Output('output-table','children'),
        Input('dropdown-selection','value'),
        State('dropdown-selection', 'options')
    )

    def filter_df(dropdown_selection, dropdown_options):
        if dropdown_selection is None:
            selected_df = df
        else:
            selected_df = df[dropdown_selection]

            
        table = html.Table([
        html.Thead(html.Tr([html.Th(dropdown_selection)])),
        html.Tbody([html.Tr([html.Td(data)]) for data in selected_df])
        ])
        

        return table
    
    return dropdown


app.layout = html.Div([
    html.H1("DF TEST"),
    render(app),
    html.Div(id='output-table')
])

if __name__ == '__main__':
    app.run()
