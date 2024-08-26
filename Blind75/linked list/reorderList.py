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


def printLinkedList(msg, head):
    print(msg, end='')
    ptr = head
    # print all node values
    while ptr:
        print(ptr.val, end=' —> ')
        ptr = ptr.next

    # print head
    print('None')


def reorderList(head: ListNode) -> None:
    #  Alternate between beginning of list and end of list
    ###################


def main():

    a = None
    for i in reversed([1, 2, 3, 4]):
        a = ListNode(val=i, next=a)
    printLinkedList(msg='First List: ', head=a)

    output_head = reorderList(head=a)
    printLinkedList('After Merge: ', output_head)
    print(' expected: [1, 5, 2, 4, 3]')


    b = None
    for i in reversed([1, 2, 3, 4, 5]):
        b = ListNode(val=i, next=b)
    printLinkedList(msg='First List: ', head=b)

    output_head = reorderList(head=b)
    printLinkedList('After Merge: ', output_head)
    print(' expected: [1, 5, 2, 4, 3]')
