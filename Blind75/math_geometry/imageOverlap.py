"""
835. Image Overlap (Medium)

You are given two images, 'img1' and 'img2', represented as binary, square matrices of size 'n' * 'n'.
A binary matrix has only 0s and 1s as values.

1. We *translate* one image however we choose by sliding all the 1-bits left, right, up, and/or down
    any number of units.
2. We then place it on top of the other image.
3. We can then calculate the overlap by counting the number of positions that have a 1 in both images.

Note also that a translation does not include any kind of rotation. Any 1-bits that are translated outside of the
matrix borders are erased.

Return the largest possible overlap.
"""


def largestOverlap(img1: list[list[int]], img2: list[list[int]]) -> int:
    """
    Largest overlap = largest count of a pixel shift between the two images
    1. get 1-bit coordinates for both images
    2. calculate shift for each coordinate pair from img1 and img2
    3. tally up which shift was counted the most frequently = max overlap

    Time Complexity: Get coords O(2n^2), nested loops O(n^2), dict: O(1). Total: O(n^4)
    Space Complexity: soring coords is larger than original O(n^2), dict O(n^2). Total O(n^2)
    """

    # Dictionary Shift:Count
    shift_count = {}
    max_overlap = 0

    # Get the coordinates of 1s in img1 and img2 as a list of tuples
    ones_img1 = [
        (i, j) for i in range(len(img1)) for j in range(len(img1)) if img1[i][j] == 1
    ]
    ones_img2 = [
        (i, j) for i in range(len(img2)) for j in range(len(img2)) if img2[i][j] == 1
    ]

    # For each pair of 1s from img1 and img2 calc the steps needed to overlap them
    for i1, j1 in ones_img1:
        for i2, j2 in ones_img2:

            # Subtract coords between images for shift required for overlap
            shift = (i2 - i1, j2 - j1)

            # Write to the dictionary. Add to the counter for this pixel shift distance
            shift_count[shift] = shift_count.get(shift, 0) + 1

            # Get the current largest overlap (largest count of this shift)
            max_overlap = max(max_overlap, shift_count[shift])

    return max_overlap


def main():
    img1 = [[1, 1, 0], [0, 1, 0], [0, 1, 0]]

    img2 = [[0, 0, 0], [0, 1, 1], [0, 0, 1]]
    print(largestOverlap(img1, img2), "expected: 3")

    img1 = [[1]]
    img2 = [[1]]
    print(largestOverlap(img1, img2), "expected: 1")

    img1 = [[0]]
    img2 = [[0]]
    print(largestOverlap(img1, img2), "expected: 0")


if __name__ == "__main__":
    main()
