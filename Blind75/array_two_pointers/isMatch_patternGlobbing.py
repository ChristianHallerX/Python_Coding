"""
44. Wildcard Matching (Hard)

Given an input 'string' and a 'pattern', implement wildcard pattern matching with support for '?' and '*' where:
 - '?' Matches any single character.
- '*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).
"""


def isMatch(string, pattern):
    """
    This function checks if a given string matches a pattern with wildcards.
    The pattern can include '?' to match any single character and '*' to match any sequence of characters.
    The algorithm uses a greedy approach with backtracking for '*' to efficiently find matches.
    Greedy matching attempts to match as much as possible initially, and backtracking is used to adjust if the match fails.
    """

    # Initialize pointers for string and pattern
    strIndex, patIndex = 0, 0

    # Variables to remember the position of '*' in pattern and corresponding position in string
    starIndex, matchIndex = -1, 0

    # Loop through the string
    while strIndex < len(string):

        # If characters match or pattern has '?', move both pointers
        if patIndex < len(pattern) and (
            pattern[patIndex] == string[strIndex] or pattern[patIndex] == "?"
        ):
            strIndex += 1
            patIndex += 1

        # If pattern has '*', record the position and try to match zero characters
        elif patIndex < len(pattern) and pattern[patIndex] == "*":
            starIndex = patIndex
            matchIndex = strIndex
            patIndex += 1

        # If mismatch occurs and there was a previous '*', backtrack
        elif starIndex != -1:
            patIndex = starIndex + 1
            matchIndex += 1
            strIndex = matchIndex

        # If no match and no previous '*', return False
        else:
            return False

    # Check for remaining '*' in pattern
    while patIndex < len(pattern) and pattern[patIndex] == "*":
        patIndex += 1

    # Return True if pattern is fully matched
    return patIndex == len(pattern)


if __name__ == "__main__":
    print(isMatch(string="aa", pattern="a"), "expected: False")

    print(isMatch(string="aa", pattern="*"), "expected: True")

    print(isMatch(string="cb", pattern="?a"), "expected: False")
