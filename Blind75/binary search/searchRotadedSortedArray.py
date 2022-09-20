"""
33. Search in Rotated Sorted Array (medium)

There is an integer array 'nums' sorted in ascending order (with distinct values).

Prior to being passed to your function, 'nums' is possibly rotated at an unknown pivot index 'k' (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0, 1, 2, 4, 5, 6, 7] might be rotated at pivot index 3 and become [4, 5, 6, 7, 0, 1, 2].

Given the array 'nums' after the possible rotation and an integer 'target', return the index of 'target'
if it is in 'nums', or -1 if it is not in 'nums'.

You must write an algorithm with O(log n) runtime complexity. Simply looping over 'mums' is O(n).
"""

def searchRotadedSortedArray(nums: list[int], target: int) -> int:
    # return index of target, return -1 if not found
    # if better than linear time complexity O(n) required -> binary search solution
    # left, middle, right pointer. In which part of the rotated array is the middle pointer?, search left or right next?
    left_p, right_p = 0, len(nums) - 1

    while left_p <= right_p: # don't let pointers cross
        mid_p = (left_p + right_p) // 2
        # all the shifting of pointers always shift mid p to the target -> exit loop here
        if nums[mid_p] == target:
            return mid_p

        # mid is in left portion
        if nums[left_p] <= nums[mid_p]:

            # target is larger than mid or smaller than left-most element -> move left p right of mid p
            if target > nums[mid_p]:
                left_p = mid_p + 1
            # target is smaller than left most value, must be in right portion -> move left p right of mid p
            elif target < nums[left_p]:
                left_p = mid_p + 1
            # only search left portion of array
            # target is smaller than mid, but larger than left most element -> move right p left of mid p
            else:
                right_p = mid_p - 1

        # mid is in right portion
        else:
            # target is smaller than mid -> move mid towards left of mid
            if target < nums[mid_p]:
                right_p = mid_p - 1
            # target is larger than right most value -> must be on left portion -> move right p left of mid p
            elif target > nums[right_p]:
                right_p = mid_p - 1
            # only search right portion of array,
            # target is greater than mid and less than right most element -> move left p to right of mid p
            else:
                left_p = mid_p + 1

    # return -1 if target was not found at mid p
    return -1


def main():
    print(searchRotadedSortedArray(nums=[4, 5, 6, 7, 0, 1, 2], target=0), "expected 4")
    print(searchRotadedSortedArray(nums=[4, 5, 6, 7, 0, 1, 2], target=3), "expected -1")
    print(searchRotadedSortedArray(nums=[1], target=0), "expected -1")


if __name__ == "__main__":
    main()
