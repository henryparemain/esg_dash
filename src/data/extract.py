from dash import Dash, html, dcc
from src.components import ids
from dash.dependencies import Input, Output
import io 
import pdftotext
import subprocess
import pandas as pd
import base64
from src.components import clean_pdf as cp

def convert_text_to_df(text: str) -> pd.DataFrame:
    #split text into paragraphs
    raw_text = text.split('\n\n')
    # replacing any new line characters within a string with a space
    raw_text = [x.replace('\n',' ') for x in raw_text]
    # remove any strings which have less than 10 words (headers etc and thus just noise)
    raw_text = [x for x in raw_text if len(x.split())>10]
    # putting raw paragraphs into a row of a dataframe
    df_raw = pd.DataFrame(raw_text)
    df_raw = df_raw.rename(columns = {0:'raw_paras'})
    return df_raw

def split_cell_at_bullets(df: pd.DataFrame) -> pd.DataFrame:
    list_of_strings = list(df.iloc[:,0])
    bullet_point_character = '•'  # Update this with the desired bullet point character
    new_list_of_sentences = []
    for sentence in list_of_strings:
        if bullet_point_character in sentence:
            sentence_split = sentence.split(bullet_point_character)
            for new_sentence in sentence_split:
                new_list_of_sentences.append(new_sentence)
        else:
            new_list_of_sentences.append(sentence)
    return new_list_of_sentences


def extract_text_from_pdf(text):
    df = convert_text_to_df(text)
    df = pd.DataFrame(split_cell_at_bullets(df))
    return df 

