"""
15. 3Sum (medium) (updated description)

Given an integer array 'nums', return all the triplets [nums[i], nums[j], nums[k]] such that

i != j,
i != k,
j != k, and
nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


def threeSum(nums):
    """
    First, sort the  array. O(n) = nlogn
    Keep a pointer ('i') fixed on left (negative num) and use as target. (loop, O(n))
    The rest is effectively 'TwoSumII', which uses a sorted array.
        Move a left ('j') and right ('k') pointer through remainder of the array. (loop, O(n))
    Time complexity O(n) = nlogn + n * n -> n**2
    Space complexity: if sorting library DOES take memory: O(n), if it does not O(1)
    Will not pass with three loops, one for each index, O(n^3)
    """
    # initialize list (of lists)
    result = []
    nums = sorted(nums)

    for index, i in enumerate(nums):
        # the 'i' pointer has to be negative and can't use same twice (after sorting, same are next to each other)
        if i > 0 and i == nums[i - 1]:
            continue

        # run TwoSumII
        # 'j' starts on the left of array one after 'i', 'k' starts at end of array
        left_pointer_j, right_pointer_k = index + 1, len(nums) - 1

        while left_pointer_j < right_pointer_k:
            threeSum = i + nums[left_pointer_j] + nums[right_pointer_k]

            if threeSum > 0:
                right_pointer_k -= 1
            elif threeSum < 0:
                left_pointer_j += 1
            else:
                # threeSum == 0, sort the nums and append as tuple -> only tuples can be used as set() to dedup
                result.append(tuple([i, nums[left_pointer_j], nums[right_pointer_k]]))
                # update left pointer only, don't let left pointer cross right pointer (again)
                left_pointer_j += 1
                # update left pointer if multiple nums are equal next to each other -> speedup
                while nums[left_pointer_j] == nums[left_pointer_j - 1] and left_pointer_j < right_pointer_k:
                    left_pointer_j += 1
    # dedup with set and convert back to list of lists
    return [list(i) for i in list(set(result))]


def main():
    print(threeSum(nums=[-1, 0, 1, 2, -1, -4]), 'Expected [[-1,-1, 2], [-1, 0, 1]]')
    print(threeSum(nums=[0, 1, 1]), 'Expected []')
    print(threeSum(nums=[0, 0, 0]), 'Expected [[0, 0, 0]]')
    print(threeSum(nums=[0]), 'Expected []')


if __name__ == '__main__':
    main()
