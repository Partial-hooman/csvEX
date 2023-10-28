import streamlit as st
uploaded_file = st.file_uploader("Choose a CSV file")
if uploaded_file is not None:
   tab1, tab2, tab3, tab4 = st.tabs(["Dataframe", "Numeric Series", "Text Series", "Datetime Series"])
   with tab1:
     pass
