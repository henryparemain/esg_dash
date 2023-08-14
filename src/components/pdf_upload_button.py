from dash import Dash, html, dcc, dash_table
from src.components import ids
import base64
from dash.dependencies import Input, Output, State
import pdftotext
import io 
from src.components import clean_pdf as cp
from src.data import extract as ex
from src.data import esg_bert as eb
from src.components import dropdown as dd
import random 
import pandas as pd



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
                dcc.Store(id = ids.OUTPUT_DATA_PDF),
                # dash_table.DataTable(id=ids.OUTPUT_DF)
                html.Div(id = ids.OUTPUT_DF)
            
                 ],
                    )


    @app.callback(
        # Output(ids.OUTPUT_DF, 'data'),
        Output(ids.OUTPUT_DATA_PDF,'data'),
        Input(ids.UPLOAD_DATA_BUTTON, 'contents') 
    )

    def update_output(pdf_contents):
        if pdf_contents is not None:
            # Convert the contents (binary string) to bytes
            content_type, content_string = pdf_contents.split(',')
            decoded_pdf = base64.b64decode(content_string)
            # extract text from pdf 
            pdf = pdftotext.PDF(io.BytesIO(decoded_pdf))
            text = []
            for page in pdf:
                text.append(page)
            
            # list of extracted sentences 
            list_of_cleanish_sentences = ex.extract_text_from_pdf(text)
            scored_df = eb.score_sentences_put_in_df(list_of_cleanish_sentences)
            scored_df = scored_df.to_dict('records')
        
            return scored_df
        
    # uncomment the below callback if you want to see the logic of using Store to store the dataframe and then retrieve it again. 
        
    # @app.callback(
    #     Output(ids.OUTPUT_DF,'data'),
    #     Input(ids.OUTPUT_DATA_PDF,'data')
    #  )
    # def show_df(df):
    #     return df
        
    @app.callback(
    Output(ids.OUTPUT_DF, 'children'),
    Input(ids.OUTPUT_DATA_PDF, 'data'),
<<<<<<< HEAD
    Input(ids.DROPDOWN_INPUT,'value')
    )

    def filter_df(df, filtered_metric):
       df = pd.DataFrame(df)
       max_row = df[filtered_metric].argmax()
       sentence = df.loc[max_row,'sentence']
       return sentence
=======
    Input(ids.DROPDOWN_INPUT,'value'),
    Input(ids.SLIDER, 'value')
    )

    def filter_df(df, filtered_metric, num_of_sentences):
       df = pd.DataFrame(df)
       sorted_df = df.sort_values(by=filtered_metric, ascending=False)
       top_n_rows = sorted_df.head(num_of_sentences)
       top_n_sentences = list(top_n_rows['sentence'])
    #    top_n_values_column = df[filtered_metric].nlargest(num_of_sentences)
    #    max_row = df[filtered_metric].argmax()
    #    sentence = df.loc[max_row,'sentence']
       formatted_sentences = '\n\n'.join(top_n_sentences)  # Add double line breaks between sentences
       return dcc.Markdown(formatted_sentences)
>>>>>>> a9a9cbf8e2a39e5503da33c9ee19c71ae88602b8

    # def dummy_callback(_):
    #     return None

        

    # @app.callback(
    #     Output(ids.DROPDOWN_OUTPUT,"children"),
    #     Input(ids.OUTPUT_DATA_PDF, 'children'),
    #     Input(ids.DROPDOWN_INPUT, 'value'),
    #     Input('dummy-output', 'children')  # Added dependency here
    #     )

    # def filter_df(df, filtered_metric, _):
    #     filtered_metric = filtered_metric
    #     df = df
    #     max_row = df[filtered_metric].argmax()
    #     sentence = df.loc[max_row,'sentence']
    #     return sentence
    
    return upload_button

