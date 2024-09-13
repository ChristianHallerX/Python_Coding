"""
23. Merge k Sorted Lists (hard)
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

(extension of LC 21, merge two lists)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    """
    Helper function (LC 21) Merge Two Linked Lists.
    """
    # Start with dummy to avoid inserting into empty list
    dummyNode = ListNode()
    tail = dummyNode

    # While both lists are not empty, attach the list with the lower value (sorting)
    while list1 and list2:
        if list1.val < list2.val:
            # Define pointer from tail to list1
            tail.next = list1
            # Define pointer forward from list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        # In any case, move tail forward (to whichever L1 or L2) for next iteration
        tail = tail.next

    # What if at the start, one list is empty and one is not?
    # -> Insert the whole of existing list, ignore the other
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    # Return node after dummy
    return dummyNode.next


def mergeKLists(lists: list[ListNode]) -> ListNode:
    """
    Use the merge-sort technique for combining pairs of lists.
    Return single, sorted LL.
    Requires helper function for merging two linked lists.
    Time complexity: O(n*logk) instead of O(n*k)
    """
    if not lists or len(lists) == 0:
        return None

    # Pair merging continually until only a single linked list is left on 'lists'
    while len(lists) > 1:
        # Temp variable
        mergedLists = []

        # Merge every second list and neighbor (pairwise)
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            # List 2 may be out of bounds if we have an odd number of lists. Check that first.
            l2 = lists[i + 1] if ((i + 1) < len(lists)) else None
            mergedLists.append(mergeTwoLists(list1=l1, list2=l2))

        # Toss the new merged Linked Lists back on 'lists' of the while loop and merge again
        lists = mergedLists
    return lists[0]


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


def main():
    input = [list_to_linkedlist(i) for i in [[1, 4, 5], [1, 3, 4], [2, 6]]]
    print(linkedlist_to_list(mergeKLists(lists=input)))

    input = []
    print(linkedlist_to_list(mergeKLists(lists=input)))

    input = [[]]
    print(linkedlist_to_list(mergeKLists(lists=input)))


if __name__ == "__main__":
    main()
