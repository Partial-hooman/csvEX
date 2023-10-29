import pandas

def get_numeric_info(col):
  uniq_val = len(Counter(col).keys())
  missing_val = col.isna().sum()
  values = [float(n) for n in col]
  for x in col:
      if x ==    
