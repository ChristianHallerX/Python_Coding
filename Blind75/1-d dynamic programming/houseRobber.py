"""
198. House Robber (medium, was easy)

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them
is that adjacent houses have security systems connected and it will automatically contact the police if
two adjacent houses were broken into on the same night.

Given an integer array 'nums' representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.
"""


def rob(nums: list[int]) -> int:
    """
    Decision tree with values and totals.
    Pick a house, then solve a sub-problem of the remaining houses. rob = max(nums[0] + rob[2:])
    Solve all the sub-problems to solve the problem.
    Only maintain the last two max we can rob from.
    Time complexity: O(n) linear


    Memory complexity: O(1) constant, no data structures used.
    """
    rob1, rob2 = 0, 0

    # Example nums [rob1, rob2, n, n+1, ...]
    for n in nums:
        # The first option (rob1+n) skips rob2 because of the alarm
        # The second option, (rob2) skips rob1 and n because of the alarm
        temp = max(rob1 + n, rob2)
        # Iterate to next position in 'nums', fill in the contents of the variables to the right in the list
        rob1 = rob2
        # Update rob2 to n
        rob2 = temp

    # When the loop reaches the end of nums, rob2 will contain the highest value you can rob
    return rob2


def main():
    nums = [1, 2, 3, 1]
    print(rob(nums), "expected: 4")

    nums = [2, 7, 9, 3, 1]
    print(rob(nums), "expected: 12")

    nums = [2, 1, 1, 2]
    print(rob(nums), "expected: 4")


if __name__ == "__main__":
    main()
