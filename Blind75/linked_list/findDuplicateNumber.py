"""
287. Find the Duplicate Number (Medium)

Given an array of integers 'nums' containing 'n' + 1 integers where each integer is in the range [1, 'n'] inclusive.

There is only *one repeated number* in 'nums', return this repeated number.

You must solve the problem *without* modifying the array 'nums' and using only constant extra space.
"""


def findDuplicate(nums: list[int]) -> int:
    """
    The contraints make this problem HARD.
    Solution: Linked List cycle. Floyd's Algorithm.
        - A repeated value is equal to a linked list going back to an old node -> cycle
        - Identify the beginning of a cycle, which is the duplicate to return.
        - Phase 1: Use fast and slow pointer that will intersect each other (are equal).
        - Phase 2: Use first slow pointer (in same place) second slow pointer from 0 and move until intersect.
            Explanation: The distance from Phase 1 to cycle intersection and 0 to Phase 2 intersection is
            always equal.
    """
    # Phase 1: Slow and Fast pointers
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        # intersect pointers
        if slow == fast:
            break

    # Phase 2: Slow and Slow 2 pointers
    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]

        # intersect pointers
        if slow == slow2:
            return slow


def main():
    nums = [1, 3, 4, 2, 2]
    print(findDuplicate(nums), "expected: 2")

    nums = [3, 1, 3, 4, 2]
    print(findDuplicate(nums), "expected: 3")

    nums = [3, 3, 3, 3, 3]
    print(findDuplicate(nums), "expected: 3")


if __name__ == "__main__":
    main()
