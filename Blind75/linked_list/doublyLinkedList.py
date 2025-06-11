"""
Implement a doubly linked list with a length counter.

The maintain length counter algorithm involves keeping a counter to track the number of nodes
in the list, updating it as nodes are added.

This allows for efficient length retrieval.
"""


class Node(object):
    """Left <- { value } -> Right"""

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class DoublyLinkedList(object):
    """List of Node objects which are linked to each other"""

    def __init__(self):
        self.begin = None
        self.end = None
        self.lengthCounter = 0  # Initialize length counter

    def append(self, value):
        # Create a new node with the given value
        newNode = Node(value)

        # If the list is empty, set the new node as both the beginning and end
        if self.begin is None:
            self.begin = newNode
            self.end = newNode
        else:
            # Link the new node to the end of the list
            self.end.right = newNode
            newNode.left = self.end
            self.end = newNode

        # Increment the length counter
        self.lengthCounter += 1

    def __len__(self):
        # Return the current length of the list
        return self.lengthCounter


if __name__ == "__main__":
    # Test 1: Create an empty list and check its length
    print("Test 1: ", len(DoublyLinkedList()))

    # Test 2: Append one item and check the length
    dll = DoublyLinkedList()
    dll.append(10)
    print("Test 2: ", len(dll))

    # Test 3: Append multiple items and check the length
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.append(30)
    print("Test 3: ", len(dll))

    # Test 4: Append and remove an item, then check the length
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.lengthCounter -= 1  # Simulate removal
    print("Test 4: ", len(dll))

    # Test 5: Append items, remove all, and check the length
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.lengthCounter = 0  # Simulate removal of all
    print("Test 5: ", len(dll))

    # Test 6: Append items, remove some, and check the length
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.append(30)
    dll.lengthCounter -= 2  # Simulate removal of two
    print("Test 6: ", len(dll))

    # Test 7: Append items, remove one, append another, and check the length
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.lengthCounter -= 1  # Simulate removal
    dll.append(30)
    print("Test 7: ", len(dll))

    # Test 8: Append a large number of items and check the length
    dll = DoublyLinkedList()
    for i in range(1000):
        dll.append(i)
    print("Test 8: ", len(dll))
