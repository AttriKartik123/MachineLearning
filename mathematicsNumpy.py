import numpy as np

x = np.array([4, 9, 16])
y = np.array([2, 3, 4])

print("x =", x)
print("y =", y)

# 1️⃣ Addition
print("\nAddition:", np.add(x, y))

# 2️⃣ Subtraction
print("Subtraction:", np.subtract(x, y))

# 3️⃣ Division
print("Division:", np.divide(x, y))

# 4️⃣ Multiplication
print("Multiplication:", np.multiply(x, y))

# 5️⃣ Square Root
print("Square Root of x:", np.sqrt(x))

# 6️⃣ Sine
print("Sine of x:", np.sin(x))

# 7️⃣ Cosine
print("Cosine of x:", np.cos(x))

# 8️⃣ Natural Log
print("Log of x:", np.log(x))

# 9️⃣ Dot Product
print("Dot product:", np.dot(x, y))

# 🔟 Roots of polynomial: x² - 4 = 0
print("Roots of polynomial:", np.roots([1, 0, -4]))
