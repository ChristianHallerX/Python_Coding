"""
143. Reorder List (Medium)

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Do not return anything, modify head in-place instead.
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


def reorderList(head) -> None:
    """
    Do not return anything, modify head in-place instead.
    You get the head object of a linked list.

    Pattern: Create new list with nodes alternating from head and tail.
    1. Find middle of the list: a slow pointer (one step, start @node1)
    and a fast pointer (two steps, start @node2).
    2. Then reverse second half. Works with even and uneven list lengths. Second half starts one node after slow.
    3. Attach to a new list from list1 and list2 alternating.
    4. Always create temporary next pointers before breaking and moving nodes.
    Time complexity: O(n)
    Space complexity: O(1)
    """
    # Initialize starting location
    slow = head
    fast = head.next
    # Find middle: Move pointers across linked list. When fast reaches end, slow will be in middle.
    while fast and fast.next:  # while not None and not reached end
        slow = slow.next
        fast = fast.next.next

    # Store node where the second half starts. One node after slow.
    second = slow.next
    # Split first and second halfs apart
    slow.next = None

    # "Reverse Linked List" Problem. Reverse second half
    previous = None
    while second:
        # Store original connection before breaking
        temp_next = second.next
        # Reverse direction
        second.next = previous
        # Move pointers
        previous = second
        second = temp_next

    # Merge two halves of list
    first = head
    second = previous
    while second:
        # Store original connection before breaking
        temp1, temp2 = first.next, second.next
        # Attach to first half node from second half portion
        first.next = second
        # Attach to second half node from first half portion
        second.next = temp1
        # Move pointers
        first = temp1
        second = temp2

    # For printing purposes
    return head


def main():
    list1 = list_to_linkedlist([1, 2, 3, 4])
    print(linkedlist_to_list(reorderList(head=list1)))

    list2 = list_to_linkedlist([1, 2, 3, 4, 5])
    print(linkedlist_to_list(reorderList(head=list2)))


if __name__ == "__main__":
    main()
