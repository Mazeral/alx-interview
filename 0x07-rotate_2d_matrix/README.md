# 0x07 - Rotate 2D Matrix
=====================================

## Table of Contents
-----------------

1. [Overview](#overview)
2. [Usage](#usage)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Testing](#testing)

## Overview
------------

This repository contains a Python solution for rotating a 2D matrix 90 degrees clockwise. The solution is implemented in the `0-rotate_2d_matrix.py` file.

## Usage
-----

To use the `rotate_2d_matrix` function, simply import it and pass a 2D matrix as an argument. The matrix will be modified in-place.

```python
from 0-rotate_2d_matrix import rotate_2d_matrix

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate_2d_matrix(matrix)
print(matrix)
```

## Requirements
------------

* Python 3.x

## Installation
------------

No installation is required. Simply clone the repository and use the `rotate_2d_matrix` function.

## Testing
-------

A test script is provided in the `main_0.py` file. To run the test, execute the following command:

```bash
./main_0.py
```

This will rotate a sample matrix and print the result.

## Solution
----------

The solution is implemented in the `0-rotate_2d_matrix.py` file. It uses a simple algorithm to rotate the matrix in-place.

```python
def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list): A 2D matrix to be rotated.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    for i in range(n):
        matrix[i] = matrix[i][::-1]
```

This solution first transposes the matrix and then reverses each row to achieve the desired rotation.
