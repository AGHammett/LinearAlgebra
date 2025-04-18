import numpy as np
from scipy.linalg import svd

def projection_matrix(A, tolerance = 1e-10):

    '''
    Takes in a matrix and returns its projection matrix P. 
    
    Arguments:
    A: Input matrix
    tolerance: Tolerance for numerical stability.
    
    "Returns:"
    P = Q Q.T - The projection matrix created from its orthonormal basis
    
    '''
    U, s, Vh = svd(A)

    r = np.sum(s > tolerance)
    Q = U[:, : r]

    return Q @ Q.T