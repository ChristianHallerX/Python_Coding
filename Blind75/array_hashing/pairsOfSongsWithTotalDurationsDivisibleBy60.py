"""
1010. Pairs of Songs With Total Durations Divisible by 60 (Medium)

You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.
Formally, we want the number of indices 'i', 'j' such that 'i' < 'j' with (time[i] + time[j]) % 60 == 0.
"""


def numPairsDivisibleBy60(time: list[int]) -> int:
    """
    Similar to 2Sum, but with modulo.
    """
    # count of pairs init
    result_count = 0
    # remainder: count
    frequency_dict = {}

    for t in time:
        remainder = t % 60
        complement = (60 - remainder) % 60

        # if complement is already in dict then read the count and add it to the result_count
        if complement in frequency_dict:
            result_count += frequency_dict[complement]
        # Always increment the count in the dict
        frequency_dict[remainder] = frequency_dict.get(remainder, 0) + 1

    return result_count


def main():
    time = [30, 20, 150, 100, 40]
    print(numPairsDivisibleBy60(time), "expected: 3")

    time = [60, 60, 60]
    print(numPairsDivisibleBy60(time), "expected: 3")


if __name__ == "__main__":
    main()
