"""
Array Challenge

Have the function 'ArrayChallenge(arr)' read the array of number stored in 'arr' which will contain a sliding
window size "N" as the first element in the array and the rest will be a list of numbers. Your program should
return the Moving Median for each element based on the element and its N-1 predecessors, where N is the sliding
window size. The final output should be a string with the moving median corresponding to each entry in the
original array separated by commas.

Note that the for the first elements (until the window size is reached), the median is computed on a smaller number
of entries. For example: if arr is [3, 1, 3, 5, 10, 6, 4, 3, 1] then your program should output "1,2,3,5,6,6,4,3".

Examples:
    Input: [5, 2, 4, 6]
    Output: 2,3,4

    Input: [3, 0, 0, -2, 0, 2, 0, -2]
    Output: 0,0,0,0,0,0
"""


def ArrayChallenge(arr):
    # Extract the window size N and the list of numbers
    N = arr[0]
    numbers = arr[1:]

    # List to store the results
    result = []

    # Calculate the moving median
    for i in range(len(numbers)):

        # Define the current sliding window
        window = numbers[max(0, i - N + 1) : i + 1]

        # Sort the window and find the median
        window.sort()
        mid = len(window) // 2

        if len(window) % 2 == 0:
            median = (window[mid - 1] + window[mid]) / 2
        else:
            median = window[mid]

        # Append the median to the result
        result.append(int(median))

    # Convert the result to a comma-separated string
    return ",".join(map(str, result))


# Example usage
print(ArrayChallenge([5, 2, 4, 6]), "expected: 2,3,4")
print(ArrayChallenge([3, 0, 0, -2, 0, 2, 0, -2]), "expected: 0,0,0,0,0,0,0")
