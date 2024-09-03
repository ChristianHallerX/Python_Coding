"""
153. Find Minimum in Rotated Sorted Array (medium)

Suppose an array of length 'n' sorted in ascending order is rotated between 1 and 'n' times. For example, the array
'nums' = [0, 1, 2, 4, 5, 6, 7] might become:

- [4, 5, 6, 7, 0, 1, 2] if it was rotated 4 times.
- [0, 1, 2, 4, 5, 6, 7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2],
..., a[n-2]].

Given the sorted rotated array 'nums' of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
"""


def findMin(nums: list[int]) -> int:
    """
    Find minimum value in sorted, rotated array of integers.
    "pivot" = where highest and lowest number meet.
    Use Binary search: left, middle, right pointers.
    In which part does the middle pointer fall into?
    -> Compare middle to values on left and right ends of list.
    - If mid is larger than left (left is small), search right portion
    - If mid is smaller than left (left is big), search left portion.
    """

    result = nums[0]  # initialize with arbitrariy value
    left, right = 0, len(nums) - 1

    while left <= right:
        if nums[left] < nums[right]:
            result = min(result, nums[left])
            break
        mid = (left + right) // 2
        result = min(result, nums[mid])

        # check left and right portions, compare with mid
        # if mid larger than left value, then it's part of the left sorted portion -> search right
        if nums[mid] >= nums[left]:
            # re-assign left to right portion (mid is assigned in next loop)
            left = mid + 1
        else:
            # re-assign right to left portion (mid is assigned in next loop)
            right = mid - 1

    return result


def main():
    print(findMin(nums=[3, 4, 5, 1, 2]), "expected 1")
    print(findMin(nums=[4, 5, 6, 7, 0, 1, 2]), "expected 0")
    print(findMin(nums=[11, 13, 15, 17]), "expected 11")


if __name__ == "__main__":
    main()
