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

    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        if coin > total:
            continue
        count += total // coin
        total %= coin
        if total == 0:
            return count
    
    return -1


