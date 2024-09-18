"""
39. Combination Sum (medium)

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations
of candidates where the chosen numbers sum to target.

You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.

Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150
combinations for the given input.
"""


def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    return None


def main():
    print(combinationSum(candidates=[2, 3, 6, 7], target=7), "expected: [[2,2,3],[7]]")

    print(combinationSum(candidates=[2], target=1), "expected: []")


if __name__ == "__main__":
    main()
