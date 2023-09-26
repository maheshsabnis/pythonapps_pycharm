import pandas as pd

# What is a Series?
# A Pandas Series is like a column in a table.
#
# It is a one-dimensional array holding data of any type.

values = [10,20,30]

series = pd.Series(values)
# Here the result will be
# 0    10
# 1    20
# 2    30
# dtype: int64
# This means that it creates a 0-based indexes for each value in the values list
print(series)

# Noe lets create a label for each vale in the label

seriesWithLabels = pd.Series(values, index=["IT", "HRD", "SALES"])

print(f"Series with Labels \n {seriesWithLabels} \n\n")

# Create a Panda Series from the Dictionary

dictionary = {
   "Asus": 120000,
   "Apple": 240000,
   "Lenovo": 340000,
   "HP":560000
}

priceSeries = pd.Series(dictionary)

print(f"\n\nThe Series: \n\n {priceSeries}")


