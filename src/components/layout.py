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
<<<<<<< HEAD
=======
            dcc.Slider(
            id=ids.SLIDER,
            min=1,
            max=10,
            step=1,
            value=5,  # Initial value
            marks={i: str(i) for i in range(1, 11)}),
>>>>>>> a9a9cbf8e2a39e5503da33c9ee19c71ae88602b8
            html.Div(style={"margin-top": "20px"}),
            html.Small('Choose an SASB metric to explore'),
            dropdown.render(app),
            html.Div(id = ids.DROPDOWN_OUTPUT),

                    ]
    )



