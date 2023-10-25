import pandas as pd

nbaDF = pd.read_csv('./../files/nba.csv', index_col='Name')


# nbaDF.isna()

# print(nbaDF)

nbaDF.isnull()

print(nbaDF)
