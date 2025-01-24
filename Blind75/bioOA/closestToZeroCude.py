"""
Closest to Zero

In this exercise you have to analyze records of temperature to find the closest to zero.

Implement the function 'compute_closest_to_zero(ts)' which takes an array of temperatures 'ts' an returns the
temperature closest to 0.

Constraints:
- If the array is empty, the function should return 0
- 0 <= ts size <= 10000
- If two temperatures are equally close to zero, the positive temperature must be returned. For example, if the input
    is -5 and 5, then 5 must be returned.
"""


def compute_closest_to_zero(ts):
    if not ts:  # Check if the array is empty
        return 0

    closest = ts[0]  # Initialize the closest value
    for temp in ts:
        # Compare absolute values and handle ties (positive preferred)
        if abs(temp) < abs(closest) or (abs(temp) == abs(closest) and temp > closest):
            closest = temp
    return closest


def main():
    ts = [-10, -5, 5, 8, 12]
    # Closest to 0: 5 (because both -5 and 5 are equidistant, positive 5 is preferred)
    print(compute_closest_to_zero(ts), "expected 5")  # Output: 5

    ts = [-3]
    # Closest to 0: -3 (only one element)
    print(compute_closest_to_zero(ts), "expected -3")  # Output: -3

    ts = []
    # Array is empty, return 0
    print(compute_closest_to_zero(ts), "expected 0")  # Output: 0

    ts = [-7, -3, -4, -1]
    # Closest to 0: -1 (smallest absolute value)
    print(compute_closest_to_zero(ts), "expected -1")  # Output: -1

    ts = [-6, 4, -4, 3, -3]
    # Closest to 0: 3 (because 3 and -3 are equally close, positive is preferred)
    print(compute_closest_to_zero(ts), "expected 3")  # Output: 3

    ts = [0, -10, 10]
    # Closest to 0: 0 (it's exactly 0)
    print(compute_closest_to_zero(ts), "expected 0")  # Output: 0

    ts = [-1000, -999, 1, 2, 999]
    # Closest to 0: 1 (smallest absolute value)
    print(compute_closest_to_zero(ts), "expected 1")  # Output: 1


if __name__ == "__main__":
    main()
