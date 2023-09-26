# importing pandas

import pandas as pd

# creating a dictionary

mydataset = {
    'Laptops':['HP', 'Lenovo', 'Accer', 'Asus', 'Apple'],
    'Price':[100000,300000,400000,4500000, 4700000]
}

# create a frame

myDataFrame = pd.DataFrame(mydataset)

print(myDataFrame)

# print the version

print(pd.__version__)



