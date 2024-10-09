"""
659. Encode and Decode Strings (medium)

Premium problem, use LintCode

Design an algorithm to encode a list of strings to a string.

The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode.
"""


def encode(strs):
    """
    Combine the strings with the measured length of the following string and pound sign as separators.
    Example: 4#gaga6#brains2#yo
    Since the pound sign could be in a string as well, we need the length indicator to skip over any pound signs
    that are part of the strings and have a pointer move to the start of a new word.
    Args:
        strs: a list of strings
    Returns:
        Single encoded string
    """
    result = ""
    for string in strs:
        result += str(len(string)) + "#" + string
    return result


def decode(str):
    """
    Decodes a single string to a list of strings
    Two pointer solution.
    Params:
        str: A single encoded string containing sub-strings and separators
    Returns:
        A list of decoded strings.
    """
    result = []
    i = 0

    # Each iteration reads one word. i is at the start of the length number, j pointer marks pound sign
    while i < len(str):
        j = i  # start j at 0, or move j back to current number char

        # Length may be multi-digit, so use a loop to move j pointer to find the end of the length number
        # Move j pointer from index of number until it hits the first pound char -> j is index of pound char
        while str[j] != "#":
            j += 1

        # Length may be multi-digit, so measure from start of number to pound sign, cast to int
        length = int(str[i:j])

        # Main part: Read current word from one after pound to length and append to result
        result.append(str[j + 1 : j + 1 + length])

        # Update length number pointer i to after current word
        i = j + 1 + length

    return result


def main():
    print(
        decode(str=encode(strs=["lint", "code", "love", "you"])),
        'expected output: ["lint", "code", "love", "you"]',
    )


if __name__ == "__main__":
    main()
