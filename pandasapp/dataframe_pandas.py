# DataFrame
# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
#
# Series is like a column, a DataFrame is the whole table.

import pandas as pd

data = {
    'Products': ["Laptop", "Mobiles", "Fashion", "Cosmetics"],
    'Sales': [400, 230, 800, 5000]
}

# Create a DataFrame
salesDataFrame = pd.DataFrame(data)

print(salesDataFrame)

# Read a specific row from the dataframe

print(f"The 2nd row from salesDataFrame \n\n{salesDataFrame.loc[1]}")

# Lets the first 2 rows


print(f"The first 2 rows from salesDataFrame \n\n{salesDataFrame.loc[[0,1]]}")

# Now lets set names to each index in DataFrame

salesDataFrameWithIndexes = pd.DataFrame(data, index=["Computer", "Phone", "Fashion-Items", "Cosmetics-Items"])

print(f"DataFrame with names to \n\n {salesDataFrameWithIndexes}")

# Now lets print a row with specific name
print(f"The 3rd row in Names DataFrame {salesDataFrameWithIndexes.loc['Phone']}")
