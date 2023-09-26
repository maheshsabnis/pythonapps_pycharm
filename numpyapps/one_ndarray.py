# Python program for
# install numpy
    # pip install numpy
# Creation of Arrays
import numpy as np

# Define an array
# This is an array with the rank 1
arr = np.array([10,20,30])

print(arr)

# Define array with 2 Ranks
arr = np.array([
    [1,2,3,4,5,6],
    [10,20,30,40,50,60]
])

print (arr)

# Defining two arrays

arr1 = np.array([10,20])
arr2 = np.array([10,20])
# This will multiply each element by its index
print(arr1 * arr2)

# Each rank must have the same dimension
arr3 = np.array([[9,8,7],[2,3,1]])
print(arr3)

# Create an array using the Tuple

arr4=np.array((10,20,40))
print(arr4)

# Defining a complex array

arr5 = np.array([
    [10,20,30,40],
    [100,200,300,400],
    [1,2,3,4],
    [20,40,60,80],
    [10,30,50,70],
    [200,400,600,800],
    [100,300,500,700]
])
# Show first 2 Ranks (means first 2 arrays)
print(f"Slice an array to see First 2 ranks {arr5[:2]}")

# Show first 2 Ranks (means first 2 arrays) and an alternative elements in each ranks
print(f"Slice an array to see First 2 ranks and an alternative element in each rank {arr5[:2, ::2]}")
