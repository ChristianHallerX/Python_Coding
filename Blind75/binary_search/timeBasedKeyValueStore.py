"""
981. Time Based Key-Value Store (Medium)

Design a time-based key-value data structure that can store multiple values for the same key at different time
stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:
 - TimeMap() Initializes the object of the data structure.
 - set(String key, String value, int timestamp) Stores the key 'key' with the value 'value' at the given
    time 'timestamp'
 - get(String key, int timestamp) Returns a value such that 'set' was called previously, with
    'timestamp_prev <= timestamp'.
    If there are multiple such values, it returns the value associated with the largest 'timestamp_prev'.
    If there are no values, it returns "".

Constraints:
 - 1 <= 'key.length', 'value.length' <= 100
 - 'key' and 'value' consist of lowercase English letters and digits.
 - 1 <= 'timestamp' <= 107
 - All the timestamps 'timestamp' of 'set' are strictly increasing.
 - At most 2 * 105 calls will be made to 'set' and 'get'.
"""


class TimeMap:
    """
    The value is identified by a key AND a timestamp
    The value is going to be a list of lists. key: [[value, timestamp],[value, timestamp]]
    The hard part is the get() method, which requires searching through timestamps.
    Timestamps will be pre-sorted according to fine print -> Binary Search.
    """

    def __init__(self):
        self.store = {}  # key = string

    def set(self, key: str, value: str, timestamp: int) -> None:
        """Time Complexity: O(1) for adding to end of hash map"""
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        """
        Timestamps are pre-sorted -> Binary Search through key's value (list of lists). Time Complexity: O(logn)
        Only return value string.
        If key not found, return "".
        If TS not found, return value of next smaller TS.
        """
        result = ""
        values = self.store.get(key, [])  # Default to empty list

        # Binary Search on values
        left = 0
        right = len(values) - 1

        while left <= right:
            middle = (left + right) // 2
            if values[middle][1] <= timestamp:
                # preliminary result, since smaller values are accepted. Search to the right (higher TS)
                left = middle + 1
                result = values[middle][0]
            else:
                # TS too big. Do not get result. Search to left (smaller TS)
                right = middle - 1

        return result


def main():
    timeMap = TimeMap()
    timeMap.set(
        "foo", "bar", 1
    )  # store the key "foo" and value "bar" along with timestamp = 1.
    print(timeMap.get("foo", 1))  # return "bar"
    print(
        timeMap.get("foo", 3)
    )  # return "bar", since there is no value corresponding to foo at timestamp
    # 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
    timeMap.set(
        "foo", "bar2", 4
    )  # store the key "foo" and value "bar2" along with timestamp = 4.
    print(timeMap.get("foo", 4))  # return "bar2"
    print(timeMap.get("foo", 5))  # return "bar2"

    print("expected: [None, None, 'bar', 'bar', None, 'bar2', 'bar2']")


if __name__ == "__main__":
    main()
