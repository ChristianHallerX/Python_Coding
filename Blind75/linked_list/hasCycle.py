"""
141. Linked List Cycle (Easy)

Given head, the head of a linked_list, determine if the linked_list has a cycle/loop in it.

There is a cycle in a linked_list if there is some node in the list that can be reached again by
continuously following the next pointer.

Internally, 'pos' is used to denote the index of the node that tail's next pointer is connected to.

Note that 'pos' is not passed as a parameter.

Return 'True' if there is a cycle in the linked_list. Otherwise, return 'False'.
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


def hasCycle(head) -> bool:
    """
    'Floyd’s cycle finding algorithm' aka 'Hare-Tortoise algorithm'
    Is the tail node connected to an earlier node in the linked_list? Are we visiting the same node twice?

    Solution 1: Add node object itself to set. All nodes need to be copied to a new data structure.
                Space complexity: O(n) (bad)
                Time complexity: O(n)
    Solution 2: Slow moving pointer (one-step) and fast moving pointer (two-step).
                If loop, slow pointer will catch up with fast, if no loop, fast will go to end of linked list (None).
                Space complexity O(1) (good)
                Time Complexity: O(n)

    "Pos" is for illustration purposes in the examples what the connected node is.
    It is internal and not an accessible parameter visible.

    """
    # Initialize fast and slow pointers
    fast = head
    slow = head

    while fast and fast.next:  # is not None
        slow = slow.next
        fast = fast.next.next

        # Slow pointer catches up with fast (linked-list loop detected), while-loop broken.
        if slow == fast:
            return True

    # Arrived at None/end of list (no linked-list loop found)
    return False


def main():
    head = list_to_linkedlist_cycle(lst=[3, 2, 0, -4], pos=1)
    print(hasCycle(head), "expected: True")

    head = list_to_linkedlist_cycle(lst=[1, 2], pos=0)
    print(hasCycle(head), "expected: True")

    head = list_to_linkedlist_cycle(lst=[1], pos=-1)
    print(hasCycle(head), "expected: False")


if __name__ == "__main__":
    main()
