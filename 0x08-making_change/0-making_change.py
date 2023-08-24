#!/usr/bin/python3
"""
Ftn to calculate fewest no of coins
"""


def makeChange(coins, total):
    """ftn to determine min no. of coins"""
    if total < 0:
        return 0  # If the target total is negative, return 0.

    # Initialize an array to store the minimum
    # number of coins needed for each total.
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Zero coins are needed to make change for zero total.

    # Iterate through each coin value.
    for coin in coins:
        for i in range(coin, total + 1):
            # Calculate the minimum number of coins
            # needed for the current total.
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1  # If no combination of coins can make the total, return -1.
    else:
        return dp[total]
