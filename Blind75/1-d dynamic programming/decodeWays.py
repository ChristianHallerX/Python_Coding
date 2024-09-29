"""
91. Decode Ways (medium)

You have intercepted a secret message encoded as a string of numbers.
The message is decoded via the following mapping:
"1" -> 'A'
"2" -> 'B'
...
"25" -> 'Y'
"26" -> 'Z'
However, while decoding the message, you realize that there are many different ways you can decode the
message because some codes are contained in other codes ("2" and "5" vs "25").

For example, "11106" can be decoded into:
- "AAJF" with the grouping (1, 1, 10, 6)
- "KJF" with the grouping (11, 10, 6)
- The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).

Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the number of ways to decode it.
If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.
"""


def numDecodings_recursive(s: str) -> int:
    """
    Recursive dfs caching solution
    Time complexity: O(n)
    Memory complexity: O(n)
    """
    # Initialize cache global var, empty string will return 1
    # index(key)->decode ways, initialize with last index, which can only decode one way
    dp_cache_dict = {len(s): 1}

    def dfs(i):
        """
        i is index in string 's'.

        """
        # Good base case: already cached or last position in s, return cached value
        if i in dp_cache_dict:
            return dp_cache_dict[i]
        # Bad base case: can't decode string that starts with 0 per definition
        if s[i] == "0":
            return 0

        # Run dfs() on first next char and, if conditions apply, second next char
        result = dfs(i + 1)
        if i + 1 < len(s) and (
            s[i] == "1"
            or s[i] == "2"
            and s[i + 1] in "0123456"  # double digit starting with 1 (1x) or 2 (2x)
        ):
            result += dfs(i + 2)

        # Cache it
        dp_cache_dict[i] = result

        return result

    # Run dfs starting at index 0
    return dfs(0)


def numDecodings_dp(s: str) -> int:
    """
    DP bottom-up solution starting from the back of string/bottom of decision tree.
    """
    dp_cache_dict = {len(s): 1}

    # Loop in reverse over 's'
    for i in range(len(s) - 1, -1, -1):
        # Bad Base Case digit 0
        if s[i] == "0":
            dp_cache_dict[i] = 0
        # Good Base Case digit 1-9: recursively calculate
        else:
            # Copy from the right to current i
            dp_cache_dict[i] = dp_cache_dict[i + 1]

        # Double digit validity checker
        if i + 1 < len(s) and (
            s[i] == "1"
            or s[i] == "2"
            and s[i + 1] in "0123456"  # double digit starting with 1 (1x) or 2 (2x)
        ):
            # Add up count to current i
            dp_cache_dict[i] += dp_cache_dict[i + 2]

    return dp_cache_dict[0]


def main():
    print(
        numDecodings_recursive(s="12"),
        "expected: 2, explanation: '12' could be decoded as 'AB' (1 2) or 'L' (12).",
    )

    print(
        numDecodings_recursive(s="226"),
        "expected: 3, explanation: '226' could be decoded as 'BZ' (2 26), 'VF' (22 6), or 'BBF'"
        "(2 2 6).",
    )

    print(
        numDecodings_recursive(s="06"),
        "expected: 0, explanation: '06' cannot be mapped to 'F' because of the leading zero"
        "('6' is different from '06'). In this case, the string is not a valid encoding,"
        "so return 0.",
    )

    print("\n")

    print(
        numDecodings_dp(s="12"),
        "expected: 2, explanation: '12' could be decoded as 'AB' (1 2) or 'L' (12).",
    )

    print(
        numDecodings_dp(s="226"),
        "expected: 3, explanation: '226' could be decoded as 'BZ' (2 26), 'VF' (22 6), or 'BBF'"
        "(2 2 6).",
    )

    print(
        numDecodings_dp(s="06"),
        "expected: 0, explanation: '06' cannot be mapped to 'F' because of the leading zero"
        "('6' is different from '06'). In this case, the string is not a valid encoding,"
        "so return 0.",
    )


if __name__ == "__main__":
    main()
