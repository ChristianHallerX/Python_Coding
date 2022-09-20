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
        if len(set(s[left_pointer:right_pointer + 1])) == 1:
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
    char_count = {} # key char: value count
    result = 0
    left_pointer = 0

    for right_pointer in range(len(s)):
        # add current character at right pointer to char count dictionary
        char_count[s[right_pointer]] = 1 + char_count.get(s[right_pointer], 0)  # 1 plus what's in dict, default 0
        this_length = right_pointer - left_pointer + 1

        # string length minus most frequent character -> chars to be replaced, k = allowable replacements
        if this_length - max(char_count.values()) > k:
            # decrement count of char at left pointer by one, then shift left pointer by one
            char_count[s[left_pointer]] -= 1
            left_pointer += 1

        result = max(result, this_length)
    return result


def main():
    print('characterReplacement')
    print(characterReplacement(s="ABAB", k=2), 'expected 4')
    print(characterReplacement(s="AABABBA", k=1), 'expected 4')
    print('characterReplacementDict')
    print(characterReplacementDict(s="ABAB", k=2), 'expected 4')
    print(characterReplacementDict(s="AABABBA", k=1), 'expected 4')


if __name__ == '__main__':
    main()
