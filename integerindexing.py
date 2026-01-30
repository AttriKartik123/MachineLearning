import numpy as np

x = np.array([[11, 28], [23, 84], [95, 56]])
print("The array used for Integer Indexing")
print(x)

y = x[[0,1,2], [0,0,1]]   #---> 0,1,2 ROW AND 0TH 0TH  1ST ELEMENT 
print("The Output is:")
print(y)




# another code 
import numpy as np
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print ('The array is:')
print (x)

#picking the first and last row
rows= np.array([[0] , [3]])

# picking 0 index and 2nd index element from each row
cols = np.array(([0,2] , [0,2]))

y = x[rows,cols]


print('The corner elements of the array are:')
print(y)