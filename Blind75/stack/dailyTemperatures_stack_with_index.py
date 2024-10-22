"""
739. Daily Temperatures (medium)

Given an array of integers 'temperatures' represents the daily temperatures, return an array 'answer' such that
'answer[i]' is the number of days you have to wait after the 'ith' day to get a warmer temperature.
If there is no future day for which this is possible, keep 'answer[i] == 0' instead.
"""


def dailyTemperatures(temperatures: list[int]) -> list[int]:
    """
    Solution 1:  Nested loops.
        Time complexity: O(n^2)
    Solution 2 Optimized: (monotonically decreasing) stack (extra space complexity)
        Time Complexity: O(n) linear
        Create stack and results list with length of 'temperatures' and default 0 values.
        Add 'temperature value + index to stack'. Move to next val and compare size to stack val.
        If temperature value larger, write index distance to results and pop from stack.
        If temp val smaller, do nothing, continue, will leave hole in 'results'
        Non-Filled in values will remain default 0
    """
    result = [0] * len(temperatures)
    # Will contain pairs [temp, index] list of lists, index to measure difference
    stack = []

    for i, temp in enumerate(temperatures):
        # This temp value is larger than the last stack value (index into sub-list), repeat if getting larger
        while stack and temp > stack[-1][0]:
            stackTemp, stackIndex = stack.pop()
            # Get index difference between current and stack and write to result
            result[stackIndex] = i - stackIndex
        # Always add to stack, no matter larger or not
        stack.append([temp, i])

    return result


def main():
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(dailyTemperatures(temperatures), "expected: [1, 1, 4, 2, 1, 1, 0, 0]")

    temperatures = [30, 40, 50, 60]
    print(dailyTemperatures(temperatures), "expected: [1, 1, 1, 0]")

    temperatures = [30, 60, 90]
    print(dailyTemperatures(temperatures), "expected: [1, 1, 0]")


if __name__ == "__main__":
    main()
