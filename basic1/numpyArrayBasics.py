
import numpy as np
a = np.array([1,2,3]) # Create a 1D array
print(a)
print(type(a))  # Prints "<class 'numpy.ndarray'>"

b=np.array([1.0,2.0,3.0])
print(b)
print(type(b))

c = np.array([1, 2, 3])   # Create a 1d array
print(c)
print(type(c)) 

print(c.shape)



#GETTTING ARRAY ELEMENTS IN THE NUMPY

b = np.array([[1,2,3],[4,5,6]])    # Create a 2d array
print(b)
print(b.shape)                     # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"