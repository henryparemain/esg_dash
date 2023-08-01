from dash import Dash, html, dcc
from src.components import pdf_upload_button
from src.data import extract




def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Small('Upload an ESG report of your choosing'),
            pdf_upload_button.render(app)
        ]
    )



