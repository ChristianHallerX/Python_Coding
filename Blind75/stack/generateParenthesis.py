"""
22. Generate Parentheses (medium)

Given 'n' pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""


def generateParenthesis(n: int) -> list[str]:
    return None


def main():
    n = 3
    print(
        generateParenthesis(n),
        'expected: ["((()))","(()())","(())()","()(())","()()()"]',
    )

    n = 2
    print(generateParenthesis(n), 'expected: ["()"]')


if __name__ == "__main__":
    main()
