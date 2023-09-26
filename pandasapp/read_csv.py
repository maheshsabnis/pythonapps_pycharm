# Read CSV Files
# A simple way to store big data sets is to use CSV files (comma separated files).
#
# CSV files contains plain text and is a well know format that can be read by everyone including Pandas.
#
# In our examples we will be using a CSV file called 'data.csv'.

import pandas as pd
# Print total number of records
print(f"Number of records {pd.options.display.max_rows}")

# The default of max_rows is 60, we can increase it
pd.options.display.max_rows =  42000
print(f"Number of records {pd.options.display.max_rows}")
# Read the File
df = pd.read_csv('./../DataSets_Dw/annual-enterprise-survey-2021-financial-year-provisional-csv.csv')

print(df.to_string())


