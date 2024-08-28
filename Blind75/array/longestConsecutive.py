"""
128. Longest Consecutive Sequence (medium, formerly hard, asked by Google)

Given an unsorted array of integers 'nums', return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time. -> cannot sort since that is O(nlogn)
"""


def longestConsecutive(nums: list[int]) -> int:
    """
    longest consecutive sequence = monotonously increasing when sorted from anywhere in the array
    Original order of input array does not matter.
    Sorting is not allowed, because it is O(nlogn).

    Iterating once over nums, time complexity O(n)
    Create a set, memory complexity O(n)
    """

    # Convert nums to set
    nums_set = set(nums)

    longest_length = 0

    # Loop over nums list and check if num is start.
    for num in nums:

        # Start of sequence if no smaller value exists in set
        if num - 1 not in nums_set:
            length = 0

            # Follow the sequence
            while (num + length) in nums_set:
                length += 1

            # Update longest length with current sequence
            longest_length = max(longest_length, length)

    return longest_length


def main():
    print(longestConsecutive(nums=[100, 4, 200, 1, 3, 2]), " expected: 4")
    print(longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), " expected: 9")


if __name__ == "__main__":
    main()
