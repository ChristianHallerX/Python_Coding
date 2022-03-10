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


def FibRecur(n):
    """Return the nth Fibonacci number recursively. Assumes n >= 0."""
    if n <= 2:
        return 1
    else:
        return FibRecur(n-1) + FibRecur(n-2)

def FibMemo(n,dict=None):
    if dict == None:
        dict = {}
    if n in dict.keys():
        return dict[n]
    elif n <= 2:
        return 1
    dict[n] = FibMemo(n-1,dict) + FibMemo(n-2,dict)
    return dict[n]


def main():
    print('Iterative calculation: ', FibIter(10))
    print('Recursive calculation: ', FibRecur(10))
    print('Memoization calculation: ', FibMemo(100)) # this should be quick with dict memo

if __name__ == '__main__':
    main()