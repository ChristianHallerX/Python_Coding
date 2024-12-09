"""
Solve Fibonacci with a stack instead of recursion
"""


def fibStack(x):
    """
    Calculates the xth Fibonacci number using a stack-based iterative approach.

    Intuition:
    The Fibonacci sequence is traditionally calculated using recursion, where each number is the sum of the two
    preceding ones:
        fib(n) = fib(n - 1) + fib(n - 2)
    However, recursive solutions can lead to deep call stacks and increased memory usage for large 'n'.

    This function uses an explicit stack (implemented with a list) to simulate the recursive calls iteratively.
    By doing so, it avoids the limitations of recursion and provides better control over the computation process.

    Stack Management:
        The stack holds all the pending computations.
        Using stack.append() and stack.pop(), we manage the order of computation (LIFO - Last In, First Out).

    Total Update:
        Only updated when a base case is encountered.
        Ensures that only valid Fibonacci values (0 or 1) are added.

    Simulation of Recursion:
        By pushing a - 1 and a - 2, we're effectively exploring all the branches of the Fibonacci computation tree.

    This approach performs a depth-first traversal of the computation tree, summing up the necessary base cases to
    compute the final Fibonacci number.

    Iteration	Action	                Stack	    Total
    1	        Pop 4, push 3, 2	    [3, 2]	    0
    2	        Pop 2, push 1, 0	    [3, 1, 0]	0
    3	        Pop 0, add 0 to total	[3, 1]	    0
    4	        Pop 1, add 1 to total	[3]	        1
    5	        Pop 3, push 2, 1	    [2, 1]	    1
    6	        Pop 1, add 1 to total	[2]	        2
    7	        Pop 2, push 1, 0	    [1, 0]	    2
    8	        Pop 0, add 0 to total	[1]	        2
    9	        Pop 1, add 1 to total	[]	        3
    """
    # Initialize the total sum to 0
    total = 0
    # Initialize a stack with the initial Fibonacci number 'x'
    stack = [x]

    # Loop until the stack is empty
    while stack:
        # Pop the last element added to the stack
        a = stack.pop()

        # Check if 'a' is 0 or 1, the base cases for Fibonacci sequence
        if a in [0, 1]:
            # Add the value of 'a' to 'total' (since fib(0) = 0 and fib(1) = 1)
            total += a  # Add the actual value of 'a' to total
        else:
            # For values greater than 1, push the next two Fibonacci computations onto the stack
            stack.append(a - 1)  # Push 'a - 1' onto the stack
            stack.append(a - 2)  # Push 'a - 2' onto the stack
    # Return the total sum, which is the Fibonacci number for 'x'
    return total


print(fibStack(4))
