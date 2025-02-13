"""
Active Lamps (Medium/Hard)

Similar to Leetcode My Calendar III

You are given a list of 'lamps' along a long street.

Each street lamp is represented by an interval [L,R][L,R] which indicates that the lamp illuminates every point
from LL to RR (inclusive).

In addition, you are provided with a list of control 'points' on the street.

Your task is to determine, for each 'point', how many street lamps are active (i.e. illuminating that point).

Implement a function that takes the list of street lamps and the list of control points, and returns
a list of counts.

The i-th count in the output should represent the number of lamps that cover the i-th control point.
"""


def activeLamps(lamps, points):
    """
    The Sweep Line algorithm is used to efficiently count the number of active intervals at any given point.
    In this solution, we treat the start and end of each lamp's range as events.
    We then sort these events and sweep through them, maintaining a count of active lamps.
    For each control point, we determine how many lamps are active at that point.

    lamps (list of lists)    each list contains the left/right interval of point coverage of a lamp
    points (list of ints)    position of control points where we measure active lamp coverage

    Return list of ints with counts of active lamps at each point.
    """

    # Initialize events list to store start and end of each lamp's range
    events = []

    # Iterate over each lamp to create events
    for lamp in lamps:
        # Add start event (+1) for the lamp
        events.append((lamp[0], 1))
        # Add end event (-1) for the lamp
        events.append((lamp[1] + 1, -1))

    # Sort events by position, breaking ties by type of event
    events.sort()

    # Initialize a dictionary to store the result for each point
    pointResults = {point: 0 for point in points}

    # Sort the points to process them in order
    sortedPoints = sorted(points)

    # Initialize activeLamps to keep track of the number of active lamps
    activeLamps = 0
    # Initialize index to track the current event
    eventIndex = 0

    # Iterate over each point in sorted order
    for point in sortedPoints:

        # Process all events that occur before or at the current point
        while eventIndex < len(events) and events[eventIndex][0] <= point:
            # Update activeLamps based on the event type
            activeLamps += events[eventIndex][1]
            # Move to the next event
            eventIndex += 1

        # Store the number of active lamps for the current point
        pointResults[point] = activeLamps

    # Return the results for each point in the original order
    return [pointResults[point] for point in points]


def main():
    lamps = [[1, 3], [2, 5], [6, 9]]
    points = [2, 4, 7]
    print(activeLamps(lamps, points), "expected: [2, 1, 1]")

    lamps = [[0, 2], [2, 4], [4, 6]]
    points = [1, 2, 3, 4, 5]
    print(activeLamps(lamps, points), "expected: [1, 2, 1, 2, 1]")

    lamps = [[10, 20]]
    points = [5, 10, 15, 25]
    print(activeLamps(lamps, points), "expected: [0, 1, 1, 0]")


if __name__ == "__main__":
    main()
