import numpy as np
data = [10, 12, 13 ,15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 40]
print("25th percentile Q1:", np.percentile(data, 25))
print("50th percentile Median:", np.percentile(data, 50))
print("75th percentile Q3:", np.percentile(data, 75))
