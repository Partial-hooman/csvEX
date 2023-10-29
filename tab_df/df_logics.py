import pandas
from datetime import datetime
from dateutil.parser import parse



def get_df_information(df):
    Num_rows = len(df)
    num_columns = len(df.columns)
    No_duplicate_rows = len(df) - len(df.drop_duplicates())
    num_missing_val = df.isnull().sum().sum()
    columns = []
    columns_dtype = []
    column_memory = list(df.memory_usage(index = False))
    for x in list(df.columns)
        try:
         n =  [float(ele) for ele in df[x]]
         Columns.append(x)
         Column_dtype.append('numeric')
        except:
         try:
          t = [parse(i) for i in df[x]]
          Columns.append(x)
          Column_dtype.append('date')
         except:
          Columns.append(x)
          Column_dtype.append('text')
     
