import pandas as pd

# Indexing

## Indexing and Selecting Data

## Indexing in pandas means simply
# selecting particular rows and columns of data from a DataFrame.
# Indexing could mean selecting all the rows and some of the columns,
# some of the rows and all of the columns, or some of each of the rows
# and columns. Indexing can also be known as Subset Selection.

nbaDF = pd.read_csv('./../files/nba.csv', index_col='Name')

print(nbaDF)

# Read Specific Rows using loc() function

row1 = nbaDF.loc['Jae Crowder']
row2 = nbaDF.loc['Sergey Karasev']

# Select a Single Column Data.
# This will show the Index Column Values and selected column Data

collageData = nbaDF["College"]

print(collageData)




print(f'Row1 1 {row1} and Row 2 {row2}')


