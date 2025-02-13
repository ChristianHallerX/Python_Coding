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

    k (int)    absolute difference between two nums

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    # init dict with frequency of each num. num:count
    num_frequency = {}

    for num in nums:
        num_frequency[num] = num_frequency.get(num, 0) + 1

    # init k-pairs count for result
    result = 0

    # iterate over unique keys (nums) in dict
    for num in num_frequency:

        # k is greater 0, num1 and num2 are different from each other
        if k > 0 and (num + k) in num_frequency:
            result += 1

        # k is 0, num1 and num2 are identical. Do we have num at frequency > 2 in the dict?
        elif k == 0 and num_frequency[num] > 1:
            result += 1

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
