import numpy as np
import matplotlib.pyplot as plt

markov_matrix = np.array(((0.8, 0.3), (0.2, 0.7)))
u0 = np.array((1., 0.))
v0 = np.array((0., 1.0))

U = [u0]
V = [v0]

for i in range(6):
    ui = np.matmul(markov_matrix, U[i])
    vi = np.matmul(markov_matrix, V[i])

    U.append(ui)
    V.append(vi)

print(f"U7: {U[6]}")
print(f"V7: {V[6]}")

plt.plot(U)
plt.plot(V)
plt.legend()
# Show the plot
plt.show()