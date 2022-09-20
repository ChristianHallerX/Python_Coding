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


def reverseListIterative(head: Optional[ListNode]) -> Optional[ListNode]:
    # Time complexity: O(n) linear
    # memory complexity: O(1) constant, only using pointers

    # initialization at head
    curr = head  # first node
    prev = None  # node before first node/head

    while curr is not None:

        # save the original next node in var, so we can move forward to it later
        temp_nxt = curr.next

        # reverse the direction of the link pointing backwards
        curr.next = prev

        # move prev forward to the right node (curr)
        prev = curr

        # move curr forward to the right node ahead of curr using the temp var
        curr = temp_nxt

    # return 'prev', since 'curr' should now be None
    return prev


def reverseListRecursive(head: Optional[ListNode]) -> Optional[ListNode]:
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
    print(reverseListIterative(head=[1, 2, 3, 4, 5]), 'expected: [5, 4, 3, 2, 1]')
    print(reverseListIterative(head=[1, 2]), 'expected: [2, 1]')
    print(reverseListIterative(head=[]), 'expected: []')

if __name__ == '__main__':
    main()
