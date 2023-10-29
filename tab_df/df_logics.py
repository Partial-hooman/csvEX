import pandas
from datetime import datetime
from dateutil.parser import parse



def get_df_information(df):
    Number_of_Rows = len(df)
    Number_of_Columns = len(df.columns)
    Number_of_Duplicated_Rows = len(df) - len(df.drop_duplicates())
    Number_of_Rows_with_Missing_Values = df.isnull().sum().sum()
    Columns = []
    Column_dtype = []
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
     
