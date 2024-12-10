#!/usr/bin/python3
"""prime_game module solution
"""


def SieveOfEratosthenes(n):
    """
    Find all prime numbers up to n using the Sieve of Eratosthenes.

    Args:
        n (int): The upper limit for finding prime numbers.

    Returns:
        list: A list of prime numbers up to n.
    """
    if n < 2:
        return []

    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    for p in range(2, int(n ** 0.5) + 1):
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False

    return [p for p in range(2, n + 1) if prime[p]]


def isWinner(x, nums):
    """
    Determine the winner of the prime game.

    Args:
        x (int): The number of rounds.
        nums (list): A list of integers representing the upper limits.

    Returns:
        str: The winner of the game, "Ben", "Maria", or None.
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)
    primes = SieveOfEratosthenes(max_n)

    # Count the number of wins for each player
    Maria_wins = 0
    Ben_wins = 0

    for n in nums:
        # Simulate the game for the current number
        remaining_numbers = set(range(1, n + 1))
        current_player = 0  # 0: Maria, 1: Ben

        for prime in primes:
            if prime > n:
                break

            # Remove prime and its multiples
            if prime in remaining_numbers:
                multiples = set(range(prime, n + 1, prime))
                remaining_numbers -= multiples
                current_player = 1 - current_player

        # Determine the winner of the round
        if current_player == 1:  # Ben made the last move
            Maria_wins += 1
        else:
            Ben_wins += 1

    # Determine the overall winner
    if Maria_wins > Ben_wins:
        return "Maria"
    elif Ben_wins > Maria_wins:
        return "Ben"
    return None
