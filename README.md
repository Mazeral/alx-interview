# alx-interview
alx interview repo, contains multiple code challenges!

---
# Pascal's Triangle

## Description

This project implements a function that generates Pascal's Triangle. Pascal's Triangle is a triangular array where each number is the sum of the two numbers directly above it. This function generates the first `n` rows of Pascal's Triangle as a list of lists.

Each row in Pascal's Triangle corresponds to the binomial coefficients of the expansion of the expression `(a + b)^n`. The function efficiently calculates each row and builds the triangle from top to bottom.

## Function Prototype

```python
def pascal_triangle(n):
    """
    Returns a list of integers representing the Pascal Triangle of n.
    Returns an empty list if n <= 0.
    """
```

## Parameters

- `n` (int): The number of rows of Pascal's Triangle to generate.
  - If `n` is less than or equal to 0, the function returns an empty list.

## Returns

- A list of lists, where each inner list contains the numbers of a specific row of Pascal's Triangle.
- The list will contain `n` rows if `n > 0`. If `n <= 0`, the function returns an empty list.

## Example Usage

### Example 1:

```python
>>> pascal_triangle(5)
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
```

### Example 2:

```python
>>> pascal_triangle(0)
[]
```

### Example 3:

```python
>>> pascal_triangle(1)
[[1]]
```

## How It Works

- The function starts by checking if `n` is less than or equal to 0. If true, it returns an empty list.
- If `n > 0`, the function initializes a list `k` with the first row of Pascal's Triangle (`[1]`).
- For each row from 1 to `n-1`, the function calculates the next row by adding elements from the previous row.
  - Each new row starts and ends with `1`.
  - Intermediate elements are calculated by summing pairs of adjacent elements from the previous row.
- The final list `k` is returned, containing all the rows of Pascal's Triangle up to the `n`th row.

## Files

- `0-pascal_triangle.py`: Contains the `pascal_triangle` function implementation.

## Requirements

- Python 3.x
