# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 13:53:30 2022

@author: ChristianV700
"""


def MergingSublists(l_list, r_list):
    """Merge two sorted sublists to one sorted result list by looping over and
    comparing first elements. O(n log(n)) growth in complexity.
    Best worst case algorithm.
    """
    result = []
    l_idx, r_idx = 0, 0

    # While there is still something in left AND right lists...
    while l_idx < len(l_list) and r_idx < len(r_list):
        # If ele in left list is smaller, append to result, increase left idx
        if l_list[l_idx] < r_list[r_idx]:
            result.append(l_list[l_idx])
            l_idx += 1
        # If ele in right list is smaller, append to result, inrease right idx
        else:
            result.append(r_list[r_idx])
            r_idx += 1

    # Only left list is left over, append all to result
    while l_idx < len(l_list):
        result.append(l_list[l_idx])
        l_idx += 1

    # Only right list is left over, append all to result
    while r_idx < len(r_list):
        result.append(r_list[r_idx])
        r_idx += 1
    print("result: ", result)
    return result


def MergeSort(L):
    """Split list in two sublists, then merge by comparing."""
    print("split list: ", L)
    if len(L) < 2:
        return L
    else:
        middle_idx = len(L)//2
        # Keep splitting in half by recursion
        left_list = MergeSort(L[:middle_idx])
        right_list = MergeSort(L[middle_idx:])
        return MergingSublists(left_list, right_list)


# Test helper function
l_list = sorted([2, 4, 5, 2, 11, 99, 83, 81, 12])
r_list = sorted([1, 4, 5, 888, 54, 38, 80, 221, 34, 37, 73])

# print("Helper function result: ", MergingSublists(l_list, r_list))

L = [48, 8, 7, 39, 817, 70, 50, 27, 17, 72, 38, 91, 84, 69, 99, 722, 1, 260]
print("Unsorted list: ", L)
print("MergeSort result: ", MergeSort(L))
