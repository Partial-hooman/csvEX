import pandas
import statistics
def get_numeric_info(col):
  uniq_val = len(Counter(col).keys())
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