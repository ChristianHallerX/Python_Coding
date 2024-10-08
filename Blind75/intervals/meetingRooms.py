"""
252. Meeting Rooms (easy)

Alternative: LintCode 920

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
determine if a person could attend all meetings.
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


def canAttendMeetings(intervals: list[Interval]) -> bool:
    """
    time complexity: O(nlogn) for sorting. rest: O(n) -> total O(nlogn)
    """
    # Key has to be defined, otherwise exception
    intervals.sort(key=lambda interval: interval.start)

    # Iterate through the sorted intervals and check for overlaps. Start at index 1.
    for i in range(1, len(intervals)):
        prevInterval = intervals[i - 1]
        currInterval = intervals[i]

        # Overlap detected
        if prevInterval.end > currInterval.start:
            return False

    # No overlaps found - Loop never exited with False
    return True


def main():
    listOfLists = [[0, 30], [5, 10], [15, 20]]
    intervalObjectsList = createIntervalObjects(listOfLists)
    print(canAttendMeetings(intervalObjectsList), "expected: False")

    listOfLists = [[7, 10], [2, 4]]
    intervalObjectsList = createIntervalObjects(listOfLists)
    print(canAttendMeetings(intervalObjectsList), "expected: True")

    listOfLists = []
    interval_objects_list = createIntervalObjects(listOfLists)
    print(canAttendMeetings(interval_objects_list), "expected: True")

    listOfLists = [[1, 5]]
    interval_objects_list = createIntervalObjects(listOfLists)
    print(canAttendMeetings(interval_objects_list), "expected: True")

    listOfLists = [[1, 5], [5, 10], [10, 15], [14, 20]]
    interval_objects_list = createIntervalObjects(listOfLists)
    print(canAttendMeetings(interval_objects_list), "expected: False")


if __name__ == "__main__":
    main()
