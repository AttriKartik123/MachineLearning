import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)


#NDIM
print(arr.ndim)

arr = np.array([[1, 2], [3, 4], [5, 6]])
print(arr.ndim)  # Output: 2


#RESHAPE
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr.shape)  # Output: (5,)

arr = np.array([[1, 2], [3, 4], [5, 6]])
print(arr.shape)  # Output: (3, 2)  -> 3 rows and 2 columns 

b = arr.reshape(2,3)
print(b)
print(arr.shape) 

#ndarray.size

arr = np.array([1, 2, 3, 4, 5])
print(arr.size)  # Output: 5

arr = np.array([[1, 2], [3, 4], [5, 6]])
print(arr.size)  # Output: 6



#ndarray.dtype
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)  # Output: int64

arr = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
print(arr.dtype)  # Output: float64


#ndarray.itemsize ----> This attribute represents the size (in bytes) of each element in the array.
arr = np.array([1, 2, 3, 4, 5])
print(arr.itemsize)  # Output: 8 (for int64 on a 64-bit system)

arr = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
print(arr.itemsize)  # Output: 8 (for float64 on a 64-bit system)



#data attribute -> points to the start  of the array data 
import numpy as np
arr1 = np.array(([1,2,3],[4,5,6]), dtype=np.int32)

print(arr1.data)




#Flags
import numpy as np
arr1 = np.array(([1,2,3],[4,5,6]), dtype=np.int32)

print(arr1.flags)