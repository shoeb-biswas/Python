import numpy as np
data = [10, 12, 13 ,15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 40]
Q3 = np.percentile(data, 75)
Q1 = np.percentile(data, 25)
IQR = Q3 - Q1
print("IQR:", IQR)
lower_bound = Q1-1.5*IQR
upper_bound = Q3+1.5*IQR
print("Outlier Range:",lower_bound, "to",upper_bound)
