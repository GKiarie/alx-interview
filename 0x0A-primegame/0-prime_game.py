#!/usr/bin/python3
"""Prime Game
"""


def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def calculate_winner(n):
        dp = [False] * (n + 1)
        for i in range(2, n + 1):
            if not dp[i] and is_prime(i):
                for j in range(i, n + 1, i):
                    dp[j] = True
        return "Ben" if dp[n] else "Maria"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = calculate_winner(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
