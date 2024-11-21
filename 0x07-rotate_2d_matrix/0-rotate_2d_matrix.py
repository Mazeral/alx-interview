#!/usr/bin/python3
"""rotating 2d matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix clockwise by 90 degrees.

    Args:
        matrix (list): A 2D list representing the matrix to be rotated.

    Returns:
        None: The input matrix is modified in-place.
    """
    n = len(matrix[0])
    new_matrix = [[matrix[n - j - 1][i] for j in range(n)] for i in range(n)]
    matrix.clear()
    matrix.extend(new_matrix)
