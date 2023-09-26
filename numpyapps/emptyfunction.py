# The Empty functions accepts parameters as
# -> shape : Number of rows
# -> order : C_contiguous or F_contiguous
# -> dtype : [optional, float(by Default)] Data type of returned array.

import numpy as np

b = np.empty(2, dtype=int)

print(b) # This will show an array with random values

# Creating Array with 2 rows and 2 columns

c = np.empty([2,2], dtype=int)
print(c)
