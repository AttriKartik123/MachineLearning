import numpy as np

dt = np.dtype([('name', 'U10'), ('grades', 'f4', (2,))])
x = np.array([('Sarah', (8.0, 7.0)), ('John', (6.0, 7.0))], dtype=dt)
print(x[1])
print(('John', [6., 7.]))
print(x[1]['grades'])
print(np.array([6.,  7.]))
print(type(x[1]))
print(type(x[1]['grades']))
