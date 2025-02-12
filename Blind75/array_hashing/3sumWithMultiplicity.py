"""
923. 3Sum With Multiplicity (Medium)

Given an integer array 'arr', and an integer 'target', return the number of tuples 'i', 'j', 'k' such that
'i' < 'j' < 'k' and arr[i] + arr[j] + arr[k] == 'target'.

As the answer can be very large, return it modulo 109 + 7.
"""


def threeSumMulti(arr: list[int], target: int) -> int:
    """
    How many times can you sum up three values to the target?
    x + y + z = target
    It's a difficult combinatorial challenge
    """
    # Init the count of found triplets
    result = 0
    MOD = int(10**9 + 7)

    # Build frequency dictionary value:count
    count_dict = {}
    for num in arr:
        count_dict[num] = count_dict.get(num, 0) + 1

    keys = sorted(count_dict)

    # loop over unique keys (array values), first value X
    for i, x in enumerate(keys):
        # get a second key, y, above x
        for j in range(i, len(keys)):
            y = keys[j]
            # calc hypothetical third value, z, given x, y, and target
            z = target - x - y

            # Ensure x < y < z, which helps counting each triplet only once
            if z < y:
                continue
            # skip this z if not in dict/does not exist in arr
            if z not in count_dict:
                continue

            # Valid triplet - Each count of a value is an answer
            # Retrieve counts for the current values
            count_x, count_y, count_z = count_dict[x], count_dict[y], count_dict[z]

            # Case 1: x, y, and z are all the same.
            if x == y == z:
                # Choose 3 out of count_x.
                result += count_x * (count_x - 1) * (count_x - 2) // 6

            # Case 2a: x == y != z.
            elif x == y and y != z:
                # Choose 2 out of count_x and multiply by count_z.
                result += count_x * (count_x - 1) // 2 * count_z

            # Case 2b: x != y and y == z.
            elif x != y and y == z:
                # Multiply count_x by choose 2 from count_y.
                result += count_x * count_y * (count_y - 1) // 2

            # Case 3: All numbers are distinct.
            elif x < y < z:
                result += count_x * count_y * count_z

            result %= MOD

    return int(result)


def main():
    arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    target = 8
    print(threeSumMulti(arr, target), "expected: 20")

    arr = [1, 1, 2, 2, 2, 2]
    target = 5
    print(threeSumMulti(arr, target), "expected: 12")

    arr = [2, 1, 3]
    target = 6
    print(threeSumMulti(arr, target), "expected: 1")

    arr = [0 for _ in range(3000)]
    target = 0
    print(threeSumMulti(arr, target), "expected: 495500972")


if __name__ == "__main__":
    main()
