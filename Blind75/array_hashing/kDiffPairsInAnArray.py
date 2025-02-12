"""
532. K-diff Pairs in an Array (Medium)

Given an array of integers 'nums' and an integer 'k', return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

- 0 <= i, j < nums.length
- i != j
- |nums[i] - nums[j]| == k

Notice that |val| denotes the absolute value of val.
"""


def findPairs(nums: list[int], k: int) -> int:
    """
    Find number of pairs
    """
    result = 0

    return result


def main():
    nums = [3, 1, 4, 1, 5]
    k = 2
    print(findPairs(nums, k), "expected: 2")

    nums = [1, 2, 3, 4, 5]
    k = 1
    print(findPairs(nums, k), "expected: 4")

    nums = [1, 3, 1, 5, 4]
    k = 0
    print(findPairs(nums, k), "expected: 1")


if __name__ == "__main__":
    main()
