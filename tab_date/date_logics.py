import pandas as pd
import datetime

def get_date_info(col):
    today = datetime.datetime.now()
    uniq_val_len = len(Counter(list(col)).keys())
    missing_val = col.isna().sum()
    weekend_date_no = 0
    weekday_date_no = 0
    future_date_no = 0
    rows_with_1900_01_01 = 0
    rows_with_1970_01_01 = 0
    minima_val = min(list(col))
    maxima_val = max(list(col))
    for x in col:
        if x.weekday() < 5:
           weekday_date_no += 1
        else:
           weekend_date_no += 1
        if x > datetime.datetime.now():
           future_date_no += 1
        if  '1900-01-01' in str(x):
           rows_with_1900_01_01 += 1
        if  '1970-01-01' in str(x):
           rows_with_1970_01_01 += 1
