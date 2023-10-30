import pandas as pd
import statistics
def get_numeric_info(col):
  uniq_val_len = len(Counter(list(col)).keys())
  missing_val = col.isna().sum()
  values = [float(n) for n in col]
  n_zeroes = 0
  num_neg = 0
  for x in values:
      if x == 0:
        n_zeroes = n_zeroes + 1
      elif x < 0:
        num_neg = num_neg + 1
  avg=sum(values)/len(values)
  std=statistics.stdev(values)
  max_val=max(values)
  min_val=min(values)
  median_val=statistics.median(values)
  unique_vals = Counter(list(col)).keys()
  occurence = []
  percntage = []
  for x in unique_vals:
      occurence.append(list(col).count(x))
      percntage.append((list(col).count(x)/len(list(col)))*100)
      
  
  return uniq_val, missing_val, n_zeroes, num_neg, avg, std, max_val, min_val, median_val, unique_vals, occurence, percntage
