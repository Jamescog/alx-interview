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
    
    def minOperations(n) -> int:
        if type(n) != int or n <= 0:
            return 0
        ops_count = 0
        i = 2
        while i <= n:
            while n % i == 0:
                ops_count += 2
                n /= i
            i += 1
        return ops_count + 1


