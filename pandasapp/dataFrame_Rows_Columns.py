# importing the pandas

import pandas as pd

companyStocks = {
    'CompanyName': ['TATA', 'Reliance', 'Mahindra', 'Bajaj'],
    'StocksVolumes':[12300, 45000, 8000, 20000],
    'CostPerVolume':[234, 5445, 1000, 400],
    'LoansInCr':[560, 120, 450, 340]
}

# create a dtaframe
df = pd.DataFrame(companyStocks)
print(df)

# Now only print 'CompanyName' and 'CostPerVolume'

print(df[[ 'CompanyName','CostPerVolume']])

# Select a specific Row using iloc() method

print(df.iloc[0])

