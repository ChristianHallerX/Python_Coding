"""
268. Missing Number (easy)

Given an array_hashing 'nums' containing 'n' distinct numbers in the range [0, n], return the only number in the range
that is missing from the array_hashing.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""


def missingNumber(nums: list[int]) -> int:
    """
    Solution 1: Create set of expected numbers 0-len(nums), then loop over nums and drop each number from nums until
    missing number is left in 0-len(nums).
    Time complexity: O(n)
    Space complexity: O(n)

    Solution 2: XOR binary (returns binary 1 for each bin position if different)
    Iterate range(len(nums)) and xor with 000 binary returns the same number.
    With any other number returns something else -> the missing number.
    Time complexity: O(n)
    Memory complexity: O(1)

    ----> Solution 3: EASIEST sum(range(len(nums))) - sum(nums) = missing number
    Time complexity: O(1)
    Memory complexity: O(n) range
    """
    result = len(nums)

    # Use only one loop, index i replaces the range(nums)
    # Adding up all i is like the sum(range(nums)), subtracting the nums[i] will leave the missing number left over
    for i in range(len(nums)):
        result += i - nums[i]
    return result


def main():
    nums = [3, 0, 1]
    print(
        missingNumber(nums),
        "expected: 2\n"
        "Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0, 3].\n"
        "2 is the missing number in the range since it does not appear in nums.\n",
    )

    nums = [0, 1]
    print(
        missingNumber(nums),
        "expected: 2\n"
        "Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0, 2].\n"
        "2 is the missing number in the range since it does not appear in nums.\n",
    )

    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(
        missingNumber(nums),
        "expected: 8\n"
        "Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9].\n"
        "8 is the missing number in the range since it does not appear in nums.\n",
    )


if __name__ == "__main__":
    main()
