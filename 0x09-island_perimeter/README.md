# Island Perimeter README
=====================================

## Project Overview

This project calculates the perimeter of a single island in a grid, represented by a 2D array of integers. The goal is to apply knowledge of algorithms, data structures (specifically matrices or 2D lists), and iterative or conditional logic to solve a geometric problem within a grid context.

## Requirements

* Allowed editors: vi, vim, emacs
* All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
* All files should end with a new line
* The first line of all files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Code should use the PEP 8 style (version 1.7)
* No module imports are allowed
* All modules and functions must be documented
* All files must be executable

## Task Description

Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in `grid`:

* `grid` is a list of list of integers:
	+ 0 represents water
	+ 1 represents land
	+ Each cell is square, with a side length of 1
	+ Cells are connected horizontally/vertically (not diagonally)
	+ `grid` is rectangular, with its width and height not exceeding 100
* The grid is completely surrounded by water
* There is only one island (or nothing)
* The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island)

## Example Usage

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12
```

## Solution

The solution is implemented in the `0-island_perimeter.py` file. The function `island_perimeter(grid)` iterates over the grid, applying logical operations to identify the perimeter of the island. The perimeter is calculated by counting the edges that contribute to the island’s perimeter.

## Resources

* Python Official Documentation: Nested Lists
* GeeksforGeeks Articles: Python Multi-dimensional Arrays
* TutorialsPoint: Python Lists
* YouTube Tutorials: Python 2D arrays and lists

## Additional Resources

* Mock Technical Interviews

## Repository

* GitHub repository: alx-interview
* Directory: 0x09-island_perimeter
* File: 0-island_perimeter.py
