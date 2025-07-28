"""
78. Subsets (Medium)

Given an integer array 'nums' of unique elements, return all possible "subsets" (the power set).

The solution set must not contain duplicate subsets.

Return the solution in any order.
"""


def subsets(nums: list[int]) -> list[list[int]]:
    """
    Backtracking, Depth First Search
    Decision tree of adding an element (value at index in nums) and adding empty element.

    In a subset, order does not matter, [2,1] is equal to [1,2]. This is NOT a permutation.
    [1, 2, 3] n elements. We can include or not include each element -> 2**n subsets, length n --> n * 2**n

    Time Complexity: O(n* 2**n)
    """
    result = []

    # global access list in dfs function
    subset = []

    def dfs(i):
        # i is the index in nums of the value we are making a decision on

        # Base case, out of bounds
        if i >= len(nums):
            result.append(subset.copy())
            return

        # Decision to include nums[i] (left leaf of tree)
        subset.append(nums[i])
        # Run DFS on next lower node left
        dfs(i + 1)

        # Decision NOT to include nums[i] (right leaf of tree)
        subset.pop()  # BACKTRACKING remove the element in subset we just appended
        # Run DFS on next lower node right
        dfs(i + 1)

    # Run dfs and populate 'result'
    dfs(0)
    return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(subsets(nums), "expected: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]")

    nums = [0]
    print(subsets(nums), "expected: [[], [0]]")
