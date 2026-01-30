import numpy as np
arr= np.arange(10)
print(arr)

#using index indirectly
b = arr[2] = 100
print(arr)

print("Slicing of items starting from the index:")
print (arr[2:])

print("Slicing of items starting from the index:")
print (arr[2:8])



#USING ELLIPSES


a = np.array([[11,2,23],[33,44,5],[84,25,16]])
print("The array is :")
print(a )
print ('\n')

#To return array of items in the second column
print("The items in second column are:")
print(a[... , 1])

# In order to slice all items from the second row
print ('The items in the second row are:')
print(a[1, ...])
print ('\n')

# In order to slice all items from column 1 onwards
print ('The items onwards to column 1 are:' )
print (a[..., 1:])

