import numpy as np

# Set the seed so random numbers are the same every time
np.random.seed(42)

# Create a 2D array of shape (3, 4) with random integers from 0 to 9
arr2d = np.random.randint(0, 10, size=(3, 4))

print("2D Array with seed:\n", arr2d)
