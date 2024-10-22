"""
853. Car Fleet (medium)

There are 'n' cars at given miles away from the starting mile 0, traveling to reach the mile 'target'
(all on same road and same direction).

You are given two integer array 'position' and 'speed', both of length 'n', where 'position[i]' is the
starting mile of the ith car and 'speed[i]' is the speed of the 'ith' car in miles per hour.

A car CANNOT pass another car, but it can catch up and then travel next to it at the speed of the slower car.

A car fleet is a car or cars driving next to each other.
The speed of the car fleet is the minimum speed of any car in the fleet.

Edge Case:
    If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.

---> Return the number of car fleets that will arrive at the destination.

"""


def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    """
    Intuition:  If two cars intersect each other before the target, they become a car fleet.
                If a far car arrives before a close car, then they must catch up as fleet.
    Reverse sort by position (high->low position / close->far from target) and start looping.
    Calculate all arrival times at target-> append to stack and pop if a fleet is formed.
    Delete the faster car from stack (it's part of the fleet now), keep the slower, since both cars keep
    driving at slowest speed as single fleet unit.
    Length of stack is result of number of fleets.
    Time complexity: O(n) and sorting O(nlogn) -> total O(nlogn)
    Space complexity: O(n) for stack
    """
    # Pair up position and speed of each car in list of lists
    pair = [[p, s] for p, s in zip(position, speed)]

    stack = []

    # reverse/high>low sorted order through cars
    for p, s in sorted(pair)[::-1]:
        # Calc arrival time at destination, distance divided by speed
        stack.append((target - p) / s)
        # if latest arrival time is earlier than bottom of stack arrival time, then it's a catchup fleet.
        if len(stack) > 1 and (stack[-1] <= stack[-2]):
            stack.pop()

    return len(stack)


def main():
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    print(carFleet(target, position, speed), "expected: 3")

    target = 10
    position = [3]
    speed = [3]
    print(carFleet(target, position, speed), "expected: 1")

    target = 100
    position = [0, 2, 4]
    speed = [4, 2, 1]
    print(carFleet(target, position, speed), "expected: 1")


if __name__ == "__main__":
    main()
