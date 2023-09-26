# The numpy.zeros() function returns
# a new array of given shape and type, with zeros. Syntax:

import numpy as np

b = np.zeros(shape=[2,2], dtype=int)
print(b)

# Lets manipulate the datatype

c = np.zeros([2,3], dtype=[('x', float),('y', int)])
print(c)
