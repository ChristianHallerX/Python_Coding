"""
875. Koko Eating Bananas (medium)

Koko loves to eat bananas.

There are 'n' piles of bananas, the ith pile has 'piles[i]' bananas.

The guards have gone and will come back in 'h' hours.

Koko can decide her bananas-per-hour eating speed of 'k'.

Each hour, she chooses some pile of bananas and eats 'k' bananas from that pile.

If the pile has less than 'k' bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer 'k' such that she can eat all the bananas within 'h' hours.
"""

import math


def minEatingSpeed(piles: list[int], h: int) -> int:
    """
    Precondition: Hours h must be larger or equal to number of piles (len(piles)) because one pile can be eaten per hour
    regardless of speed.
    - Brute Force: Start at k=1 and increase up to k=max(piles). Time Complexity: O(max(piles) * len(piles))
    - Binary Search: Use a range of eating speeds k (1 to max(piles)) and run
        Binary Search (left,middle(k), right pointers) on this range and test for the minimum k possible.
        If selected k works, go left/smaller. If k fails, go right/larger.
        Time Complexity: O(log(max(piles)) * len(piles))
    If resulting time h is too large, increase eating speed k, search to right (higher speeds).
    If resulting time is shorter than h, try decreasing speed, search to left (slower speeds).
    """
    # Init bin search
    left = 1
    right = max(piles)
    result = max(piles)  # Start with worst case and update by minimizing

    while left <= right:
        # Middle pointer is eating speed k
        k = (left + right) // 2

        # Calc the hours needed for the pile given k speed
        hours = 0
        for p in piles:
            # Always round up hours with ceiling function
            hours += math.ceil(p / k)
        if hours <= h:
            # Hours less than required -> update result with eating speed k (middle pointer)
            # and search to left (move right pointer)
            result = min(result, k)
            right = k - 1
        else:
            # Hours too long, eating speed k too low -> search to right (move left pointer)
            left = k + 1

    return result


def main():
    piles = [3, 6, 7, 11]
    h = 8
    print(minEatingSpeed(piles, h), "expected: 4")

    piles = [30, 11, 23, 4, 20]
    h = 5
    print(minEatingSpeed(piles, h), "expected: 30")

    piles = [30, 11, 23, 4, 20]
    h = 6
    print(minEatingSpeed(piles, h), "expected: 23")


if __name__ == "__main__":
    main()
