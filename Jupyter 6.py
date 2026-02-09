import numpy as np

matrix = np.arange(16).reshape(4,4)
first_row = matrix[0]
last_col = matrix[:,-1]

subarray = matrix[1:3,1:3]
print("Matrix:\n",matrix)
print("\nFirst row:",first_row)
print("\nLast column:",last_col)
print("\nCenter 2×2 subarray:\n",subarray)
