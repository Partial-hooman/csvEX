import streamlit
from df_logics import get_df_information
import pandas

def df_display(df):
    num_rows, num_columns, no_duplicate_rows, num_missing_val, columns, columns_dtype, column_memory = get_df_information(df) 
    with st.expander('Dataframe'):
         table = {'Description':['Number of Rows','Number of columns','Number of Duplicate Rows','Number of Rows with Missing Values'],'Value':[num_rows, num_columns, no_duplicate_rows, num_missing_val]}
         st.table(table)
    with st.expander('Columns'):
         table2 = {'column':columns,'Data_type':columns_dtype,'memory':column_memory}
         st.table(table2)
    with st.expander('Explore Dataframe'):
         rows = st.slider('Select the number of rows to be displayed',min_value=5,max_value=50)
         method = st.radio('Exploration Method',['Head','Tail','Sample'])
