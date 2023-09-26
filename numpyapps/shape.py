# The numpy.reshape() function shapes an array without
# changing the data of the array.

import numpy as np

arr1 = np.arange(10)
print(arr1)
# reshape the arr1 in 2 rows and 5 columns
arr2 = arr1.reshape(2,5)
print(arr2)

arr3 = arr1.reshape(3,3,3) # This will give error because thw original array has only 10 elements and here the
# reshaping is excedding it
print(arr3)

