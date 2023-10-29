import streamlit as st
from tab_numeric.numeric_logics import get_numeric_info 

def display_numeric(df):
    num_cols = []
    for x in list(df.columns):
      try:
        n = [float(i) for i in df[x]]
        num_cols.append(x)
      except:
        pass
    col = st.selectbox('Which numeric column do you want to explore',num_cols)
    uniq_val, missing_val, n_zeroes, num_neg, avg, std, max_val, min_val, median_val = get_numeric_info(df[col]) 
    tble = {'Description':['Number of unique values','Number of missing values']}
