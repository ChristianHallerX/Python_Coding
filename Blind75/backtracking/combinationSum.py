"""
39. Combination Sum (medium)

Given an array of distinct integers 'candidates' and a target integer 'target', return a list of all unique combinations
of 'candidates' where the chosen numbers sum to 'target'.

You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.

Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150
combinations for the given input.
"""


def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    """
    Solution: Recursion Tree, Depth First Search
    Time complexity: Worst case, tree may be as tall as 'target' (7x1, 7 splits) -> O(2°t)
    The same number may be picked multiple times, but all combinations must be unique.
    How to eliminate duplicated combinations?
    Backtracking means adding a number and not adding a number/skipping.
    """
    # Global result
    result = []

    def dfs(i, cur, total):
        # Each call we add a different candidate to cur list
        # i = index of candidate, cur = current combination of candidates for this dfs call, total = sum of cur

        # Base case successful, add to global var 'result'
        if total == target:
            result.append(cur.copy())
            return None
        # Base case sum too large, do nothing
        if i >= len(candidates) or total > target:
            return None

        # Run DFS Recursive tree
        # Append candidate number to cur list
        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])

        # Do not append candidate number
        cur.pop()
        dfs(i + 1, cur, total)

    dfs(i=0, cur=[], total=0)
    return result


def main():
    print(
        combinationSum(candidates=[2, 3, 6, 7], target=7), "expected: [[2, 2, 3],[7]]"
    )

    print(combinationSum(candidates=[2], target=1), "expected: []")


if __name__ == "__main__":
    main()
