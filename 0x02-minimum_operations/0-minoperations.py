#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations
in this file: Copy All and Paste. Given a number n,
write a method that calculates the fewest number
of operations needed to result in exactly n H
characters in the file.
"""


def minOperations(n):
    """min operations"""
    if n == 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n /= divisor
        else:
            divisor += 1

    return operations
