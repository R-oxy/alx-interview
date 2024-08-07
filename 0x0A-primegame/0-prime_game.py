#!/usr/bin/python3
"""
Prime Game Module
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game after x rounds.

    Args:
    x (int): The number of rounds.
    nums (list): List of integers representing the range for each round.

    Returns:
    str: The name of player that won the most rounds or None if it is a tie.
    """
    if x <= 0 or not nums:
        return None

    # Find the maximum number in nums to generate primes up to that number
    max_num = max(nums)

    # Generate primes using Sieve of Eratosthenes
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(max_num ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False

    # Calculate the prime counts for each number up to max_num
    prime_counts = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if is_prime[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Determine the winner for each round
    for n in nums:
        if prime_counts[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
