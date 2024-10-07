"""
56. Merge Intervals (medium)

Given an array of 'intervals' where 'intervals[i] = [start_i, end_i]', merge all overlapping intervals, and return an
array of the non-overlapping intervals that cover all the intervals in the input.
"""


def merge(intervals: list[list[int]]) -> list[list[int]]:
    """
    Original 'intervals' is NOT sorted. Sort first.
    Does the current interval overlap with the previous interval (previous right val, vs current left value)
    Time complexity: O(nlogn) for sorting
    """
    # Sort by left value
    # intervals.sort(key=lambda i: i[0])
    intervals = sorted(intervals)
    # Prepopulate result with first value to avoid edge case
    result = [intervals[0]]

    for currStart, currEnd in intervals[1:]:
        # Compare current interval left value to the last interval's left value in outputs
        lastEnd = result[-1][1]

        # Overlapping case, update the end value in result
        if currStart <= lastEnd:
            result[-1][1] = max(lastEnd, currEnd)
        # Not overlapping case
        else:
            result.append([currStart, currEnd])

    return result


def main():
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(merge(intervals), "expected: [[1, 6], [8, 10], [15, 18]]")

    intervals = [[1, 4], [4, 5]]
    print(merge(intervals), "expected: [[1, 5]]")


if __name__ == "__main__":
    main()
