"""
155. Min Stack (medium, was easy)

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- push(int) pushes the element val onto the stack.
- pop() removes the element on the top of the stack.
- top() gets the top element of the stack.
- getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.
"""

"""
The getMin() in O(1) time is  the hardest.
    Hint 1: Consider each node in the stack having a minimum value.
    -> Use a second stack with 'min' values, 'stack' and 'minStack'
"""


class MinStack:
    def __init__(self):
        # init two stacks with lists
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # find out if this value is the new minimum, if not append old value to minStack
        # edge case: if statement for empty stack
        val = min(self.minStack[-1] if self.minStack else val, val)
        self.minStack.append(val)

    def pop(self) -> None:
        # pop deletes the last value
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # Return the stack's last value without popping
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the minStack's last value without popping
        return self.minStack[-1]


def main():
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())  # -3
    obj.pop()
    print(obj.top())  # 0
    print(obj.getMin())  # -2

    print("expected: [None, None, None, None, -3, None, 0, -2]")


if __name__ == "__main__":
    main()
