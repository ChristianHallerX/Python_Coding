"""
1. Two Sum (easy)

Given an array of integers 'nums' and an integer 'target', return indices of the two numbers such that they add up to

'target'.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


def twoSum(nums, target):
    """
    The idea is to calculate fear each number the difference to target and
    compare to a dictionary of previously visited numbers.
    The dictionary contains all num values mapped to index (num:index).
    If the diff IS in the dict, return current num's index and diff's index from dict.
    If the diff is NOT in the dict, add the num: index.
    Time Complexity: O(n), where n is the number of elements in the array. Each element is visited only once.
    Space Complexity: O(n),  space used by the hash map to store up to n elements.
    """

    num_dict = {}  # num: index

    for i, num in enumerate(nums):

        diff = target - num

        if diff in num_dict:
            # return the pair of indices
            return [num_dict[diff], i]

        # did not find diff in dict, add current num: index to dict
        num_dict[num] = i


def main():
    print(twoSum(nums=[2, 7, 11, 15], target=9), " expected: [0,1]")
    print(twoSum(nums=[3, 2, 4], target=6), " expected: [1,2]")
    print(twoSum(nums=[3, 3], target=6), " expected: [0,1]")


if __name__ == "__main__":
    main()
