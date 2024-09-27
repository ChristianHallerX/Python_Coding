"""
271. String Encode and Decode (medium)

Design an algorithm to encode a list of strings to a single string.

The encoded string is then decoded back to the original list of strings.

Please implement encode and decode
"""


def encode(strs: list[str]) -> str:
    """
    Use a char count and pound sign (#) as delimiters. 6#blabla2#ka
    """
    result = ""
    for string in strs:
        result += str(len(string)) + "#" + string

    return result


def decode(self, s: str) -> list[str]:
    """We get a single string and want to return a list"""
    result = []
    # initialize first pointer
    i = 0

    while i < len(s):
        # Second pointer, j, find end of 'length' integer
        # may be double, triple digit
        j = i
        while s[j] != "#":
            j += 1

        # slice the 'length' integer with both pointers
        length_int = int(s[i:j])

        # read the word starting after # up to length_int
        result.append(s[j + 1 : j + 1 + length_int])

        # update pointer i to end of word
        i = j + 1 + length_int

    return result


def main():
    input1 = ["neet", "code", "love", "you"]
    output1 = ["neet", "code", "love", "you"]
    encoded1 = encode(input1)
    print(decode(encoded1), f"expected: {output1}")
    input2 = ["we", "say", ":", "yes"]
    output2 = ["we", "say", ":", "yes"]
    encoded2 = encode(input2)
    print(decode(encoded2), f"expected: {output2}")


if __name__ == "__main__":
    main()
