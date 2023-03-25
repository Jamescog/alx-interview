#!/usr/bin/python3
"""# Probem number 8"""


def makeChange(coins, total):
    """ Given a pile of coins of different values, this functio will determine
        the fewest number of coins needed t meet a given amount total.
    """
    if total <= 0:
        return 0
    
    min_coins = [float('inf') * (total + 1) ] 
    min_coins[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], 1 + min_coins[i- coin])
    
    if min_coins[total] != float('inf'):
        return min_coins[total]
    return -1
