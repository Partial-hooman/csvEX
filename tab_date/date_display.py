import streamlit as st
from tab_date.date_logics import get_date_info 
import altair as alt
import pandas as pd
from datetime import datetime
from dateutil.parser import parse

def display_date(df):
    date_cols = []
    for x in list(df.columns):
      try:
        dt = [parse(d) for d in df[x]]
        date_cols.append(x)
      except:
        pass
    date_col = st.selectbox('Which date column do you want to explore',date_cols)
    uniq_val_len, missing_val, weekend_date_no, weekday_date_no, future_date_no, rows_with_1900_01_01, rows_with_1970_01_01, minima_val, maxima_val, unic_vals, occurencess, percentagess = get_date_info(date_col)
    dt_table = {'Description':['Number of Unique Values','Number of Rows with Missing Values','Number of Weekend Dates','Number of Weekday Dates','Number of Dates in Future','Number of Rows with 1900-01-01','Number of Rows with 1970-01-01','Minimum Value','Maximum Value'],'Values':[uniq_val_len, missing_val, weekend_date_no, weekday_date_no, future_date_no, rows_with_1900_01_01, rows_with_1970_01_01, minima_val, maxima_val]}
    with st.expander('Date Column'):
        st.table(dt_table)
    with st.expander('Histogram Chart'):
        hist1 = alt.Chart().mark_bar(dt_table).encode(x = 'Values',  y = 'count()') 
        st.altair_chart(hist1)
    with st.expander('Most Frequent Values'):
        
