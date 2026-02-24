import numpy as np
arr = np.arange(8).reshape((2,2,2))
print("Input array : \n ", arr)
print("Flipped array : \n ", np.flip(arr, 0))




import numpy as np

arr = np.arange(8).reshape(2, 2, 2)
print("Input array:\n", arr)
print("Flipped array (along axis 2):\n", np.flip(arr, axis=2))



#flipped array
import numpy as np

arr = np.array([10, 20, 30, 40])
print("Input array:", arr)
print("Flipped array:", np.flip(arr))



