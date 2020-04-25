import numpy as np
np.random.seed(0)

x1 = np.random.randint(10, size = 6) # One diamensional array
x2 = np.random.randint(10, size = (3,4)) # Two diamensional array
x3 = np.random.randint(10, size = (3,4,5)) # Three diamensional array

x1

x2

x3

print('x3 ndim = ', x3.ndim)

print('x3 size = ', x3.size)

print('x3 shape = ', x3.shape)

print('x3 dtype = ', x3.dtype)

print('item size = ', x3.itemsize, 'bytes')

print('nbytes = ', x3.nbytes, 'bytes')
