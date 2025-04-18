import numpy as np
from projectionmatrix import projection_matrix

A = np.array(([3, 6, 6], [4, 8, 8]))

P = projection_matrix(A)
print(P)

print(np.matmul(A.T, A))