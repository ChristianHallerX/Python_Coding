"""
253. Meeting Rooms II (medium)

Compare to LintCode 919

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.
"""


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


def createIntervalObjects(list_of_lists):
    """
    Helper function to crate list of Objects.
    """
    return [Interval(start, end) for start, end in list_of_lists]


def minMeetingRooms(intervals: list[Interval]) -> int:
    """
    Get the max count of concurrent meetings.
    Sort intervals.
    Loop through intervals and add all start times to a start list and end times to end list.
    Use start pointer and end pointer and compare values ath them. Update a concurrentRooms counter.
    Time complexity: sorting O(nlogn), logic O(n) -> total O(nlogn)
    """
    # Fill all start times and end times into sorted lists respectively
    start = sorted([i.start for i in intervals])
    end = sorted([i.end for i in intervals])

    maxConcurrent, count = 0, 0
    startPointer, endPointer = 0, 0

    while startPointer < len(intervals):
        # Case 1: start time is before previous end (with overlap)
        if start[startPointer] < end[endPointer]:
            startPointer += 1
            count += 1
        # Case 2: start time is after previous end (no overlap)
        else:
            endPointer += 1
            count -= 1

        maxConcurrent = max(maxConcurrent, count)

    return maxConcurrent


def main():
    listOfLists = [[0, 30], [5, 10], [15, 20]]
    listOfObjects = createIntervalObjects(listOfLists)
    print(minMeetingRooms(listOfObjects), "expected: 2")

    listOfLists = [[7, 10], [2, 4]]
    listOfObjects = createIntervalObjects(listOfLists)
    print(minMeetingRooms(listOfObjects), "expected: 1")


if __name__ == "__main__":
    main()
