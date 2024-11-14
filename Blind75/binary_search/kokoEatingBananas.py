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


def minEatingSpeed(piles: list[int], h: int) -> int:
    """
    Use a range of eating speeds (k) and run binary search on this range and test for the minimum k possible.
    If resulting time h is too large, increase eating speed k, search to right (higher speeds).
    If resulting time is shorter than h, try decreasing speed, search  to left (slower speeds).
    """
    return None


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
