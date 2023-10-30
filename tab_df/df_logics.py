import pandas
from datetime import datetime
from dateutil.parser import parse



def get_df_information(df):
    num_rows = len(df)
    num_columns, = len(df.columns)
    no_duplicate_rows = len(df) - len(df.drop_duplicates())
    num_missing_val = df.isnull().sum().sum()
    columns = []
    columns_dtype = []
    column_memory = list(df.memory_usage(index = False))
    for x in list(df.columns):
        try:
         n =  [float(ele) for ele in df[x]]
         df[x] = n
         columns.append(x)
         column_dtype.append('numeric')
        except:
         try:
          t = [parse(i) for i in df[x]]
          df[x] = t
          columns.append(x)
          column_dtype.append('date')
         except:
          columns.append(x)
          column_dtype.append('text')
    return num_rows, num_columns, no_duplicate_rows, num_missing_val, columns, columns_dtype, column_memory 
