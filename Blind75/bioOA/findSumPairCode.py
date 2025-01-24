"""
Find Sum pair (aka Two Sum)

In this problem, you'll be given a list of positive integers and a separate integer, 'k',
and tasked with finding whether there is a pair of integers in the list that sums exactly to 'k'


"""

from typing import List


def find_sum_pair(numbers: List[int], k: int) -> List[int]:
    # Use a dictionary to store numbers and their indices
    num_to_index = {}

    for index, number in enumerate(numbers):
        # Calculate the complement that would add up to k
        complement = k - number

        # Check if the complement exists in the dictionary
        if complement in num_to_index:
            # Return the indices as required, the lower index first
            return [num_to_index[complement], index]

        # Store the current number and its index in the dictionary
        num_to_index[number] = index

    # Return [0, 0] if no pair is found
    return [0, 0]


def main():
    # Example input
    numbers = [1, 5, 8, 1, 2]
    k = 13
    print(find_sum_pair(numbers, k), "indices expected: [1, 2]")


if __name__ == "__main__":
    main()
