import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import lu
from visualisematrix import visualise_matrix
from seconddifference import second_difference_matrix


n = 6

K = second_difference_matrix(n)
Kinv = np.linalg.inv(K)
P, L, U = lu(K)

print(K)
print(np.round(Kinv, 2))

#visualise_matrix((K,Kinv, L, U), ("K","K-1", "L", "U"))

#Q 26
Kinv7 = Kinv*7
visualise_matrix((np.round(Kinv7, 1),), ("K*7",))

Kindentity = np.matmul(K, Kinv7)
visualise_matrix((np.round(Kindentity, 1),), ("K*K-1*7",))