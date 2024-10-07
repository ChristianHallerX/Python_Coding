"""
57. Insert Interval (medium)

You are given an array of non-overlapping intervals 'intervals' where intervals[i] = [start_i, end_i] represent the
start and the end of the 'ith' interval and 'intervals' is sorted in *ascending* order by 'start_i'.
You are also given an interval 'newInterval = [start, end]' that represents the start and end of another interval.

Insert 'newInterval' into 'intervals' such that 'intervals' is still sorted in ascending order by 'start_i' and
'intervals' still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return 'intervals' after the insertion.

Note that you don't need to modify 'intervals' in-place. You can make a new array and return it.
"""


def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    """
    We are delivered exactly one new interval
    Loop through intervals and compare the new interval with each of them.
    Time complexity: O(n)
    Memory complexity: O(n) the result variable will be as long as the intervals + newInterval.
    """
    result = []

    # Iterate through intervals
    for i in range(len(intervals)):
        # Edge case 1: new interval goes before this interval.
        # End value of new interval is smaller than start of current interval (not overlapping on left)
        # Finish loop after inserting new interval to result and from current interval to end
        if newInterval[1] < intervals[i][0]:
            result.append(newInterval)
            return result + intervals[i:]
        # Edge case 2: new interval goes after this interval. May still overlap with intervals after.
        # Append the old interval to results (new interval cannot be appended yet, since it may overlap with following)
        elif newInterval[0] > intervals[i][1]:
            result.append(intervals[i])
        # Overlapping case, re-write newInterval with minimum of both left values and maximum of both right values
        # Cannot be appended to results yet, since it may overlap with following intervals.
        else:
            newInterval = [
                min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1]),
            ]

    result.append(newInterval)
    return result


def main():
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    print(insert(intervals, newInterval), "expected: [[1, 5],[6, 9]]")

    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    print(
        insert(intervals, newInterval),
        "expected: [[1, 2],[3, 10],[12, 16]], \n Explanation: Because the new interval"
        "[4,8] overlaps with [3, 5],[6, 7],[8, 10].",
    )


if __name__ == "__main__":
    main()
