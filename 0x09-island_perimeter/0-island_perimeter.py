#!/usr/bin/python3
"""Island permeter module
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of an island in a grid.

    Uses Depth-First Search (DFS) to traverse through the island and
    find the longest perimeter.

    Args:
        grid (list): A 2D list representing the grid, where 0 represents
        water and 1 represents land.

    Returns:
        int: The perimeter of the island. Returns 0 if no perimeter exists.

    Raises:
        TypeError: If the input grid is not a list.
    """

    # Check if the input grid is a list
    if not isinstance(grid, list):
        raise TypeError("Input grid must be a list")

    # Get the number of rows and columns in the grid
    number_of_rows = len(grid)
    number_of_columns = len(grid[0])

    # Initialize a set to keep track of visited cells
    visited = set()

    # Helper function to perform DFS
    def dfs(row, col):
        """
        Performs DFS from the given cell and returns the perimeter.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.

        Returns:
            int: The perimeter of the island.
        """

        # Check if the cell is out of bounds or is water
        if (row < 0 or row >= number_of_rows or
            col < 0 or col >= number_of_columns or
                grid[row][col] == 0):
            return 1

        # Check if the cell has already been visited
        if (row, col) in visited:
            return 0

        # Mark the cell as visited
        visited.add((row, col))

        # Initialize the perimeter
        perimeter = 0

        # Check all four neighbors (up, down, left, right)
        perimeter += dfs(row - 1, col)  # Up
        perimeter += dfs(row + 1, col)  # Down
        perimeter += dfs(row, col - 1)  # Left
        perimeter += dfs(row, col + 1)  # Right

        return perimeter

    # Main logic to find the starting land cell
    for row in range(number_of_rows):
        for col in range(number_of_columns):
            if grid[row][col] == 1:
                # Start DFS from the first land cell found
                return dfs(row, col)

    # If no land cell found, return 0
    return 0
