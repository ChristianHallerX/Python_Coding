"""
56. Merge Intervals (medium)

Given an array of 'intervals' where 'intervals[i] = [start_i, end_i]', merge all overlapping intervals, and return an
array of the non-overlapping intervals that cover all the intervals in the input.
"""


def merge(intervals: list[list[int]]) -> list[list[int]]:
    result = []

    return result


def main():
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(merge(intervals), "expected: [[1, 6], [8, 10], [15, 18]]")

    intervals = [[1, 4], [4, 5]]
    print(merge(intervals), "expected: [[1, 5]]")


if __name__ == "__main__":
    main()
