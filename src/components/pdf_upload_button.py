from dash import Dash, html, dcc, dash_table
from src.components import ids
import base64
from dash.dependencies import Input, Output, State
import pdftotext
import io 
import PyPDF2
from PyPDF2 import PdfReader
import fitz  # Import PyMuPDF as fitz
from src.components import clean_pdf as cp



def render(app):
    upload_button = html.Div([
                    dcc.Upload(
                    id= ids.UPLOAD_DATA_BUTTON,
                    children=html.Div([
                        'Drag and Drop or ',
                        html.A('Select Files')
                    ]),
                    style={
                        'width': '100%',
                        'height': '60px',
                        'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'margin': '2px'
                    },
                    # Allow multiple files to be uploaded
                    multiple=False
                ),
                html.Div(id=ids.OUTPUT_DATA),
                        ],
                    )


    @app.callback(
        Output(ids.OUTPUT_DATA, "children"),
        [Input(ids.UPLOAD_DATA_BUTTON, 'contents')],
        [State(ids.UPLOAD_DATA_BUTTON, 'filename')]
    )

    def update_output(contents, filename):
        if contents is not None:
            # Convert the contents (binary string) to bytes
            content_type, content_string = contents.split(',')
            decoded_pdf = base64.b64decode(content_string)

            pdf = pdftotext.PDF(io.BytesIO(decoded_pdf))
            text = ""
            for page in pdf:
                text += page
            
            df = cp.clean_pdf(text)
            data_list = df.to_dict(orient='records')












            # with fitz.open(stream=io.BytesIO(decoded_pdf), filetype="pdf") as pdf_document:
            #     for page_num in range(pdf_document.page_count):
            #         page = pdf_document.load_page(page_num)
            #         text += page.get_text()
            
            # text = [x.replace('\n',' ') for x in text]
            # Display the extracted text in a div
            return html.Div([
                html.H5(f"Extracted Text from {filename}:"),
                # html.Pre(text, style={'white-space': 'pre-wrap'})
                dash_table.DataTable(
                columns=[{'name': col, 'id': col} for col in df.columns],
                data=data_list,
                style_table={'overflowX': 'scroll'})
            ])
        else:
            return "Upload a PDF file to extract and display its text."
    
    return upload_button

