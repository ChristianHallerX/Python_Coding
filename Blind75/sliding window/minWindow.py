"""
76. Minimum Window Substring (hard)

Given two strings 's' and 't' of lengths 'm' and 'n' respectively, return the minimum window substring of 's'
such that every character in 't' (including duplicates) is included in the window.
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
"""

def minWindow(s: str, t: str) -> str:
    """
    Use sliding window/left, right pointers to iterate over string.
    Return the shortest length window with all target chars.
    Time complexity: O(n), window goes over string s only once.
    """

    # empty string edge case described in prompt
    if t == "":
        return ""

    # init dict for window substring and dict for t target string
    window_dict, target_dict = {}, {}
    # init result window index
    result, result_length = [-1, -1], float("infinity")
    left_pointer = 0

    # add all target characters and count into dict
    for char in t:
        target_dict[char] = 1 + target_dict.get(char, 0)  # char (key): sum (value)

    # initialize character count sum for window (have) and target (need)
    have_count, need_count = 0, len(target_dict)

    for right_pointer in range(len(s)):
        # get char at right pointer and add char to window dictionary
        char = s[right_pointer]
        window_dict[char] = 1 + window_dict.get(char, 0)  # char (key): sum (value)

        if char in target_dict and window_dict[char] == target_dict[char]:
            have_count += 1

        while have_count == need_count:
            # update result if window shorter than prev length (looking for minimized window)
            if (right_pointer - left_pointer + 1) < result_length:
                result = [left_pointer, right_pointer]
                result_length = (right_pointer - left_pointer + 1)

            # move left pointer and remove that char from window dict
            window_dict[s[left_pointer]] -= 1
            if s[left_pointer] in target_dict and window_dict[s[left_pointer]] < target_dict[s[left_pointer]]:
                have_count -= 1
            left_pointer += 1

    left_pointer, right_pointer = result
    return s[left_pointer:right_pointer + 1] if result_length != float("infinity") else ""


def main():
    print(minWindow(s="ADOBECODEBANC", t="ABC"), "expected BANC")
    print(minWindow(s="a", t="a"), "expected a")
    print(minWindow(s="a", t="aa"), "expected '' empty string")


if __name__ == '__main__':
    main()
