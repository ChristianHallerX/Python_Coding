"""
3159. Find Occurrences of an Element in an Array (Medium)

You are given an integer array 'nums', an integer array 'queries', and an integer 'x'.

For each queries[i], you need to find the index of the queries[i]th occurrence of x in the nums array.
If there are fewer than queries[i] occurrences of 'x', the answer should be -1 for that query.

Return an integer array answer containing the answers to all queries.
"""


def occurrencesOfElement(nums: list[int], queries: list[int], x: int) -> list[int]:
    """
    x (int)    number to find in nums, target value
    queries (list of ints)    ith instance of target value to be found

    Return a list containing the indices of the ith 'x' to all queries

    Time Complexity: O(n + m), list comp O(n), loop queries m O(m)
    Space Complexity: O(n + m) if considering result, indices list O(n), result O(m)
    """
    # Create a list of indices where x occurs. Skip all non-x values (does not require a dict)
    indices = [i for i, num in enumerate(nums) if num == x]

    result = []
    # make sure the q is smaller than the occurrences of x in nums
    for q in queries:
        if q <= len(indices):
            # Since lists are zero-indexed, the q-th occurrence is at index q-1.
            result.append(indices[q - 1])
        else:
            # If there are fewer than q occurrences of x, append -1.
            result.append(-1)

    return result


def main():
    nums = [1, 3, 1, 7]
    queries = [1, 3, 2, 4]
    x = 1
    print(occurrencesOfElement(nums, queries, x), "expected: [0,-1,2,-1]")

    nums = [1, 2, 3]
    queries = [10]
    x = 5
    print(occurrencesOfElement(nums, queries, x), "expected: [-1]")


if __name__ == "__main__":
    main()
