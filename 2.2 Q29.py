import numpy as np
from scipy.linalg import lu

pivot_1 = 0
pivot_2 = 0
pivot_3 = 0

num_iterations = 100000

for i in range(num_iterations):
    A = np.random.rand(3, 3)

    P, L, U = lu(A)

    pivot_1 += abs(U[0, 0])
    pivot_2 += abs(U[1, 1])
    pivot_3 += abs(U[2, 2])

pivot_1 /= num_iterations
pivot_2 /= num_iterations
pivot_3 /= num_iterations

print(f"Pivot 1 Average: {pivot_1}")
print(f"Pivot 2 Average: {pivot_2}")
print(f"Pivot 3 Average: {pivot_3}")

