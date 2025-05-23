"""
25. Reverse Nodes in k-Group (Hard)

'k' is a positive integer and is less than or equal to the length of the linked list.

You must reverse the first 'k' nodes in the linked list, and then reverse the next 'k' nodes, and so on.
If there are fewer than k nodes left, leave the nodes as they are.

You may not alter the values in the list's nodes, only node pointers may be changed.
"""


# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linkedlist(lst):
    """
    Helper function to convert a list to a linked list
    """
    if not lst:
        return None
    head = Node(lst[0])
    current = head
    for value in lst[1:]:
        current.next = Node(value)
        current = current.next
    return head


def linkedlist_to_list(node: Node):
    """
    Helper function to convert a linked_list back to a list
    """
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst


def reverseKGroup(head: Node, k: int) -> Node:
    """
    Use dummy node before head to avoid edge cases
    Reverse groups of nodes of length k.
    """
    dummy = Node(val=0, next=head)

    # use a namded node that is always right before a group of reversal nodes
    groupPrev = dummy

    # each iteration reverses a group
    while True:
        kth = getkth(groupPrev, k)
        # If group is shorter than k, break the loop - No reversal required
        if not kth:
            break
        groupNext = kth.next

        # Reverse group ends
        prev, curr = kth.next, groupPrev.next

        # Reverse group nodes
        while curr != groupNext:
            tmp = curr.next
            # Reverse pointer
            curr.next = prev
            prev = curr
            # shift forward
            curr = tmp

        # Temporarily store the first node in group
        tmp = groupPrev.next
        # kth was the last node in the group, now it becomes the first
        groupPrev.next = kth
        # Update groupPrev for the next iteration
        groupPrev = tmp

    # dummy.next is the head
    return dummy.next


def getkth(curr, k):
    """
    Helper function to return the k-th node after the curr.
    Returns None if there are less than k nodes
    """
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr


def main():
    lst = [1, 2, 3, 4, 5, 6]
    head = list_to_linkedlist(lst)
    k = 3
    head = reverseKGroup(head=head, k=k)
    print(linkedlist_to_list(node=head), "expected: [3, 2, 1, 6, 5, 4]")

    lst = [1, 2, 3, 4, 5]
    head = list_to_linkedlist(lst)
    k = 3
    head = reverseKGroup(head=head, k=k)
    print(linkedlist_to_list(node=head), "expected: [3, 2, 1, 4, 5]")


if __name__ == "__main__":
    main()
