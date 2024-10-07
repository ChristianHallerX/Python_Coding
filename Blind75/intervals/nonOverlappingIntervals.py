"""
435. Non-overlapping Intervals (medium)

Given an array of intervals 'intervals' where 'intervals[i] = [start_i, end_i]', return the minimum number of
intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping.
For example, [1, 2] and [2, 3] are non-overlapping.
"""


def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    """
    Edge case for this problem: Same values/touching intervals are NOT overlapping.

    First sort the intervals list.
    Time complexity: O(nlogn)
    Count how many times ends are overlapping
    """
    result = 0
    prevEnd = intervals[0][1]
    intervals.sort()

    # Start looping at second interval
    for start, end in intervals[1:]:
        # Case 1 NOT overlapping
        if start >= prevEnd:
            # Nothing to do, just update prevEnd
            prevEnd = end
        # Case 2 Overlapping
        else:
            result += 1
            # Which end shall we keep? Compare the two ends (right sides of the intervals)
            # -> The shorter one/further to the left, that has lower probability to overlap with the next interval.
            prevEnd = min(end, prevEnd)

    return result


def main():
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print(eraseOverlapIntervals(intervals), "expected: 1")

    intervals = [[1, 2], [1, 2], [1, 2]]
    print(eraseOverlapIntervals(intervals), "expected: 2")

    intervals = [[1, 2], [2, 3]]
    print(eraseOverlapIntervals(intervals), "expected: 0")


if __name__ == "__main__":
    main()
