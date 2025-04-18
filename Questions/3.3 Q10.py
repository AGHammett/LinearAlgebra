import numpy as np

u = np.array(((3, 1, 4),))
v = np.array(((1, 2, 2),))

A = np.matmul(u.T, v)

print(A)

b = np.array(((2, -1),))
c = np.array(((1, 1, 3, 2),))

a = np.matmul(b.T, c)
print(a)