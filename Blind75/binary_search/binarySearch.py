"""
704. Binary Search (easy)

Given an array of integers 'nums' which is sorted in ascending order, and an integer 'target',
write a function to search 'target' in 'nums'.
If target exists, then return its index.
Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""


def search(nums: list[int], target: int) -> int:
    """
    Use left and right pointers at ends of list.
    Divide indices of left/right in half to find middle pointer
    If value at middle is smaller than target, them continue on right (move left pointer to middle +1)
    If middle is larger than target, continue left (move right pointer to middle -1)
    Time complexity: O(nlogn)
    Space complexity: O(1) 3 pointers
    """
    left = 0
    right = len(nums) - 1

    # Pointers close in from the outside, but do never cross
    while left <= right:
        mid = (left + right) // 2
        # Search left
        if nums[mid] > target:
            right = mid - 1
        # Search right
        elif nums[mid] < target:
            left = mid + 1
        # nums[mid] == target
        else:
            return mid
    # If the loop did not find the target
    return -1


def main():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(search(nums, target), "expected: 4")

    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    print(search(nums, target), "expected: -1")


if __name__ == "__main__":
    main()
