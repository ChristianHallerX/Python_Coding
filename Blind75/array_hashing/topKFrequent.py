"""
347. Top K Frequent Elements (medium)

Given an integer array 'nums' and an integer 'k', return the 'k' most frequent elements.

You may return the answer in any order.
"""


def topKFrequent(nums: list[int], k: int) -> list[int]:
    hash_map = {}  # number: count
    freq = [[]] * (len(nums) + 1)  # list of lists of length of nums

    # populate hash_map
    for n in nums:
        hash_map[n] = 1 + hash_map.get(
            n, 0
        )  # loop through numbers and add 1 to previous value, default 0

    # write to frequency list of lists
    for number, count in hash_map.items():
        freq[count].append(number)

    # go backwards through frequency list of lists(-1) and start with the highest frequency
    result = []
    for i in range(len(freq) - 1, 0, -1):
        # loop through inner lists
        for n in freq[i]:
            result.append(n)
            if len(result) == k:
                return result


def main():
    print(topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2), "expected: [1,2]")
    print(topKFrequent(nums=[1], k=1), "expected: [1]")


if __name__ == "__main__":
    main()
