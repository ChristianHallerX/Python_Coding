# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 13:09:24 2022

@author: ChristianV700
"""


def SelectionSort(L):
    """Sort a smaller and smaller portion of the list. Compare each element
    of remaining list against marker.
    Complexity growth O(n2), where n is len(L).
    """
    marker_idx = 0
    # Loop while marker is not at the end of the list
    while marker_idx != len(L):
        # Iterate over list elements from marker to end
        for i in range(marker_idx, len(L)):
            # Move item to marker position if it is smaller than the marker
            if L[i] < L[marker_idx]:
                L[i], L[marker_idx] = L[marker_idx], L[i]
        marker_idx += 1
        print(L[marker_idx])
    return L


myList = [20, 1, 22, 45, 8, 92, 0, 18, 21, 44]
print("Before sorting: ", myList)
print(SelectionSort(myList))
