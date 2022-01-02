# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 01:04:28 2021

@author: ChristianV700
"""


def FibIter(n):
    """Return the nth Fibonacci number iteratively. Assumes n >= 0."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # the first two fibs are always given
        fib_i = 0
        fib_ii = 1
        # Starting with n = 2, it's temp, fib_i, fib_ii (new number)
        for i in range(n-1):
            temp = fib_i
            fib_i = fib_ii
            fib_ii = temp + fib_i
        return fib_ii


print('Iterative calculation: ', FibIter(10))


def FibRecur(n):
    """Return the nth Fibonacci number recursively. Assumes n >= 0."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return FibRecur(n-1) + FibRecur(n-2)


print('Recursive calculation: ', FibRecur(10))
