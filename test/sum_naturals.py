"""Generalization."""

def identity(k):
    return k

def cube(k):
    return pow(k,3)

def summation(n, term):
    """Sum the first N terms of a sequence.
    
    >>> summation(5, cube)
    225

    >>> summation(5, identity)
    15
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total


def sum_naturals(n):
    """Take the first N natural numbers

    >>> sum_naturals(5)
    15
    """
    total, k = 0, 1 
    while k <= n:
        total, k = total + k, k + 1
    return total

def sum_cubes(n):
    """Sum the first N cubes of natural numbers
    >>> sum_cubes(5)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + k * k * k, k + 1
    return total