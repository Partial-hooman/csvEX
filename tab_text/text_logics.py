import pandas as pd
from statistics import mode

def get_text_column_info(col):
    uniq_val_len = len(Counter(list(col)).keys())
    missing_val = col.isna().sum()
    empty_rows = list(col).count('')
    whitespace_no = 0
    lowercase_no = 0
    uppercase_no = 0
    alphabet_no = 0
    digit_no = 0
    mode_val = mode(list(col))
    unick_vals = []
    occurences = []
    percentages = []
    for x in col:
        if x.isspace() == True:
           whitespace_no += 1
        elif x.islower() == True:
            lowercase_no += 1
        elif x.isupper() == True:
            uppercase_no += 1
        elif x.isalpha() == True:
            alphabet_no += 1
        elif x.isnumeric() == True:
            digit_no += 1 
        if x not in unick_vals:
           unick_vals.append(x)
           occurences.append(list(col).count(x))
           percentages.append((list(col).count(x)/len(list(col)))*100)
    return uniq_val_len, missing_val, empty_rows, whitespace_no, lowercase_no, uppercase_no, alphabet_no, digit_no, mode_val, unick_vals, occurences, percentages   
