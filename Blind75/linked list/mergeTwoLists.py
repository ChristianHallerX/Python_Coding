"""
21. Merge Two Sorted Lists (easy)

You are given the heads of *two sorted* linked lists 'list1' and 'list2'.

Merge the two lists in a *one sorted* list. The list should be made by splicing together the nodes of the first
two lists.

Return the head of the merged linked list.
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


def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    # Process:
    # Create a new output linked-list starting at dummy tail and work towards head.
    # Loop through l1 and l2 nodes in parallel.
    # While both nodes are not None (not empty), add the smaller node of l1 and l2 to output tail.
    # Move the tail forward and make current l1/l2 node the tail.
    # If one list is None (empty, l1/l2 are unequal length),
    # then insert remaining part to output. Since it is pre-sorted, no sorting required.
    dummy = ListNode()
    tail = dummy

    while list1 and list2:  # are BOTH not None/empty
        if list1.val < list2.val:
            tail.next = list1  # write after tail
            list1 = list1.next  # move list1 node forward
        else:
            tail.next = list2  # write after tail
            list2 = list2.next  # move list2 node forward
        tail = tail.next  # make current node the tail / move tail forward

    # if only one list is not None, add that one to the tail
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    return dummy.next


def main():
    a = b = None
    for i in reversed([1, 2, 4]):
        a = ListNode(val=i, next=a)
    printLinkedList(msg='First List: ', head=a)

    for i in reversed([1, 3, 4]):
        b = ListNode(val=i, next=b)
    printLinkedList('Second List: ', b)

    head = mergeTwoLists(list1=a, list2=b)
    printLinkedList('After Merge: ', head)
    print("expected: [1, 1, 2, 3, 4, 4]")


    a = b = None
    for i in reversed([]):
        a = ListNode(val=i, next=a)
    printLinkedList('First List: ', a)

    for i in reversed([]):
        b = ListNode(val=i, next=b)
    printLinkedList('Second List: ', b)

    head = mergeTwoLists(list1=a, list2=b)
    printLinkedList('After Merge: ', head)
    print("expected: []")


    a = b = None
    for i in reversed([]):
        a = ListNode(val=i, next=a)
    printLinkedList('First List: ', a)

    for i in reversed([0]):
        b = ListNode(val=i, next=b)
    printLinkedList('Second List: ', b)

    head = mergeTwoLists(list1=a, list2=b)
    printLinkedList('After Merge: ', head)
    print("expected: [0]")


if __name__ == '__main__':
    main()
