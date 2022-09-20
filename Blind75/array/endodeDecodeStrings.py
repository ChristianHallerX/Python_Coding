"""
659. Encode and Decode Strings (medium)

Design an algorithm to encode a list of strings to a string.

The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode.
"""

def encode(strs):
    """
    Combine the strings with the length of the following string and pound sign as separators.
    example 4#gaga6#brains
    Args:
        strs: a list of strings
    Returns:
        encodes a list of strings to a single string.
    """
    result = ""
    for string in strs:
        result += str(len(string)) + "#" + string
    return result


def decode(str):
    """
    Params:
        str: A string
    Returns:
        decodes a single string to a list of strings
    """
    result = []
    i = 0

    # i marks the start of a word, j is iterated through the word
    while i < len(str):
        j = i  # move j back to current number char
        # read the encoded length char in the first index of a word and cast to int
        length = int(str[i])
        # loop j pointer until before we hit the first pound char -> j is index of the number char
        while str[j] != "#":
            j += 1
        # read one word from one after pound to length and  append to result
        result.append(str[j+1:j+1+length])
        # update start-of-word pointer to after current word
        i = j + 1 + length


    return result


def main():
    print(decode(str=encode(strs=["lint", "code", "love", "you"])), 'expected output: ["lint", "code", "love", "you"]')
    #print(decode(str=["lint:;code:;love:;you"]), "expected output: ['lint', 'code', 'love', 'you']")


if __name__ == '__main__':
    main()
