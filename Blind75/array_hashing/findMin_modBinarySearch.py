"""
153. Find Minimum in Rotated Sorted Array (medium)

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example,

the array 'nums' = [0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2],
..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

"""


def findMin(nums: list[int]) -> int:
    # modified binary_search

    # Initialize with an arbitrary value
    res = nums[0]

    # Initialize pointer index of binary_search at ends of list
    left_pointer, right_pointer = 0, len(nums) - 1

    # Continue while pointer indices in valid position
    while left_pointer <= right_pointer:
        #  Subarray already sorted, left is lowest, compare with res
        if nums[left_pointer] < nums[right_pointer]:
            res = min(res, nums[left_pointer])
            break

        # Subarray not sorted, do binary_search
        mid_pointer = (left_pointer + right_pointer) // 2
        res = min(res, nums[mid_pointer])
        # Is the mid a part of the left sorted portion? that means left pointer is smaller than mid. then search right
        if nums[mid_pointer] >= nums[left_pointer]:
            # re-assign left pointer to mid plus one
            left_pointer = mid_pointer + 1
        # if the left pointer is smaller than left, then search left
        else:
            # Re-assign right pointer to mid minus one
            right_pointer = mid_pointer - 1

    return res


def main():
    print(findMin(nums=[3, 4, 5, 1, 2]), "expected: 1")
    print(findMin(nums=[4, 5, 6, 7, 0, 1, 2]), "expected: 0")
    print(findMin(nums=[11, 13, 15, 17]), "expected: 11")


if __name__ == "__main__":
    main()
