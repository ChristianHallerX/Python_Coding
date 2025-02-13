"""
2. Add Two Numbers (
Medium)
You are given two non-empty linked lists representing two non-negative integers.

The digits are stored in reverse order, and each of their nodes contains a single digit.

Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linkedlist(lst):
    # Helper function to convert a list to a linked_list
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def linkedlist_to_list(node):
    # Helper function to convert a linked_list back to a list
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Construct a new LL with sum
    Edge Cases: carry -> sum greater 9
                one LL is shorter than the other -> if shorter then use 0
    """
    # initialize output LL
    dummyHead = ListNode(0)
    currentNode = dummyHead

    # initialize carry to handle sums greater than 9
    carry = 0

    while l1 is not None or l2 is not None or carry != 0:

        val1 = l1.val if l1 is not None else 0
        val2 = l2.val if l2 is not None else 0

        # sum up and add carry from last iteration
        totalSum = val1 + val2 + carry

        # calc carry for next iteration
        carry = totalSum // 10

        # create new LL and Node with sum
        currentNode.next = ListNode(totalSum % 10)

        # advance output LL pointer forward for next iteration
        currentNode = currentNode.next

        # advance the L1 and L2 pointers forward for next iteration
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next

    # return next of dummyHead, which is the first node of the result LL
    return dummyHead.next


def main():
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    LL1 = list_to_linkedlist(l1)
    LL2 = list_to_linkedlist(l2)
    sumLL = addTwoNumbers(LL1, LL2)
    print(linkedlist_to_list(sumLL), "expected: [7,0,8]")

    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]
    LL1 = list_to_linkedlist(l1)
    LL2 = list_to_linkedlist(l2)
    sumLL = addTwoNumbers(LL1, LL2)
    print(linkedlist_to_list(sumLL), "expected: [8,9,9,9,0,0,0,1]")

    l1 = [0]
    l2 = [0]
    LL1 = list_to_linkedlist(l1)
    LL2 = list_to_linkedlist(l2)
    sumLL = addTwoNumbers(LL1, LL2)
    print(linkedlist_to_list(sumLL), "expected: [0]")


if __name__ == "__main__":
    main()
