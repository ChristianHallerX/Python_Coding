'''
33. Search in Rotated Sorted Array (medium)

There is an integer array 'nums' sorted in ascending order (with distinct values).

Prior to being passed to your function, 'nums' is possibly rotated at an unknown pivot index 'k' (1 <= k < nums.length)

such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).

For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array 'nums' after the possible rotation and an integer target, return the index of target if it is in 'nums',

or -1 if it is not in 'nums'.

You must write an algorithm with O(log n) runtime complexity.
'''


def search(nums: list[int], target: int) -> int:
    ''' return the index of the target in nums with binary search'''
    # initialize pointers (indices)
    left_pointer = 0
    right_pointer = len(nums)-1

    # binary search with while loop using pointers, will stop when array length is only one element -> l==r
    while left_pointer <= right_pointer:

        # assign mid_pointer
        mid_pointer = (left_pointer + right_pointer) // 2

        # narrowed down to final element, mid pointer is target
        if target == nums[mid_pointer]:
            return mid_pointer

        # check on which side of the list we need to search, left or right
        # mid_pointer and left_pointer are in the left sorted portion
        if nums[left_pointer] <= nums[mid_pointer]:
            # search in right portion, update left pointer
            if target > mums[mid_pointer]:
                left_pointer = mid_pointer + 1
            # search in right portion, update left pointer
            elif target < nums[left_pointer]:
                left_pointer = mid_pointer + 1
            # search left portion, update right pointer
            else:
                right_pointer = mid - 1

        # mid_pointer is in the right sorted portion
        else:
            # search in left portion, update right pointer
            if target < nums[mid_pointer]:
                right_pointer = mid - 1
            # search in left portion, update right pointer
            elif target > nums[right_pointer]:
                right_pointer = mid - 1
            # search in right portion, update left pointer
            else:
                left_pointer = mid + 1
    # target not found
    return -1


def main():
    print(search(nums=[4, 5, 6, 7, 0, 1, 2]), target=0), 'expected: 4')
    print(search(nums=[4, 5, 6, 7, 0, 1, 2]), target=3), 'expected: -1')
    print(search(nums=[1]), target=0), 'expected: -1')


if __name__ == '__main__':
    main()
