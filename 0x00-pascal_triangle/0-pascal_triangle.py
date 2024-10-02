#!/usr/bin/python3
"""
A function that generates Pascal's Triangle.

Pascal's Triangle is a triangular array where each number is the sum of the
two directly above it. This function generates the first 'n' rows of Pascal's
Triangle.

Each row corresponds to the binomial coefficients of the expansion of
(a + b)^n.

Args:
    n (int): The number of rows of Pascal's Triangle to generate.

Returns:
    list: A list of lists, where each inner list represents a row of Pascal's
    Triangle.
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
