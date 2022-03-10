# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 16:15:41 2021

@author: ChristianV700
"""


def BubbleSort(L):
    """Sort list by comparing two list items and reverse if not sorted.
    Complexity growth: O(n) * O(n) = O(n2) quadratic.
    """
    another_iteration = True

    # Loop while elements have been reversed last run
    while another_iteration:
        # Set to True, which stops While loop when done.
        another_iteration = False
        # Iterate through list
        for i in range(1, len(L)):
            # Check if element pair reversed
            if L[i-1] > L[i]:
                # If one element reversed, need another loop iteration
                another_iteration = True
                # Reverse the two list items
                L[i], L[i-1] = L[i-1], L[i]
    return L


myList = [20, 1, 22, 45, 8, 92, 0, 18, 21, 44]
print("Before sorting: ", myList)
print(BubbleSort(myList))
