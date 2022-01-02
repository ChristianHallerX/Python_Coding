# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 18:39:43 2022

@author: ChristianV700
"""

def factorial_iter(n):
    """Return n! by iterating over n. Growth complexity: O(n)."""
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod


print(factorial_iter(4))

def factorial_recur(n):
    """Return n! by muliplying n with n-1, n-2.... Growth complexity: O(n)."""
    if n <= 1:
        return 1
    else:
        return n * factorial_iter(n - 1)


print(factorial_recur(4))
