"""
206. Reverse Linked List (easy)

Given the 'head' of a singly linked list, reverse the list, and return the reversed list.

Example:
    Input:    head=1->2->3->4->5->None
    Output:  None<-1<-2<-3<-4<-5=head

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

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


def reverseListIterative(head):
    """
    Traverse over list items starting at head and reverse connection around current pointer.
    Null/None is at the bottom end of list pointing at first item.
    Head is a regular element at top end of list pointing nowhere.
    Instantiation of ListNode class as 'curr' with .next attribute.
    prev, next pointers are variables.
    Reverse order of pointers around 'current' object.
    Time complexity: O(n), iterate over list once
    Space complexity: O(1), just store pointers, no data structures
    """

    # Curr is the list object, it points nowhere, hence prev=None
    prev, curr = None, head

    # Continue moving over linked list while whe have not arrived at a None
    while curr is not None:
        # Before flipping, store original next to temp var
        temp_next = curr.next

        # Flip direction
        curr.next = prev

        # Move forward one node
        prev = curr

        # Move forward one node to original next from temp var
        curr = temp_next
    return prev


def reverseListRecursive(head):
    # Time complexity: O(n) linear
    # memory complexity: O(n) linear (worse than iterative)

    if head is not None:
        return None

    newHead = head
    if head.next is not None:
        newHead = self.reverseListRecursive(head.next)
        head.next.next = newHead
    head.next = None

    return newHead


def main():
    head = list_to_linkedlist([1, 2, 3, 4, 5])
    print(linkedlist_to_list(reverseListIterative(head)), "expected: [5, 4, 3, 2, 1]")

    head = list_to_linkedlist([1, 2])
    print(linkedlist_to_list(reverseListIterative(head)), "expected: [2, 1]")

    head = list_to_linkedlist([])
    print(linkedlist_to_list(reverseListIterative(head)), "expected: []")


if __name__ == "__main__":
    main()
