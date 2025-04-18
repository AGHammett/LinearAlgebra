import numpy as np

C = np.array(((1, 1), (2, 4), (3, 1), (4, 2)))
R = np.array(((2, 1), (3, 4), (2, 2), (3, 1)))

A = np.matmul(C, R.T)
print(A)
