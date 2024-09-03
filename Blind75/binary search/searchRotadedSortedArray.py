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


def search(nums: list[int], target: int) -> int:
    """
    Rotated array/list of integers.
    Return index of target.
    Find solution that is faster than O(n). I.e., binary search O(logn).
    Rotation: Pivot, left portion, right portion.
    Binary Search: left pointer, mid pointer, right pointer.

    If middle val larger than left val, then we are in left sorted portion.
    You can't figure out the if conditions without drawing up the combinations.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (right + left) // 2

        # Target is at mid, exit loop
        if nums[mid] == target:
            return mid

        # Mid is in left portion
        if nums[left] <= nums[mid]:
            # Search right portion
            if target > nums[mid]:
                left = mid + 1
            # Search right portion
            elif target < nums[left]:
                left = mid + 1
            # Search left portion
            else:
                right = mid - 1

        # Mid is in right portion
        else:
            # Search left portion
            if target < nums[mid]:
                right = mid - 1
            # Search left portion
            elif target > nums[right]:
                right = mid - 1
            # Search right portion
            else:
                left = mid + 1

    # Mid never arrived at target -> bug or -> target does not exist in nums.
    return -1


def main():
    print(search(nums=[4, 5, 6, 7, 0, 1, 2], target=0), "expected 4")
    print(search(nums=[4, 5, 6, 7, 0, 1, 2], target=3), "expected -1")
    print(search(nums=[1], target=0), "expected -1")


if __name__ == "__main__":
    main()
