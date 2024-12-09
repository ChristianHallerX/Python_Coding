"""
Stream Filter DataDog

There is a 'stream' that has coming 'tags' and also has a list of 'keywords'.
Design a high performance filter to output remaining tags minus the keyword.

For example:
You are given stream:
['apple, facebook, google',
'banana, facebook',
'facebook, google, tesla',
'intuit, google, facebook'].

If the keyword is ['apple'] the output should be ['facebook', 'google'] because only
'apple, facebook, google' has apple.

Similarly, if the keyword is ['facebook', 'google'], the output should be ['apple', 'tesla', 'intuit'].

The output can be in any order and can be put into a single list/array.
"""


def streamFilter(stream, kws):
    """
    Time complexity: O(n(k+m)), k=tags per line, m=keywords, n=lines
    Memory complexity: O(m+U) create 2 sets plus k line sets.
                       All unique tags O(U), no matches -> Output = stream.
    """

    kws_set = set(kws)
    output_set = set()

    for line in stream:
        tags = line.split(", ")
        tag_set = set(tags)

        # Using sets, check if ALL keywords are present in the current set of tags (all O(n) ops)
        if kws_set.issubset(tag_set):
            # Add all tags from this line to the output set, except the keyword tags
            output_set.update(tag_set - kws_set)

    # Convert set to list before returning
    return list(output_set)


def main():
    stream = [
        "apple, facebook, google",
        "banana, facebook",
        "facebook, google, tesla",
        "intuit, google, facebook",
    ]
    kws = ["apple"]
    print(streamFilter(stream, kws), "expected ['facebook', 'google']")

    stream = [
        "apple, facebook, google",
        "banana, facebook",
        "facebook, google, tesla",
        "intuit, google, facebook",
    ]
    kws = ["facebook", "google"]
    print(streamFilter(stream, kws), "expected ['apple', 'tesla', 'intuit']")


if __name__ == "__main__":
    main()
