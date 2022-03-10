# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 12:09:34 2021

@author: ChristianV700

Bisection Search aka Binary Search
"""


def BisectionSearch1(L, ele):
    """Return Boolean if sorted list of ints contains element. Element to
    search for must be int. Cut list in halves below and above element and
    check for element. Must create new list of half length!
    Complexity growth O(n log(n)).
    """
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == ele
    else:
        half_length = len(L) // 2

        # Element is smaller than half length of list, search in first half
        if ele < L[half_length]:
            return BisectionSearch1(L[:half_length], ele)
        # Ele is NOT smaller than half length of list, search in second half
        else:
            return BisectionSearch1(L[half_length:], ele)


my_list = [4, 6, 7, 8, 9, 22, 33, 35, 49, 55]
print("-----Bisection Search.-----")
print(BisectionSearch1(my_list, 1))
print(BisectionSearch1(my_list, 5))
print(BisectionSearch1(my_list, 6))
print(BisectionSearch1(my_list, 23))
print(BisectionSearch1(my_list, 33))


def BisectionSearch2(L, ele):
    """Return Boolean if sorted list of ints contains element. Element to
    search for must be int. Cut list in halves below and above element and
    check for element. Uses idx to avoid creating new lists.
    Complexity growth O(log(n)).
    """
    def BisectionHelper(L, ele, low_idx, high_idx):
        """Recursive function that checks if ele is on list between indices."""
        if high_idx == low_idx:
            return L[low_idx] == ele  # Return True when ele found

        mid_idx = (low_idx + high_idx) // 2
        if L[mid_idx] == ele:
            return True
        # Search in lower half of list
        elif L[mid_idx] > ele:
            if low_idx == mid_idx:
                return False
            else:
                return BisectionHelper(L, ele, low_idx, mid_idx - 1)
        # Search in higher half of list
        else:
            return BisectionHelper(L, ele, mid_idx + 1, high_idx)

    if len(L) == 0:
        return False
    else:
        return BisectionHelper(L, ele, 0, len(L) - 1)


print("-----Bisection Search with index.-----")
print(BisectionSearch2(my_list, 1))
print(BisectionSearch2(my_list, 5))
print(BisectionSearch2(my_list, 6))
print(BisectionSearch2(my_list, 23))
print(BisectionSearch2(my_list, 33))
