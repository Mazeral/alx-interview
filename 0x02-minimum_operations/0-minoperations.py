#!/usr/bin/python3


def minOperations(n: int) -> int:
    """
    Calculate the minimum number of operations required to reduce a number to 1.

    The operations allowed are subtracting the smallest factor of the number.

    Args:
        n (int): The number to reduce.

    Returns:
        int: The minimum number of operations required.

    Raises:
        TypeError: If n is not an integer.

    Examples:
        >>> min_operations(10)
        8
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")

    if n < 2:
        # Base case: 0 or 1 requires no operations
        return 0

    operations = 0
    factor = 2

    # Reduce n by its factors, adding operations accordingly
    while n > 1:
        while n % factor == 0:
            # Subtract the factor from n and increment operations
            operations += factor
            n //= factor
        factor += 1

    return operations
