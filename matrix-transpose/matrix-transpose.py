import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A = np.array(A)
    rows,cols = A.shape
    new_matrix = np.zeros((cols,rows))

    for row in range(rows):
        for col in range(cols):
            new_matrix[col][row]=A[row][col]
    return new_matrix
    pass
