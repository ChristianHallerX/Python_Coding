"""
621. Task Scheduler (Medium)

You are given an array of CPU 'tasks', each labeled with a letter from A to Z, and a number 'n'.

Each CPU interval can be idle or allow the completion of one task.

Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least 'n' intervals
between two tasks with the same label (cooldown period). Using a different task in the gap does NOT reset the cooldown.

Return the minimum number of CPU intervals required to complete all tasks.
"""

import heapq
from collections import Counter, deque


def leastInterval(tasks: list[str], n: int) -> int:
    """
    Count the unique letters (tasks). Add task count to MaxHeap (negative minHeap).
    Use the more frequent tasks first. -> Pop most frequent task from MaxHeap.
    Push task count and time to queue [-time, itleTime] and back to MaxHeap.
    Keep time counter.
    Time Complexity: O(log26) for each letter task, total O(n * m) n = letter task, m = idle time
    """
    # Automatically create a dictionary letter -> count
    countDict = Counter(tasks)

    # Convert counts to negative, so the python minHeap becomes a maxHeap
    maxHeap = [-cnt for cnt in countDict.values()]
    # Convert list to MaxHeap
    heapq.heapify(maxHeap)

    # Init time variable that we want to return
    time = 0

    # Init queue with lists. Each time step will be [-count, idleTime]
    q = deque()

    # Run loop while these are not empty
    while maxHeap or q:
        # Increment time at start of each iteration step
        time += 1

        # Use one task, decrement (increment because we are reversed minHeap)
        if maxHeap:
            cnt = heapq.heappop(maxHeap) + 1

            # Add count, time + idle time to queue
            if cnt:
                q.append([cnt, time + n])

        # Remove first queue item if first queue item's idle time and current time match and add count back to Maxheap
        if q and q[0][1] == time:
            heapq.heappush(maxHeap, q.popleft()[0])

    return time


if __name__ == "__main__":
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    print(leastInterval(tasks, n), "expected: 8, AB_AB_AB")

    tasks = ["A", "C", "A", "B", "D", "B"]
    n = 1
    print(leastInterval(tasks, n), "expected: 6, ABCDAB")

    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 3
    print(leastInterval(tasks, n), "expected: 10, AB__AB__AB")
