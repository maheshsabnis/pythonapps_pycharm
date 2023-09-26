import numpy as np
# Defining an array

arr1 = np.array([
    [10,20,30,40],
    [100,200,300,400],
    [1,2,3,4],
    [20,40,60,80],
    [10,30,50,70],
    [200,400,600,800],
    [100,300,500,700]
])

# Modify each element by adding 10 to each record in each rank

print(arr1 + 10)

# Sum the array

print(arr1.sum())

# Print the Dimension of the array

print(f"Dimensions are {arr1.ndim}")

# Shape of the array

print(f"Shape of the array {arr1.shape}")

# Total Number of Elements

print(f"Total Number of elements in array are {arr1.size}")

# Datatype of elements in array

print(f"Data Type of elements in array {arr1.dtype}")
# Python buffer object pointing to the start of the array's data.
print(f"Data = {arr1.data}")
# Size of each item (8 bytes)
print(f"Size of each element of array {arr1.itemsize}")
# Return an element from array based on index
print(arr1.item(10))

# Insert scalar into an array
# insert value in 3rd rank (starts from 0) at 2nd index actually at 3rd position (index starts from 0)
arr1.itemset((3,2),  1000)

print(arr1)

# Max amd min

print(f"Max value element : {arr1.max()} "
      f"and Min value element : {arr1.min()} ")

# the Max element's index is
print(np.where(arr1 == arr1.max())[0][0])

print(arr1[3][2])

# the Min element's index is
print(np.where(arr1 == arr1.min())[0][0])

# Average of all Elements in Array

print(f" Average of elements:  {arr1.mean()}")


