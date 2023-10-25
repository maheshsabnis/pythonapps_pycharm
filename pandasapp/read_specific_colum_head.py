
import pandas as pd
df = pd.read_csv('./../DataSets_Dw/annual-enterprise-survey-2021-financial-year-provisional-csv.csv')
# The column Name
series = df[["Variable_name","Variable_code", "Value"]]

# read first 5 records

data = series.head(5)

print(data)
