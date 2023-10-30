import streamlit as st
from tab_date.date_logics import get_date_info 
import altair as alt
import pandas as pd

def display_date(df):
    date_cols = []
    for x in list(df.columns):
      try:
        n = [float(i) for i in df[x]]
        num_cols.append(x)
      except:
        pass
