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
    unic_vals = []
    occurencess = []
    percentagess = []
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
        if x not in unic_vals:
           unic_vals.append(x)
           occurencess.append(list(col).count(x))
           percentagess.append((list(col).count(x)/len(list(col)))*100)
            
    return uniq_val_len, missing_val, weekend_date_no, weekday_date_no, future_date_no, rows_with_1900_01_01, rows_with_1970_01_01, minima_val, maxima_val, unic_vals, occurencess, percentagess
