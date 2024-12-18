#!/usr/bin/python3
"""makeChange module
"""


def makeChange(coins, total):
    """Make change function
    """
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    # dp[x] = min(dp[x], dp[x-coin] + 1)
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
