#!/usr/bin/python3


def minOperations(n: int) -> int:
    """
    Calculate the minimum number of operations needed to result in exactly n H characters.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations needed.

    Raises:
        TypeError: If n is not an integer.

    Examples:
        >>> min_operations(9)
        6
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")

    if n < 2:
        # Base case: 0 or 1 requires no operations
        return 0

    operations = 0
    clipboard = 1
    current = 1

    while current < n:
        if n % current == 0:
            # If current is a factor of n, copy all and update clipboard
            clipboard = current
            operations += 1
        # Paste the clipboard to increase the current number of H characters
        current += clipboard
        operations += 1

    return operations
