def fibonacci(n: int):
    """
    Generate the Fibonacci sequence from index 0 to n (inclusive) Iterative bottom up.

    Parameters:
        n (int): A non-negative integer representing the last index in the Fibonacci sequence.
    Returns:
        list: A list containing the Fibonacci sequence from index 0 to n.

    Time Complexity: O(n)
    Space Complexity: O(1), only two variables plus output list
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")

    sequence = []
    a, b = 0, 1
    for _ in range(n + 1):
        sequence.append(a)
        a, b = b, a + b  # Update values for the next number in the sequence
    return sequence


def fib_recursive(n: int, memo=None) -> int:
    """
    Calculate the n-th Fibonacci number.

    Time Complexity: O(n)
    Space Complexity: O(n) uses the dictionary to save time
    """
    # Init dict if not there yet
    if memo is None:
        memo = {}

    # Read from dict
    if n in memo:
        return memo[n]

    # Base case
    if n <= 1:
        return n

    # Recursive call top down
    memo[n] = fib_recursive(n - 1, memo) + fib_recursive(n - 2, memo)

    return memo[n]


if __name__ == "__main__":
    n = 10
    print(fibonacci(n))

    n = 100
    print(fibonacci(n))

    n = 10
    print(fib_recursive(10))
