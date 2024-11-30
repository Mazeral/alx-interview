#!/usr/bin/python3
"""makeChange module
"""


def makeChange(coins, total):
    """Make change function
    """
    if total <= 0:
        return 0
    dp = []
    for i in range(total + 1):
        if i == 0:
            dp[i] = 0
        else:
            dp[i] = float('inf')
    # dp[x] = min(dp[x], dp[x-coin] + 1)
    for c in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
