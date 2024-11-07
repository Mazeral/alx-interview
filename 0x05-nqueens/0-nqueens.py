#!/usr/bin/python3
"""
Module for solving the N-Queens problem using backtracking.

The N-Queens problem is the task of placing N queens on an N×N chessboard
such that no two queens attack each other. This module provides a solution
using recursion and backtracking.
"""

import sys
from typing import Dict, List, Tuple

# Global variables to store the queens' positions and found solutions.
queens: Dict[int, List[int]] = {}
solutions: List[List[List[int]]] = []


def diag_safe(curr_key: int) -> bool:
    """
    Check if the queen at the current key is safe diagonally.

    Args:
        curr_key (int): The key representing the current queen's position.

    Returns:
        bool: True if the queen is safe diagonally, False otherwise.
    """
    for key, value in queens.items():
        if key != curr_key:
            x_diff = abs(queens[curr_key][0] - queens[key][0])
            y_diff = abs(queens[curr_key][1] - queens[key][1])
            if x_diff == y_diff:
                return False
    return True


def row_safe(curr_key: int) -> bool:
    """
    Check if the queen at the current key is safe horizontally.

    Args:
        curr_key (int): The key representing the current queen's position.

    Returns:
        bool: True if the queen is safe horizontally, False otherwise.
    """
    for key, value in queens.items():
        if queens[curr_key][0] == queens[key][0] and curr_key != key:
            return False
    return True


def col_safe(curr_key: int) -> bool:
    """
    Check if the queen at the current key is safe vertically.

    Args:
        curr_key (int): The key representing the current queen's position.

    Returns:
        bool: True if the queen is safe vertically, False otherwise.
    """
    for key, value in queens.items():
        if queens[curr_key][1] == queens[key][1] and curr_key != key:
            return False
    return True


def queen_safe(key: int) -> bool:
    """
    Check if the queen at the given key is safe from attacks.

    Args:
        key (int): The key representing the current queen's position.

    Returns:
        bool: True if the queen is safe, False otherwise.
    """
    return col_safe(key) and row_safe(key) and diag_safe(key)


def recursive_sol(key: int) -> None:
    """
    Recursive backtracking function to place queens on the board.

    Args:
        key (int): The current row key to place a queen.
    """
    n = int(sys.argv[1])

    # Base case: all queens are placed
    if key == n:
        solution = [x for x in queens.values()]
        solutions.append(solution)
        return

    # Try placing the queen in each column of the current row
    for col in range(n):
        queens[key] = [key, col]
        if queen_safe(key):
            recursive_sol(key + 1)

    # Reset the queen's position for backtracking
    queens[key] = [-1, -1]


def nqueens() -> None:
    """
    Main function to solve the N-Queens problem.
    It parses the input, initializes the queens' positions, and prints all
    solutions.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize queens' positions
    for x in range(n):
        queens[x] = [-1, -1]

    # Start the recursive backtracking
    recursive_sol(0)

    # Print each solution
    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    nqueens()
