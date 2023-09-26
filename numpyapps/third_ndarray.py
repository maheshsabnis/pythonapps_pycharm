import numpy as np
# Defining an array

arr1 = np.array([
    [1,0,1,0],
    [10,20,30,40],
    [100,200,300,400],
    [1,2,3,4],
    [20,40,60,80],
    [10,30,50,70],
    [200,400,600,800],
    [100,300,500,700],
    [0, 12, 1, 0]
])

print(f"Return the indices of the elements that are non-zero : {np.nonzero(arr1)}")
