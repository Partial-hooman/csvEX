import pandas as pd
from tab_df.df_display import df_display
from tab_numeric.numeric_display import numeric_display
from tab_text.text_display import text_display
from tab_date.date_display import date_display
import streamlit as st
uploaded_file = st.file_uploader("Choose a CSV file")
if uploaded_file is not None:
   numeric_display
   tab1, tab2, tab3, tab4 = st.tabs(["Dataframe", "Numeric Series", "Text Series", "Datetime Series"])
   with tab1:
     df_display(df)
   with tab2:
     numeric_display(df)
   with tab3:
     text_display(df)
   with tab4:
     date_display(df)

