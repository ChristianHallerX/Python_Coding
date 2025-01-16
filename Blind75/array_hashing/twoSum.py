"""
1. Two Sum (easy)

Given an array of integers 'nums' and an integer 'target', return indices of the two numbers such that they add up to
'target'.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


def twoSum(nums, target):
    """
    Intuition: Calculate for each num the diff to target and search in dict (diff:index) if this num and
    index exists yet. If yes, return current index and diff index from dict. If not, write num:index to dict.
    Time Complexity: O(n), where n is the number of elements in the array_hashing. Each element is visited only once.
    Space Complexity: O(n),  space used by the hash map to store up to n elements.
    """
    # key = num, value = index
    num_dict = {}

    for i, num in enumerate(nums):

        # calc current value's difference missing to add up to 'target'
        diff = target - num

        # Diff found
        if diff in num_dict:
            # Return index pair: index of 'diff' and current 'num''s index (thanks to enumerate())
            return [num_dict[diff], i]

        # Diff Not found. Add current to dict
        num_dict[num] = i


def main():
    print(twoSum(nums=[2, 7, 11, 15], target=9), " expected: [0,1]")
    print(twoSum(nums=[3, 2, 4], target=6), " expected: [1,2]")
    print(twoSum(nums=[3, 3], target=6), " expected: [0,1]")


if __name__ == "__main__":
    main()
