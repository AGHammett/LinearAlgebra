import numpy as np

P = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]])

Q = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 1, 0, 0]])

def matrix_power(matrix, power):
    result = matrix
    for i in range(power-1):
        result = np.matmul(result, matrix)
    return result

print(matrix_power(P, 3))
print(matrix_power(Q, 4))