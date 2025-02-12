"""
454. 4Sum II (Medium)

Given four integer arrays 'nums1', 'nums2', 'nums3', and 'nums4' all of length 'n',
return the number of tuples (i, j, k, l) such that:

- 0 <= i, j, k, l < n
- nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
"""


def fourSumCount(
    nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]
) -> int:
    """
    Four values have to sum up to 0. How many cases are there?

    1 Loop through every combination of elements from nums1 and nums2, add each sum to dict with count.
    2a Loop through every combination of elements from nums3 and nums3, make the sum negative target.
    2b Look up each negative target in the dict. If matches, get counts and add them to result_count.

    Time Complexity: 2*O(n^2) -> O(n^2)
    Space Complexity: there are n^2 pairs, in the worst case a dict of size O(n^2)
    """
    # compute all possible pair sums of elements from 'nums1' and 'nums2', and store the counts in a dictionary
    # sum: count
    sum_count = {}
    for a in nums1:
        for b in nums2:
            s = a + b
            sum_count[s] = sum_count.get(s, 0) + 1

    # Innit result counter
    result_count = 0

    # Compute all possible pair sums from  'nums3' and 'nums4' and make them negative
    # check if the complementary sum exists in sum_count dict that makes it 0
    for c in nums3:
        for d in nums4:
            # Original a+b+c+d=0  balance to-> a+b=-(c+d)
            target = -(c + d)

            # If target that combines to 0 already in dict, get the count and add to result_count
            if target in sum_count:
                result_count += sum_count[target]

    return result_count


def main():
    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]
    print(fourSumCount(nums1, nums2, nums3, nums4), "expected: 2")

    nums1 = [0]
    nums2 = [0]
    nums3 = [0]
    nums4 = [0]
    print(fourSumCount(nums1, nums2, nums3, nums4), "expected: 1")


if __name__ == "__main__":
    main()
