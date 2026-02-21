# Reduce & Lambda Function
from functools import reduce
lst = [847, 73,3, 43, 3,24,50]
sumation = reduce(lambda x,y: x+y, lst)
print(sumation)

from functools import reduce
lst = [847, 73,3, 43, 3,24,50]
max_val = reduce(lambda x,y:x if x>y else y,lst )
print(max_val)

import numpy as np
arr1 = np.array([1,2,3])
print(arr1.dtype)

import numpy as np
arr1 = np.array([1,3,5]) #1D array
arr2 = np.array([[2,6,5],[3,8,1]]) #2D array
arr3 = np.array([[[2,4,6]],[[9,7,4]]]) #3D array
