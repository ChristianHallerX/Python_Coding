"""
128. Longest Consecutive Sequence (medium, formerly hard??)

Given an unsorted array of integers 'nums', return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time. -> cannot sort since that is O(nlogn)

Time: O(2n) -> O(n)
Space: set and the longest seq -> O(2n) -> O(n)
"""

def longestConsecutive(nums: list[int]) -> int:
    """
    Mentally divide nums into sub-sequences. Check if each number has a smaller number in the set.
    If smaller not present, then it's a seq start and start counter upwards that checks presence of following element.
    The set data structure makes element lookup an O(n) time
    """
    numSet = set(nums)
    longest_seq = 0

    # visit every num once
    for num in nums:
        # check if num is start of seq (num below is not present in set)
        if (num - 1) not in numSet:
            # this IS a sequence, get length, visit every num a second time
            seq_len = 0
            while (num + seq_len) in numSet:
                seq_len += 1
            longest_seq = max(seq_len, longest_seq)

    return longest_seq


def main():
    print(longestConsecutive(nums=[100, 4, 200, 1, 3, 2]), " expected: 4")
    print(longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), " expected: 9")


if __name__ == '__main__':
    main()
