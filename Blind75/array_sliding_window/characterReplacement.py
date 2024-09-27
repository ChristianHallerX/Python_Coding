"""
424. Longest Repeating Character Replacement (medium)

You are given a string 's' and an integer 'k'. You can choose any character of the string and change it to any other

uppercase English character. You can perform this operation at most 'k' times.

Return the length of the longest EQUAL substring containing the same letter you can get after performing the above
operations.
"""


def characterReplacement(s: str, k: int) -> int:
    left_pointer, right_pointer = 0, 0
    result = 0
    working_k = k

    while right_pointer <= len(s):
        # Case: contains only one kind of char (good)
        if len(set(s[left_pointer : right_pointer + 1])) == 1:
            # reset working_k to original k if all equal
            working_k = k

            this_length = right_pointer - left_pointer + 1
            result = max(this_length, result)

            # update vars for next iteration
            right_pointer += 1

        # Case: contains unique char (bad)
        else:
            if working_k > 0:

                this_length = right_pointer - left_pointer + 2
                result = max(this_length, result)

                # update vars for next iteration
                right_pointer += 1
                working_k -= 1
            else:
                left_pointer += 1

    return result


def characterReplacementDict(s: str, k: int) -> int:
    """
    Sliding Window, Two Pointers.
    Given a substring, you can replace k chars to make all equal chars.
    What is the longest substring length for the given input string and k non-most-frequent chars?

    Right pointer always moves forward, left pointer is adjusted until valid, then measure window length.

    Time complexity O(n*26) = O(n)
    """
    result = 0
    count_dict = {}
    left = 0

    # Always move right pointer to right
    for right in range(len(s)):

        # Add char key at right pointer to count_dict and
        # increment count value (get defaults to 0)
        count_dict[s[right]] = 1 + count_dict.get(s[right], 0)

        # Adjust window length on left if necessary
        # While substring has too many substitutes (is invalid), move left pointer
        while (right - left + 1) - max(count_dict.values()) > k:
            # Decrement left pointer char in dict
            count_dict[s[left]] -= 1
            # Move left pointer
            left += 1

        # Calculate window length
        result = max(right - left + 1, result)

    return result


def main():
    print("characterReplacement")
    print(characterReplacement(s="ABAB", k=2), "expected 4")
    print(characterReplacement(s="AABABBA", k=1), "expected 4")
    print("characterReplacementDict")
    print(characterReplacementDict(s="ABAB", k=2), "expected 4")
    print(characterReplacementDict(s="AABABBA", k=1), "expected 4")


if __name__ == "__main__":
    main()
