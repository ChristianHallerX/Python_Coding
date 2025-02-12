"""
2131. Longest Palindrome by Concatenating Two Letter Words (Medium)

You are given an array of strings 'words'.
Each element of 'words' consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from 'words' and concatenating them in any order.
Each element can be selected at most once.

Return the length of the longest palindrome that you can create.
If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.
"""


def longestPalindrome(words: list[str]) -> int:
    # count occurrences of each word with dict
    count_dict = {}
    for word in words:
        count_dict[word] = count_dict.get(word, 0) + 1

    # Keep track of words that have been ulilized
    used_set = set()
    total_length = 0
    # A word that's two equal letters (mirrorable) can be used in the center of a palindrome
    center_used = False

    # loop over all words
    for word in words:
        # Skip words that are already in the used set (i.e., a reverse word
        if word not in used_set:
            reverse_word = word[::-1]

            # equal-letter word
            if word == reverse_word:
                # Use in center if this equal letter-word exists only once and has not been used yet as center
                if count_dict[word] % 2 == 1 and not center_used:
                    center_used = True
                    total_length += 2

                # are there multiple equal-letter words? How many pairs of double-letter words?
                pairs = count_dict[word] // 2
                used_set.add(word)

            # not equal-letter word
            else:
                # find out if the reverse word has counts in the dict. If so, also use the reverse.
                pairs = min(count_dict[word], count_dict.get(reverse_word, 0))
                used_set.add(word)
                if reverse_word in count_dict:
                    used_set.add(reverse_word)
            # Each pair contributes 4 to the length
            total_length += pairs * 4

    return total_length


def main():
    words = ["lc", "cl", "gg"]
    print(longestPalindrome(words), "expected: 6")

    words = ["ab", "ty", "yt", "lc", "cl", "ab"]
    print(longestPalindrome(words), "expected: 8")

    words = ["cc", "ll", "xx"]
    print(longestPalindrome(words), "expected: 2")


if __name__ == "__main__":
    main()
