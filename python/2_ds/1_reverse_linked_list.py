# Theory:
## A singly linked list is a chain of nodes where each node holds a value
## and a pointer to the next node - unlike an array, there's no contiguous
## memory or O(1) random access, but insertion/removal at a known position
## is O(1) once you're there (no shifting elements). Reversing one is the
## classic entry point into pointer manipulation: you must relink every
## node's "next" pointer to point backward instead of forward, without
## losing your place in the original chain. A recursive approach reverses
## the rest of the list first, then fixes up the current node - simple to
## write but costs O(n) call stack space. The iterative approach walks the
## list once with three pointers (previous, current, next), relinking as
## it goes, using only O(1) extra space.


# Packages:
## dataclasses.dataclass - a concise way to define a node class (alternative to a plain class)
## collections.deque - not for the list itself, but useful for BFS-style traversal of linked structures
## None - Python's null; the natural "end of list" sentinel, no library needed


# Task:
## Given the head of a singly linked list (as a chain of ListNode objects,
## val/next), reverse it and return the new head.
## Test1: Inputs: head = [1, 2, 3, 4, 5]   Outputs: [5, 4, 3, 2, 1]
## Test2: Inputs: head = [1, 2]   Outputs: [2, 1]
## Test3: Inputs: head = []   Outputs: []
## Hint:
## Ugly way: recursion - reverse the rest of the list first, then fix up
## the current node's link; costs O(n) call stack space.
## Right way: iterative - walk the list once with three pointers
## (prev, curr, next), relinking as you go; O(1) space.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def linked_list_to_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def reverse_list_ugly(head):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def reverse_list(head):
    return reverse_list_ugly(head)


# Tests:
def validate():
    cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
        ([1], [1]),
    ]
    for fn in (reverse_list_ugly, reverse_list):
        for values, expected in cases:
            result = linked_list_to_list(fn(build_linked_list(values)))
            assert result == expected, (
                f"{fn.__name__}({values!r}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(linked_list_to_list(reverse_list_ugly(build_linked_list([1, 2, 3, 4, 5]))))
    print(linked_list_to_list(reverse_list_ugly(build_linked_list([1, 2]))))
    print(linked_list_to_list(reverse_list_ugly(build_linked_list([]))))
    print(linked_list_to_list(reverse_list_ugly(build_linked_list([1]))))
