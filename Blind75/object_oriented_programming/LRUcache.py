"""
146. LRU Cache (Medium)

Design a data structure that follows the constraints of a "Least Recently Used (LRU)" cache.

Implement the LRUCache class:
    - LRUCache(int capacity)
        Initialize the LRU cache with positive size capacity.

    - get(key (int))
        Return the value of the key if the key exists, otherwise return -1.

    - put(key (int), value (int))
        Update the value of the key if the key exists.
        Otherwise, add the key-value pair to the cache.
        If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.
"""

from collections import OrderedDict


class LRUCache:
    """
    Use an 'ordered dict' Python special data structure that preserves the usage order of entries.
    It's like a queue dict with special methods move_to_end() and popitem()
    """

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # Move the used key to the most recently used position (end item)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:

        # Move the key to the most recently used position (end item)
        if key in self.cache:
            self.cache.move_to_end(key)

        # Write the key and value at the end
        self.cache[key] = value

        # If write exceeds cap, drop the oldest key (first item)
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)

        return None


def main():
    cache = LRUCache(capacity=2)
    print(cache, "expected: None")
    print(cache.put(key=1, value=1), "expected: None")
    print(cache.put(key=2, value=2), "expected: None")
    print(cache.get(key=1), "expected: 1")
    print(cache.put(key=3, value=3), "expected: None")
    print(cache.get(key=2), "expected: -1")
    print(cache.put(key=4, value=4), "expected: None")
    print(cache.get(key=1), "expected: -1")
    print(cache.get(key=3), "expected: 3")
    print(cache.get(key=4), "expected: 4")


if __name__ == "__main__":
    main()
