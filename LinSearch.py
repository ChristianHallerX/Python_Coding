# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 16:50:18 2022

@author: ChristianV700
"""

def LinSearch(L, ele):
    """Return Boolean if element in unsorted list. Complexity growth O(n)."""
    found = False
    for i in L:
        if i == ele:
            # In the best case break early, in worst case, ele is last
            found = True
            break
    return found


L = [12, 48, 27, 77, 176, 28, 93, 3]
print(LinSearch(L, 83))
print(LinSearch(L, 93))
