"""
142. Linked List Cycle II (Medium)

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return 'None'.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
following the next pointer.

Internally, 'pos' is used to denote the index of the node that tail's 'next' pointer is connected to (0-indexed).

It is -1 if there is no cycle. Note that 'pos' is not passed as a parameter.

Do not modify the linked list.
"""


# Definition for singly-linked_list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linkedlist_cycle(lst, pos=-1):
    if not lst:
        return None  # Return None if the list is empty

    head = ListNode(lst[0])  # Initialize the head node with the first element
    current = head  # Use 'current' to traverse and build the linked_list
    cycle_node = None  # This will point to the node where the cycle should connect

    if pos == 0:
        cycle_node = head  # If pos is 0, cycle should start at the head

    for i in range(1, len(lst)):
        current.next = ListNode(lst[i])  # Create the next node and link it
        current = current.next  # Move 'current' to the newly created node

        if i == pos:
            cycle_node = current  # Mark the node where the cycle should start

    if pos >= 0 and cycle_node:
        current.next = (
            cycle_node  # Connect the tail to the cycle node to form the cycle
        )

    return head


def detectCycle(head: ListNode) -> ListNode:
    return None


def main():
    head = list_to_linkedlist_cycle(lst=[3, 2, 0, -4], pos=1)
    print(detectCycle(head), "expected: 1")

    head = list_to_linkedlist_cycle(lst=[1, 2], pos=0)
    print(detectCycle(head), "expected: 0")

    head = list_to_linkedlist_cycle(lst=[1], pos=-1)
    print(detectCycle(head), "expected: -1")


if __name__ == "__main__":
    main()
