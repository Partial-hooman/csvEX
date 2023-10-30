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
    date_col = 
