import pandas as pd
from tab_df.df_display import df_display
from tab_numeric.numeric_display import display_numeric
from tab_text.text_display import display_text
from tab_date.date_display import display_date
import streamlit as st
uploaded_file = st.file_uploader("Choose a CSV file")
if uploaded_file is not None:
   df = pd.read_csv(uploaded_file)
   tab1, tab2, tab3, tab4 = st.tabs(["Dataframe", "Numeric Series", "Text Series", "Datetime Series"])
   with tab1:
     df_display(df)
   with tab2:
     display_numeric(df)
   with tab3:
     display_text(df)
   with tab4:
     display_date(df)

