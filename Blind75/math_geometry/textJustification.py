"""
68. Text Justification (Hard)

Given an array of strings words and a width maxWidth, format the text such that each line has exactly 'maxWidth'
characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be
assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:
    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array words contains at least one word.
"""


def fullJustify(words: list[str], maxWidth: int) -> list[str]:
    """
    Lots of trouble with the edge cases
    Time Complexity: O(n * L) L=max word length
    Space Complexity: O(maxWidth), store one line at a time besides the output
    """
    result = []
    curr_line = []
    curr_line_length = 0
    i = 0

    while i < len(words):
        # how do we know the current line is complete? -> Additional words exceed maxWidth
        # -> if exceeds length, then distribute the extra space between the accumulated words on list
        if curr_line_length + len(curr_line) + len(words[i]) > maxWidth:
            extra_space = maxWidth - curr_line_length

            # Calc how many spaces go between the words in each gap. max() avoid div 0 error (curr_line is 1 -> /(1-1))
            spaces_per_gap = extra_space // max(1, len(curr_line) - 1)
            # Remainder spaces exist if they can't be evenly distributed between the words
            remainder_spaces = extra_space % max(1, len(curr_line) - 1)

            # Insert spaces string elements between the words elements on curr_line list
            # -1 because we are not adding space behind the last word, only second but last.
            # max(1) handles 1 word line edge case
            for j in range(max(1, len(curr_line) - 1)):
                curr_line[j] += " " * spaces_per_gap
                # Add remainder spaces to the left of line first (greedily)
                if remainder_spaces:
                    curr_line[j] += " "
                    remainder_spaces -= 1

            # append all elements on list to 'result' as a single string
            result.append("".join(curr_line))
            # reset
            curr_line, curr_line_length = [], 0

        # Add a word to curr_line while not exceeding maxWidth yet
        curr_line.append(words[i])
        curr_line_length += len(words[i])
        i += 1

    # handling last line with single spaces between words (left justified) and trailing space on right.
    # 'curr_line' is still filled
    last_line = " ".join(curr_line)
    trailing_space = maxWidth - len(last_line)
    result.append(last_line + " " * trailing_space)

    return result


def main():
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    print(
        fullJustify(words, maxWidth),
        """
expected:
["This    is    an", "example  of text", "justification.  "]
""",
    )

    words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    maxWidth = 16
    print(
        fullJustify(words, maxWidth),
        """
expected:
["What   must   be", "acknowledgment  ", "shall be        "]
""",
    )

    words = [
        "Science",
        "is",
        "what",
        "we",
        "understand",
        "well",
        "enough",
        "to",
        "explain",
        "to",
        "a",
        "computer.",
        "Art",
        "is",
        "everything",
        "else",
        "we",
        "do",
    ]
    maxWidth = 20
    print(
        fullJustify(words, maxWidth),
        """
expected:
["Science  is  what we", "understand      well", "enough to explain to", "a  computer.  Art is", "everything  else  we", "do                  "]
""",
    )


if __name__ == "__main__":
    main()
