"""
21. Merge Two Sorted Lists (easy)

You are given the heads of two sorted linked lists 'list1' and 'list2'.

Merge the two lists in a one *sorted* list. The list should be made by splicing together the nodes of the first
two lists.

Return the head of the merged linked list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:



def main():
    solution = Solution()
    print(solution(list1=[1, 2, 4], list2=[1, 3, 4]), "expected: [1, 1, 2, 3, 4, 4]")
    print(solution(list1=[], list2=[]), "expected: []")
    print(solution(list1=[], list2=[0]), "expected: [0]")


if __name__ == '__main__':
    main()
