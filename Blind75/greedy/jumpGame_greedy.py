"""
55. Jump Game (medium)

You are given an integer array 'nums'.

You are initially positioned at the array's first index, and each element in the array represents your *maximum*
jump length at that position.

Return 'True' if you can reach the last index, or 'False' otherwise.
"""


def canJump(nums: list[int]) -> bool:
    """
    Brute Force O(n^n)
    DP with cache O(n^2)
    -> greedy bottom-up solution O(n)
    Note: You can jump LESS than the value at a given index. Finding ONE path is enough if there are multiple.
    Bottom Up Greedy Intuition: Work in reverse starting from last index.
        Move goalIndex backwards: can you reach this intermediate index (goalIndex) given the jump value
        at a current index?
        If you can reach for each step, then the goalIndex will reach index 0 and we can return True.
    """
    # Init goal at last index
    goalIndex = len(nums) - 1

    # Reverse loop over nums
    for i in range(len(nums) - 1, -1, -1):
        # Is current index plus jump value at current index larger than goalIndex? Can the jump reach the goal?
        if i + nums[i] >= goalIndex:
            # Yes, move goalIndex backwards to current index (do not move goalIndex if jump value does not reach goal)
            goalIndex = i

    # True if goalIndex was moved all the way to start of nums, False if it got stuck (>0)
    return True if goalIndex == 0 else False


def main():
    nums = [2, 3, 1, 1, 4]
    print(
        canJump(nums),
        "expected: True, \n Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.",
    )

    nums = [3, 2, 1, 0, 4]
    print(
        canJump(nums),
        "expected: False, \n Explanation: You will always arrive at index 3 no matter what."
        "Its maximum jump length is 0, which makes it impossible to reach the last index.",
    )


if __name__ == "__main__":
    main()
