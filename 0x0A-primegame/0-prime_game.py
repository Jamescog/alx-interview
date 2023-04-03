#!/usr/bin/python3
"""0. Prime Game"""


def generate_primes(n: int):
    """ Generate a list of prime numbers up to n using the
        sieve of Eratosthenes algorithm.

        Params:
            n: int - number up to which the prime number generated.

        Returns:
            List of prime numbers
    """

    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return primes


def isWinner(x: int, nums):
    """Determines who is the winner

        Params:
        x: int - the number of rounds
        nums: List - the array of n
    """

    winner_count = {"Maria": 0, "Ben": 0}
    for n in nums:
        primes = generate_primes(n)
        if len(primes) == 0:
            winner_count["Ben"] += 1
            continue
        if len(primes) % 2 == 0:
            winner_count["Ben"] += 1
        else:
            winner_count["Maria"] += 1

    if winner_count["Maria"] > winner_count["Ben"]:
        return "Maria"
    elif winner_count["Maria"] < winner_count["Ben"]:
        return "Ben"
    else:
        return None
