from dash import Dash, html, dcc
from src.components import pdf_upload_button
from src.data import extract
from src.components import dropdown
from src.components import ids 



def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Small('Upload an ESG report of your choosing'),
            pdf_upload_button.render(app),
            html.Div(style={"margin-top": "20px"}),
            html.Small('Choose an SASB metric to explore'),
            dropdown.render(app),
            html.Div(id = ids.DROPDOWN_OUTPUT),

                    ]
    )



