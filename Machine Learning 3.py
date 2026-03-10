import numpy as np
data = np.array([10, 12, 13 ,15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 40])

mean = np.mean(data)
std = np.std(data)

z_scores = [(x-mean)/ std for x in data]
print("z_scores:", np.round(z_scores, 2))
