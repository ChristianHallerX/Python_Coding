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
    # return the minimum element in O(log n) time -> binary search, non-traditional
    left_p, right_p = 0, len(nums) - 1
    result = nums[0] # initiate with arbitrary value in nums

    while left_p <= right_p:

        # both pointers are in the same portion, the left_p is the smallest num -> define as result
        if nums[left_p] < nums[right_p]:
            result = min(result, nums[left_p])
            break

        # establish middle_p and then decide if moving left or right
        middle_p = (right_p - left_p) // 2
        #result = min(result, nums[middle_p])

        # middle is in left portion if middle is larger than left (because sorted sorted)
        if nums[middle_p] > nums[left_p]:
            # when in left portion, this never contains the lowest num at index 0,
            # set left_p to right of middle_p and search
            left_p = middle_p + 1

        # middle is in right portion if the left is greater than middle
        # (everything in the right portion is smaller than the smallest left num at index 0)
        else:
            # set right_p to the left of middle_p
            right_p = middle_p - 1
    return result


def main():
    print(findMin(nums=[3, 4, 5, 1, 2]), 'expected 1')
    print(findMin(nums=[4, 5, 6, 7, 0, 1, 2]), 'expected 0')
    print(findMin(nums=[11, 13, 15, 17]), 'expected 11')


if __name__ == '__main__':
    main()
