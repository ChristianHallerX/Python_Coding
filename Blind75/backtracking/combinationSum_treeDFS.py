"""
39. Combination Sum (medium)

Given an array of distinct integers 'candidates' and a target integer 'target', return a list of all unique
combinations of 'candidates' where the chosen numbers sum to 'target'.

You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.

Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150
combinations for the given input.
"""


def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    """
    Recursion Decision Tree, Depth First Search with Backtracking (removal of item)
    -------------------------------------------------------------------------------
    Time complexity: Worst case, tree may be as tall as 'target' (7x1, 7 splits) -> O(2^t)
    The same number may be picked multiple times, but all combinations must be unique.
    Challenge: How to eliminate duplicated combinations?
    A regular decision tree does NOT work because it creates duplicate combinations.
    Solution: Binary decision tree with backtracking for one branch.
    First branch normal, second branch skips the current number (index i)
    """
    # Global result list
    result = []

    def dfs(i, cur, total):
        # Each call we add a different candidate to cur list and if meets criteria, add to result list.
        # i = index of number in candidate list
        # cur = current combination list of candidates for this dfs call
        # total = sum of cur

        # Base case 1: successful, total sum of candidates matches target -> add to global var 'result'
        if total == target:
            result.append(cur.copy())  # copy, so the pop won't modify it
            return None
        # Base case 2: i reached end of candidates list, sum too large -> do nothing
        if i >= len(candidates) or total > target:
            return None

        # Include candidate number to cur list
        cur.append(candidates[i])

        # Branch1: Run DFS, tree branch left (add candidate to total sum)
        dfs(i, cur, total + candidates[i])

        # BACKTRACKING. Remove last number from cur list again
        cur.pop()

        # Branch2: Run DFS with next candidate index, tree branch right
        dfs(i + 1, cur, total)

    # Call DFS and append to result
    dfs(i=0, cur=[], total=0)
    return result


def main():
    print(
        combinationSum(candidates=[2, 3, 6, 7], target=7), "expected: [[2, 2, 3],[7]]"
    )

    print(combinationSum(candidates=[2], target=1), "expected: []")


if __name__ == "__main__":
    main()
