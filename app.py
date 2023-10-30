import pandas as pd
from tab_df.df_display import df_display
import streamlit as st
uploaded_file = st.file_uploader("Choose a CSV file")
if uploaded_file is not None:
   tab1, tab2, tab3, tab4 = st.tabs(["Dataframe", "Numeric Series", "Text Series", "Datetime Series"])
   with tab1:
     df = pd.read_csv(uploaded_file)
     df_display(df)
   with tab2:
     pass
   with tab3:
     pass
   with tab4:
     pass

