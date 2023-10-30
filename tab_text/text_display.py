import streamlit as st
from tab_text.text_logics import get_text_info 
import altair as alt

def display_text(df):
    text_cols = [ col  for col, dt in df.dtypes.items() if dt == object]
    text_Col = st.selectbox('Which text column do you want to explore',text_cols)
    uniq_val_len, missing_val, empty_rows, whitespace_no, lowercase_no, uppercase_no, alphabet_no, digit_no, mode_val, unick_vals, occurences, percentages = get_text_info(text_Col)
    text_tble = {'Description':['Number of Unique Values','Number of Rows with Missing Values','Number of Empty Rows','Number of Rows with Only Whitespace','Number of Rows with Only Lowercases','Number of Rows with Only Uppercases','Number of Rows with Only Alphabet','Number of Rows with Only Digits','Mode Value'],'Value':[uniq_val_len, missing_val, empty_rows, whitespace_no, lowercase_no, uppercase_no, alphabet_no, digit_no, mode_val]}
    with st.expander('Text Column'):
         st.table(text_tble)
    with st.('Bar Chart'):
         bar = alt.Chart().mark_bar({'Value':unick_vals, 'occurence':occurences}).encode(x = 'Value',  y = 'occurence')
         st.altair_chart(bar)
    with st.('Most Frequent Values'):
         st.table({'Value':unick_vals[0:21], 'occurence':occurences[0:21], 'percentage':percntages[0:21]})
