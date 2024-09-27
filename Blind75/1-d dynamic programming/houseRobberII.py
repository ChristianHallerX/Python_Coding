"""
213. House Robber II (medium)

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.
All houses at this place are arranged in a *circle*.
That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected, and it will automatically
contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.
"""


def rob(nums: list[int]) -> int:
    """
    Like House Robber I, twist circle street (first house is connected to the last house)
    Re-use House Robber I as helper function.
    Choose the higher value of inputs:
        (1) include first house and skip last house nums[:-1],
        (2) skip first and include last house nums[1:].
    Return the max of two inputs
    Time complexity: O(2n) -> O(n) linear
    Memory complexity: O(1) constant, no data structures used.
    """

    def robHelper(nums: list[int]) -> int:
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

    # Edge case: nums[0] is for nums has only single value like nums = [1]
    return max(nums[0], robHelper(nums[:-1]), robHelper(nums[1:]))


def main():
    nums = [2, 3, 2]
    print(rob(nums), "expected 3")

    nums = [1, 2, 3, 1]
    print(rob(nums), "expected 4")

    nums = [1, 2, 3]
    print(rob(nums), "expected 3")

    nums = [2]
    print(rob(nums), "expected 2")


if __name__ == "__main__":
    main()
