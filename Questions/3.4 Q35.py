import numpy as np
from seconddifference import second_difference_matrix
import matplotlib.pyplot as plt

K = second_difference_matrix(9)

b = np.full(9, 10)

x = np.linalg.solve(K, b)
print(x)

plt.plot(x, 'o', linestyle='--', color='red')
plt.show()