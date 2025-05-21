"""
138. Copy List with Random Pointer (Medium)

A linked list of length 'n' is given such that each node contains an additional random pointer,
which could point to any node in the list, or None.

Construct a deep copy of the list.

The deep copy should consist of exactly 'n' brand new nodes, where each new node has its value set to the
value of its corresponding original node.
Both the next and random pointer of the new nodes should point to new nodes in the copied list such that
the pointers in the original list and copied list represent the same list state.
None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes 'X' and 'Y' in the original list, where X.random --> Y,
then for the corresponding two nodes 'x' and 'y' in the copied list, x.random --> y.

Return the 'head' of the copied linked list.

Linked List definition:

The linked list is represented in the input/output as a list of 'n' nodes.

Each node is represented as a pair of [val, random_index] where:
    - val: an integer representing Node.val
    - random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or None
    if it does not point to any node.

Your code will only be given the 'head' of the original linked list.
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


def list_to_linkedlist(data):
    """
    Convert a list of (value, random_index) into a linked list.

    - data[i] = (val_i, rand_i)
      * val_i:       the value for node i
      * rand_i:      integer index of the node that node i.random should point to, or
                     None if node i.random should be None.

    Returns the head of the constructed list (or None if data is empty).
    """
    if not data:
        return None

    # 1) Create all nodes (random & next default to None)
    nodes = [Node(val) for val, _ in data]

    # 2) Wire up .next pointers; last node.next stays None
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # 3) Wire up .random pointers, allowing None
    for i, (_, rand_idx) in enumerate(data):
        if rand_idx is None:
            nodes[i].random = None
        else:
            # assume 0 <= rand_idx < len(nodes)
            nodes[i].random = nodes[rand_idx]

    return nodes[0]


def linkedlist_to_list_of_lists(head):
    """
    Convert a linked list with next & random pointers back into
    a list of [value, random_index] lists.
      - The i-th sublist corresponds to the i-th node along .next from head.
      - random_index is the integer j such that node.random == nodes[j], or None.
    Returns an empty list if head is None.
    """
    # 1) collect node order & map each node to its index
    nodes = []
    idx_map = {}
    cur = head
    idx = 0
    while cur:
        nodes.append(cur)
        idx_map[cur] = idx
        cur = cur.next
        idx += 1

    # 2) build the list-of-lists
    output = []
    for node in nodes:
        rand_idx = idx_map[node.random] if node.random is not None else None
        output.append([node.val, rand_idx])

    return output


def copyRandomList(head: Node) -> Node:
    """
    Two Pass + hash map
        - First pass: create new nodes and copy vals, create pointer hash map (original_LL_node: new_ll_node)
        - Second pass: connect pointers using hash map

    Time Complexity: O(n) linear
    Space Complexity: O(n) hash map
    """

    # Init hash map with edge case None. original: copy
    oldToCopy = {None: None}

    curr = head
    # First pass
    while curr:
        # 1. create new node with original val
        copy = Node(curr.val)
        # 2. write original -> copy node association to hash map
        oldToCopy[curr] = copy
        # 3. iterate loop
        curr = curr.next

    # Reset curr node to head
    curr = head

    # Second pass
    while curr:
        # 1. Fetch the copy node from hash map
        copy = oldToCopy[curr]
        # 2. Connect next and random pointers
        copy.next = oldToCopy[curr.next]
        copy.random = oldToCopy[curr.random]
        # 3. iterate loop
        curr = curr.next

    return oldToCopy[head]


if __name__ == "__main__":
    head = list_to_linkedlist([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
    deepcopyll = copyRandomList(head)
    print(
        linkedlist_to_list_of_lists(deepcopyll),
        "expected: [[7, None],[13, 0],[11, 4],[10, 2],[1, 0]]",
    )

    head = list_to_linkedlist([[1, 1], [2, 1]])
    deepcopyll = copyRandomList(head)
    print(linkedlist_to_list_of_lists(deepcopyll), "expected: [[1, 1],[2, 1]]")

    head = list_to_linkedlist([[3, None], [3, 0], [3, None]])
    deepcopyll = copyRandomList(head)
    print(
        linkedlist_to_list_of_lists(deepcopyll),
        "expected:[[3, None], [3, 0], [3, None]]",
    )
