#!/usr/bin/python3
"""
0-pascal_triangle
"""

import math


def pascal_triangle(n):
    """
    Generate Pascal's Triangle with 'n' rows.

    Parameters:
        n (int): Number of rows to generate in Pascal's Triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle.
              Each inner list contains the numbers of that row.
    """
    if n <= 0:
        return []
    else:
        pascal = []
        for i in range(n):
            pascal_row = []
            j = 0
            while j <= i:
                if j == 0 or j == i:
                    pascal_row.append(1)
                else:
                    pascal_row.append(pascal[i-1][j-1] + pascal[i-1][j])
                j += 1
            pascal.append(pascal_row)
        return pascal
