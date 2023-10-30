import streamlit as st
from tab_text.text_logics import get_text_info 
import altair as alt

def display_text(df):
    cols = [ col  for col, dt in df.dtypes.items() if dt == object]
    uniq_val_len, missing_val, empty_rows, whitespace_no, lowercase_no, uppercase_no, alphabet_no, digit_no, mode_val, unick_vals, occurences, percentages = get_text_info()
    
