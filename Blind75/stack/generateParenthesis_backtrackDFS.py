"""
22. Generate Parentheses (medium)

Given 'n' pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""


def generateParenthesis(n: int) -> list[str]:
    """
    DFS recursive with Backtracking and stack.
    Intuition:
    - Only add closing p if amount of open p is > closing p.
    - Only add open p if open p < n.
    - Valid result if open p == closing p == n (base case).
    Choice: add open (open, open) or close (open, close).
    """
    # Stack is a global var that contains the individual parenthesis chars and need to be joined for result element
    stack = []
    result = []

    def backtrackDFS(openN, closedN):
        # Base case for stopping/joining/appending
        if openN == closedN == n:
            result.append("".join(stack))

        if openN < n:
            # Add open p to stack, run DFS with new p, then remove char from stack
            stack.append("(")
            backtrackDFS(openN + 1, closedN)
            stack.pop()

        if closedN < openN:
            # Add closed p to stack, run DFS with new p, then remove char from stack
            stack.append(")")
            backtrackDFS(openN, closedN + 1)
            stack.pop()

    # Call DFS with starting params and populate result
    backtrackDFS(openN=0, closedN=0)

    return result


def main():
    n = 3
    print(
        generateParenthesis(n),
        'expected: ["((()))","(()())","(())()","()(())","()()()"]',
    )

    n = 1
    print(generateParenthesis(n), 'expected: ["()"]')


if __name__ == "__main__":
    main()
