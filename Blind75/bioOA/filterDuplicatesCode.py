"""
Filter Duplicates

Implement the function 'filter_duplicates(data) that takes a 'data' array as input and returns an array
containing the values of 'data' without the duplicates.

Important: The initial order of the values must be kept.
"""


def filter_duplicates(data):
    seen_set = set()
    result = []

    for item in data:
        if item not in seen_set:
            # The result list preserves the order (which will be lost in the set alone)
            result.append(item)
            seen_set.add(item)
    return result


def main():
    data = [7, 6, 4, 3, 3, 4, 9]
    print(filter_duplicates(data), "expected: [7, 6, 4, 3, 9]")


if __name__ == "__main__":
    main()
