import streamlit
from df_logics import get_df_information
import pandas

def df_display(df):
    num_rows, num_columns, no_duplicate_rows, num_missing_val, columns, columns_dtype, column_memory = 
