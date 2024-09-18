"""
295. Find Median from Data Stream (hard)

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value,
and the median is the mean of the two middle values.

- For example, for arr = [2,3,4], the median is 3.
- For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:
- 'MedianFinder()' initializes the 'MedianFinder' object.
- 'void 'addNum(int num)' adds the integer 'num' from the data stream to the data structure.
- 'double findMedian()' returns the median of all elements so far.
  Answers within 10^-5 of the actual answer will be accepted.
"""

import heapq


class MedianFinder:
    def __init__(self):
        """
        Two heap implementation, calc. median in O(1) time.
        Init small heap and large heap (lists).
        Left side of list: Small heap (get max value)
        Right side of list: large heap (get min value)
        The 0-index element of a heap in python is always the smallest value (min heap).
        In python, only min heaps exist. A max heap requires a workaround -> has to be created with negative values.
        """
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        """
        Keep heaps approximately equal (max. 1 element length difference)
        Max of small heap has to be smaller than min of large heap. Otherwise, remove and add to large heap.
        Next, check if length is max 1 element difference, otherwise move smallest element from large heap to small h.

        1. Lookup: the max in a max heap and min in min heap can be found in O(1) time.
        2. Removing/popping: O(logn) time
        3. Adding/ordering: By default, add to small h, but push the largest value of small h to large h. O(logn) time.
        """
        # By default, add every number to small heap
        # python only implements min-heaps. To get the 'small' max heap, use negative
        heapq.heappush(self.small, -1 * num)

        # Assure max element in small heap is smaller or equal than min in large heap
        # -> pop from small h, push to large h
        # Heap: Largest value is at index 0, small h: multiply by -1 to get true value
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = -1 * heapq.heappop(
                self.small
            )  # Large heap can store the positive value, multiply by -1
            heapq.heappush(self.large, val)

        # Small h getting too large -> pop and push to large
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(
                self.small
            )  # Large heap can store the positive value, multiply by -1
            heapq.heappush(self.large, val)

        # Large h getting too large -> pop and push to small
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

        return None

    def findMedian(self) -> float:
        """
        Popping values from heap is O(1) time.
        For the median on an even number of values (small h + large h), divide the middle two elements by two.
        For the median on odd numbers, if small h larger, value largest value, if big h larger pick smallest value.
        """
        # Odd length, small is longer, pick from small
        if len(self.small) > len(self.large):
            return self.small[0] * -1

        # Odd length, large is longer, pick from large
        if len(self.large) > len(self.small):
            return self.large[0]

        # Equal length
        if len(self.large) == len(self.small):
            return (-1 * self.small[0] + self.large[0]) / 2


def main():
    # Your MedianFinder object will be instantiated and called as such:
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    print(obj.findMedian())
    obj.addNum(3)
    print(obj.findMedian())

    print("expected: [null, null, null, 1.5, null, 2.0]\n")

    obj2 = MedianFinder()
    obj2.addNum(1)
    print(obj2.findMedian())
    obj2.addNum(2)
    print(obj2.findMedian())
    obj2.addNum(3)
    print(obj2.findMedian())
    obj2.addNum(4)
    print(obj2.findMedian())
    obj2.addNum(5)
    print(obj2.findMedian())
    obj2.addNum(6)
    print(obj2.findMedian())
    obj2.addNum(7)
    print(obj2.findMedian())
    obj2.addNum(8)
    print(obj2.findMedian())
    obj2.addNum(9)
    print(obj2.findMedian())
    obj2.addNum(10)
    print(obj2.findMedian())

    print(
        "expected: [null,null,1.00000,null,1.50000,null,2.00000,null,2.50000,null,3.00000,null,3.50000,null,"
        "4.00000,null,4.50000,null,5.00000,null,5.50000]"
    )


if __name__ == "__main__":
    main()
