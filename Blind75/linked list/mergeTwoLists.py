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


def mergeTwoLists(list1, list2):
    # Start with dummy to avoid inserting into empty list (e.g., examples 1 and 2)
    dummyNode = ListNode()
    tail = dummyNode

    while list1 and list2:
        if list1.val < list2.val:
            # Define pointer from tail to list1
            tail.next = list1
            # Define pointer forward from list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # What if one list is empty and one is not?
    # Insert remaining, whole section of list and insert
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    # Return first item of new list after dummy (i.e., head)
    return dummyNode.next


def main():
    list1 = list_to_linkedlist([1, 2, 4])
    list2 = list_to_linkedlist([1, 3, 4])
    print(linkedlist_to_list(mergeTwoLists(list1, list2)))

    list1 = list_to_linkedlist([])
    list2 = list_to_linkedlist([])
    print(linkedlist_to_list(mergeTwoLists(list1, list2)))

    list1 = list_to_linkedlist([])
    list2 = list_to_linkedlist([0])
    print(linkedlist_to_list(mergeTwoLists(list1, list2)))


if __name__ == "__main__":
    main()
