"""
1. Two Sum (easy)

Given an array of integers 'nums' and an integer 'target', return indices of the two numbers such that they add up to

'target'.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

def twoSum(nums, target):
    """
    Write all nums to hash_map and check if the diff of current num is already in hash_map
    iterate once over nums list -> time O(n)
    """
    hash_map = {}  # num : index

    for index, num in enumerate(nums):
        diff = target - num
        if diff in hash_map:
            # if the diff to current num is in hash_map,
            # then return the diff index and the current index from hash_map
            return [hash_map[diff], index]
        else:
            # basic operation:  if 'diff' is not in hash_map, then save 'num' and 'index' to hash_map
            hash_map[num] = index


def main():
    print(twoSum(nums=[2, 7, 11, 15], target=9), ' expected: [0,1]')
    print(twoSum(nums=[3, 2, 4], target=6), ' expected: [1,2]')
    print(twoSum(nums=[3, 3], target=6), ' expected: [0,1]')


if __name__ == '__main__':
    main()
