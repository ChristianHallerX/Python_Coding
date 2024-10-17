"""
150. Evaluate 'Reverse Polish Notation' (medium)

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
- The valid operators are '+', '-', '*', and '/'.
- Each operand may be an integer or another expression.
- The division between two integers always truncates toward zero.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""


def evalRPN(tokens: list[str]) -> int:
    """
    Loop through tokens and evaluate them.
        If operator, pop last two elements, operate, append result to stack.
        if non-operator (number), push to stack.
    Time complexity: O(n)
    Memory complexity: O(n)
    """
    stack = []
    for char in tokens:
        if char == "+":
            # Remove the last two stack elements, add them, and push the result to stack
            stack.append(stack.pop() + stack.pop())
        elif char == "*":
            stack.append(stack.pop() * stack.pop())
        elif char == "-":
            # Popping works from right to left, which means we need to reverse
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif char == "/":
            a, b = stack.pop(), stack.pop()
            # Cast the float back to int, which rounds to 0
            stack.append(int(b / a))
        else:
            stack.append(int(char))
    # Only the last result should be on stack
    return stack[0]


def main():
    tokens = ["2", "1", "+", "3", "*"]
    print(evalRPN(tokens), "expected: 9. Explanation: ((2 + 1) * 3) = 9")

    tokens = ["4", "13", "5", "/", "+"]
    print(evalRPN(tokens), "expected: 6. Explanation: (4 + (13 / 5)) = 6)")

    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(evalRPN(tokens), "expected: 22")


if __name__ == "__main__":
    main()
