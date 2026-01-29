#using numpy.zeros

import numpy as np 
arr = np.zeros((3,4))    #-> 3 rows and 4 columns
print(arr)



#using numpy.ones 


arr = np.ones((2, 2),dtype=np.int32)  # Creates a 2x2 array 
print(arr)


#numpy.empty():
arr1 = np.empty((2,3) , dtype=np.int32)
print(arr1)


#numpy.arange(): -> evenly spaced elements 
arr= np.arange(1 ,30 , 3)
print(arr)


#numpy.eye() or numpy.identity():

import numpy as np

arr = np.eye(3)  # Creates a 3x4 identity matrix
print(arr)



#numpy.random.random():      ----> gives random values
import numpy as np

arr = np.random.random((2, 2))  # Creates a 2x2 array with random values between 0 and 1
print(arr)