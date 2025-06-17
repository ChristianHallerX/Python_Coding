"""
703. Kth Largest Element in a Stream (Easy, should be Medium)

You are part of a university admissions office and need to keep track of the 'k'th highest test score from
applicants in real-time.
This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

You are tasked to implement a CLASS which, for a given integer 'k', maintains a stream of test scores
and continuously returns the 'k'th highest test score after a new score has been submitted.

More specifically, we are looking for the 'k'th highest score in the sorted list of all scores (i.e., duplicates count).

Implement the 'K'th Largest class:

    KthLargest(int k, int[] nums)       Initializes the object with the integer k and the stream of test scores nums.
    add(int val)                        Adds a new test score val to the stream and returns the element representing
                                        the 'k'th largest element in the pool of test scores so far.

"""

import heapq


class KthLargest:
    """
    A min-heap always automatically has the smallest value at index 0.
    Min-heap of size 'k' avoids searching the list in n-time when sorting etc. and makes
    - add/pop O(log n) time and
    - get min in O(1) time available

    Why min-heap and why size 'k'?
        - If the heap is 'k'-long, then they 'k'-smallest is always at the end and read in O(1).
    How to use  the add function?
        - add new value O(logn), pop smallest value O(logn) to cut heap back to k length

    Time Complexity: O(nlogn) constructor, O(logn) add
    """

    def __init__(self, k: int, nums: list[int]):
        # Heapify list
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        self.k = k

        # Cut down heap length to 'k' length so that min (i.e., 'k'th-largest) is always at root
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Add new value and automatically sort
        heapq.heappush(self.minHeap, val)

        # Remove smallest value if heap longer than 'k'
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # Return the smallest value at zero index
        return self.minHeap[0]


if __name__ == "__main__":
    # Test 1
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    print(kthLargest.add(3), "expected: 4")  # return 4
    print(kthLargest.add(5), "expected: 5")  # return 5
    print(kthLargest.add(10), "expected: 5")  # return 5
    print(kthLargest.add(9), "expected: 8")  # return 8
    print(kthLargest.add(4), "expected: 8")  # return 8

    # Test 2
    print("\n")
    kthLargest = KthLargest(4, [7, 7, 7, 7, 8, 3])
    print(kthLargest.add(2), "expected: 7")  # return 7
    print(kthLargest.add(10), "expected: 7")  # return 7
    print(kthLargest.add(9), "expected: 7")  # return 7
    print(kthLargest.add(9), "expected: 8")  # return 8
