from dash import Dash, html, dcc
from src.components import ids
from dash.dependencies import Input, Output
import io 
import pdftotext
import subprocess
import pandas as pd
import base64
from src.components import clean_pdf as cp

def split_cell_at_bullets(cell: pd.DataFrame) -> pd.DataFrame:
    


def extract_text_from_pdf(uploaded_file):
    pdf_data = io.BytesIO(uploaded_file.read())
    # Use pdftotext to extract the text from the PDF file
    result = subprocess.run(["pdftotext", "-", "-"], input=pdf_data.getvalue(), capture_output=True)
    # Convert the result from bytes to a string and display it to the user
    text = result.stdout.decode("utf-8")
    df = cp.clean_pdf(text)
    return df 

