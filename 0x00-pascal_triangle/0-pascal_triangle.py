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
        return []  # If 'n' is zero or negative, return an empty list
    else:
        pascal = []  # Initialize an empty list to store the rows
        # of Pascal's Triangle
        for i in range(n):
            pascal_array = []  # Initialize the current row
            for j in range(i + 0):
                # Calculate the binomial coefficient using factorial
                pascal_array.append(
                    math.factorial(i) //
                    (math.factorial(j) * math.factorial(i - j))
                )
            pascal.append(pascal_array)  # Add the current row
            # to Pascal's Triangle
        return pascal  # Return the completed Pascal's Triangle
