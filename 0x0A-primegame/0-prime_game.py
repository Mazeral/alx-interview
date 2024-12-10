#!/usr/bin/python3
"""prime_game module solution
"""


def SieveOfEratosthenes(n):
    """
    Implementation of the Sieve of Eratosthenes algorithm to find all
    prime numbers up to n.

    Args:
        n (int): The upper limit for finding prime numbers.

    Returns:
        list: A boolean array where prime[i] is True if i is a prime number,
        False otherwise.
    """
    # Create a boolean array "prime[0..n]" and initialize all entries as true.
    # A value in prime[i] will finally be false if i is Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        # If prime[p] is not changed, then it is a prime
        if (prime[p] is True):
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return prime


def multiples_of_n(n, start=0, stop=None):
    """
    Generate a range of multiples of n.

    Args:
        n (int): The number for which to generate multiples.
        start (int, optional): The starting value of the range.
        Defaults to 0.
        stop (int, optional): The stopping value of the range.
        Defaults to n * 10.

    Returns:
        range: A range of multiples of n.
    """
    if stop is None:
        stop = n * 10  # default stop value
    return range(start, stop, n)


def isWinner(x, nums):
    """
    Determine the winner of the prime game.

    Args:
        x (int): The input value.
        nums (list): A list of numbers.

    Returns:
        str: The winner of the game, either "Ben" or "Maria".
    """
    player = False
    Ben = 0
    Maria = 0
    for num in nums:
        numbers = [x for x in range(1, num + 1)]
        # Create an array that saves the prime numbers
        prime_number = SieveOfEratosthenes(num)
        # Create a dictionary that maps every number to its multiples

        def create_multiples_dict(n, max_multiple):
            """
            Create a dictionary that maps every number to its multiples.

            Args:
                n (int): The upper limit for generating multiples.
                max_multiple (int): The maximum multiple to generate.

            Returns:
                dict: A dictionary where each key is a number and its value
                is a list of multiples.
            """
            return {i: [j for j in range(i, max_multiple + 1, i)]
                    for i in range(2, n + 1)}
        multiples = create_multiples_dict(num, num)
        # For each pick, filter the numbers array based on the multiples
        # dictionary If there's a number that is a prime number, continue,
        # else print the result

        # Each turn, pick the first number in the array, then change the
        # player value If the value is True: Ben wins, else Maria wins
        current_number = 2
        while len(numbers) > 1:
            full_list = []
            full_list.extend(numbers)
            filter_list = list(multiples[current_number])
            filtered_result = [item for item in full_list if
                               item not in filter_list]
            numbers.clear()
            numbers.extend(filtered_result)
            current_number += 1
            player = not player

        if player is True:
            Ben += 1
        else:
            Maria += 1
    if Ben > Maria:
        return "Ben"
    else if Maria > Ben:
        return "Maria"
    else:
        return None
