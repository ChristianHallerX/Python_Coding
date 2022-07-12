""" Leetcode 1. Two Sum
Given an array of integers 'nums' and an integer 'target', return indices of the two numbers such that they add up to

'target'.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

def twoSum(nums, target):
    hash_map = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in hash_map:
            return [i, hash_map[diff]]
        hash_map[num] = i


def main():
    print(twoSum(nums=[2,7,11,15], target=9))
    print(twoSum(nums=[3,2,4], target=6))
    print(twoSum(nums=[3,3], target=6))

if __name__ == '__main__':
    main()
