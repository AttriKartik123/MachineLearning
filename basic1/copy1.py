import numpy as np

input_arr = np.array([[5,2,7,4],[9,0,2,3],[1,2,3,19]])
print("The Original Array is :\n")
print(input_arr)
print("\nThe ID of array a:")
print(id(input_arr))

b = input_arr  # assigning input_arr to b
print("\nNow we make the copy of the input_arr")
print("\nThe ID of b:")
print(id(b))

b.shape = (4,3)  # making some changes to b
print("\nThe Changes on b also reflect to a:")
print(input_arr)







#IN CONTEXT OF COPY GIVEN EXAMPE 
import numpy as np

input_arr = np.array([[5,2,7,4],[9,0,2,3],[1,2,3,19]])
print("Original Array:\n", input_arr)
print("ID of input_arr:", id(input_arr))

b = input_arr.copy()
print("\nAfter Copy:")
print("ID of b:", id(b))

b.shape = (4,3)
print("\nAfter changing b, input_arr remains:")
print(input_arr)
print("b becomes:")
print(b)
