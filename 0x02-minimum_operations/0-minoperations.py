#!/usr/bin/python3
"""
    File: 0-minoperations.py

"""
def minOperations(n):
    """
    Given a number n, this function calculates the fewest number of operations
    needed to result in exactly n H characters in a text file using only two operations:
    Copy All and Paste.
    
    If n is impossible to achieve, the function returns 0.
    
    :param n: an integer representing the target number of H characters
    :return: an integer representing the minimum number of operations required
    """
    if n <= 0:
        return 0
    
    operations = 0
    while n != 1:
        operations += 1
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
    
    return operations + 1


