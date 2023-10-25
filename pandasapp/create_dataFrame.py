# importing the pandas

import pandas as pd

# define the array

list = ["Tejas", "Mahesh", "Ramesh", "Ram", "Gundaram"]

# Create a DataFrame
df = pd.DataFrame(list)

print(df)

# create dataframe from the dictionary

companyStocks = {
    'CompanyName': ['TATA', 'Reliance', 'Mahindra', 'Bajaj'],
    'StocksValumes':[12300, 45000, 8000, 20000]
}

# create a dtaframe
df = pd.DataFrame(companyStocks)
print(df)




