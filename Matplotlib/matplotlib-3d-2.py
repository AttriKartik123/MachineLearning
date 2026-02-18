#plt.subplot(rows, columns, position)
import matplotlib.pyplot as plt

# Simple straight line data
x = [0, 1, 2, 3, 4]
y = [0, 1, 2, 3, 4]
z = [0, 1, 2, 3, 4]

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot straight line
ax.plot(x, y, z)

# Show plot
plt.show()
