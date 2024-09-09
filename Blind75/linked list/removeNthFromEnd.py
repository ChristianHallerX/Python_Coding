"""
19. Remove Nth Node From End of List (Medium)

Given the head of a linked list, remove the nth node from the end of the list and return its head.

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linkedlist(lst):
    # Helper function to convert a list to a linked list
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def linkedlist_to_list(node):
    # Helper function to convert a linked list back to a list
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst


def removeNthFromEnd(head, n):
    """
    Use two pointers left/right with distance of "n". Add a dummy node at the start, so we find the node before n.
    Start left pointer at dummy, right pointer at start + n.
    Move them both until the right pointer hits the position after the last node (end, None).
    The left pointer should be one node before the correct node to delete.
    Finally, set left pointer node next to left pointer next.next to remove the node at n.
    Return dummy.next
    Time complexity: O(n)
    Space complexity: O(1) no extra data structures beyond pointers.
    """
    # Insert dummy at head of list for left pointer initial position
    dummy = ListNode(0, head)
    left = dummy

    # Move right pointer to initial position
    right = head
    while n > 0 and right is not None:
        right = right.next
        n -= 1

    # Move left+right in lockstep until right is at end/None
    while right:
        left = left.next
        right = right.next

    # Delete node/connect left with left.next.next
    left.next = left.next.next

    return dummy.next


def main():
    head = list_to_linkedlist([1, 2, 3, 4, 5])
    n = 2
    print(linkedlist_to_list(removeNthFromEnd(head, n)), "expected: [1, 2, 3, 5]")

    n = 1
    head = list_to_linkedlist([1])
    print(linkedlist_to_list(removeNthFromEnd(head, n)), "expected: []")

    n = 1
    head = list_to_linkedlist([1, 2])
    print(linkedlist_to_list(removeNthFromEnd(head, n)), "expected: [1]")


if __name__ == "__main__":
    main()
