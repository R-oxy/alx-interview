#!/usr/bin/python3
""" minimum operations"""


def minOperations(n):
    """ return min n of operations"""
    
    operations = 0
    current = 1
    clipboard = 0

    if current > n:
        return 0

    while current < n:
        if n % current == 0 and current > clipboard:
            clipboard = current
        else:
            current += clipboard
        operations += 1

    return operations
