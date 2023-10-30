import streamlit as st
from tab_numeric.numeric_logics import get_numeric_info 
import altair as alt

def display_numeric(df):
    num_cols = []
    for x in list(df.columns):
      try:
        n = [float(i) for i in df[x]]
        num_cols.append(x)
      except:
        pass
    col = st.selectbox('Which numeric column do you want to explore',num_cols)
    uniq_val, missing_val, n_zeroes, num_neg, avg, std, max_val, min_val, median_val, unique_vals, occurence, percntage = get_numeric_info(df[col]) 
    tble = {'Description':['Number of unique values','Number of Rows with missing values','Number of Rows with 0','Number of Rows with Negative Values','Average Value','Standard Deviation Value','Minimum Value','Median Value'],"Value":[uniq_val, missing_val, n_zeroes, num_neg, avg, std, max_val, min_val, median_val]}
    with st.expander('Numeric Column'):
         st.table(tble)
    with st.expander('Histogram chart'):
         hist = alt.Chart().mark_bar(tble).encode(x = 'Value',  y = 'count()') 
         st.altair_chart(hist)
    with st.expander('Most Frequent Values'):
         st.table({'Value':unique_vals[0:21], 'occurence':occurence[0:21], 'percentage':percntage[0:21]})
         
         
