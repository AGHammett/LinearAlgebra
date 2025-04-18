import numpy as np
import matplotlib.pyplot as plt

def visualise_matrix(matrices: tuple, titles: tuple) -> None:

    """"
    Plots the given matrices in a grid format in different window."
    
    Parameters:
    matrices (tuple): A tuple of matrices to be visualised.""
    titles (tuple): A tuple of titles for each matrix.""
    
    Returns:
    None
    """

    if len(matrices) != len(titles):
        raise ValueError(f"The number of titles does not match the number of matrices.{len(matrices)} matrices and {len(titles)} titles were provided.")
    
    for m in range(len(matrices)):
        fig, ax = plt.subplots()

        fig.patch.set_facecolor('white')
        ax.set_facecolor('white')
        
        ax.matshow(np.ones_like(matrices[m]), cmap='gray', vmin=0, vmax=1)  
        for (i, j), val in np.ndenumerate(matrices[m]):
            ax.text(j, i, f'{val}', ha='center', va='center', color='black')

        ax.set_xticks([]) 
        ax.set_yticks([])  
        ax.set_title(titles[m], fontsize=16, fontweight='bold')

    plt.show()
