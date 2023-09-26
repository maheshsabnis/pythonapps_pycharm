# The numpy.linspace() function returns number spaces evenly w.r.t interval.

# numpy.linspace(start,
#                stop,
#                num = 5,
#                endpoint = True,
#                retstep = False,
#                dtype = None)

# -> start  : [optional] start of interval range. By default start = 0
# -> stop   : end of interval range
# -> restep : If True, return (samples, step). By default restep = False
# -> num    : [int, optional] No. of samples to generate
# -> dtype  : type of output array


import numpy as np
# run the folloiwng command to use the pylab
#  pip install matplotlib
import pylab as p

x_axis = np.linspace(0,5,10, endpoint=False)
# Generate y_axis with new shape array
y_axis = np.ones(10)
# This will draw chart
p.plot(x_axis,y_axis, '*')
p.show()
#p.xlim(-0.2, 1.8)


