import numpy as np 

#Integer Indexing
import numpy as np

# 1D array
arr1D = np.array([1, 2, 3, 4, 5])

# Access third element
print(arr1D[2])  
print(arr1D[0])




#Access 2-D Arrays

arr2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2D[1, 2])
print(arr2D[2,2])  


#Negative Indexing in NumPy Arrays
import numpy as np

# Create a 1-D numpy array
arr = np.array([10, 20, 30, 40, 50])

# Access elements using negative indexing
print(arr[-1])  
print(arr[-2])  
print(arr[-3])  


# Create a 2-D numpy array
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Access elements using negative indexing
print(arr_2d[-1, -1])  # Outputs: 12
print(arr_2d[-2, -3])  # Outputs: 6


#Array slicing 
import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

subset = arr[1:7:2]

print(subset)  



#2-D Array Slicing
# Create a 2D array
matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Use slicing to get a subset of the array
subset = matrix[1:, 2:]

print(subset)

#output
# [[ 7  8]
#  [11 12]]


