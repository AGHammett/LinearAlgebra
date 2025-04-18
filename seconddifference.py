import numpy as np

def second_difference_matrix(n: int) -> np.ndarray:
    
    """
    Create a matrix of size n x n with 2 on the diagonals and -1 on the sub and superdiagonals."
    
    Parameters:
    n (int): The size of the matrix."
    
    "Returns:"
    K np.ndarray: The second difference matrix of size n x n.
    """

    K = np.zeros((n, n))
    
    for i in range(n):
        K[i, i] = 2  

        if i > 0:
            K[i, i - 1] = -1

        if i < n - 1:
            K[i, i + 1] = -1
    
    return K