#!/usr/bin/python3
""" minimum operations"""


def minOperations(n):
    """
    Calculates minimum operations needed to achieve n 'H' characters.

    Args:
        n (int): Target number of 'H' characters.

    Returns:
        int: Minimum number of operations required.
             Returns 0 if n is impossible to achieve.
    """
    if n <= 0:
        return 0
    
    operations = 0
    current = 1
    clipboard = 0

    while current < n:
        if n % current == 0:
            clipboard = current
        current += clipboard
        operations += 1

    return operations
