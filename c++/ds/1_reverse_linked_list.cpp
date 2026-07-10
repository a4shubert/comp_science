// Theory:
// A singly linked list is a chain of nodes where each node holds a value
// and a pointer to the next node - unlike a vector, there's no contiguous
// memory or O(1) random access, but insertion/removal at a known position
// is O(1) once you're there (no shifting elements). Reversing one is the
// classic entry point into pointer manipulation: you must relink every
// node's "next" pointer to point backward instead of forward, without
// losing your place in the original chain. A recursive approach reverses
// the rest of the list first, then fixes up the current node - simple to
// write but costs O(n) call stack space. The iterative approach walks the
// list once with three pointers (previous, current, next), relinking as
// it goes, using only O(1) extra space.

// Headers & STL components:
// <memory> - std::unique_ptr/shared_ptr, for owning nodes safely (a raw-pointer list is used here for simplicity)
// <vector> - used only for the test-harness conversion helpers
// <forward_list> - the STL's own singly linked list, for comparison

// Task:
// Given the head of a singly linked list (a chain of ListNode, val/next),
// reverse it and return the new head.
// Test1: Inputs: head = {1, 2, 3, 4, 5}   Outputs: {5, 4, 3, 2, 1}
// Test2: Inputs: head = {1, 2}   Outputs: {2, 1}
// Test3: Inputs: head = {}   Outputs: {}
// Hint:
// Ugly way: recursion - reverse the rest of the list first, then fix up
// the current node's link; costs O(n) call stack space.
// Right way: iterative - walk the list once with three pointers
// (prev, curr, next), relinking as you go; O(1) space.

// Solutions:
#include <cassert>
#include <iostream>
#include <vector>

struct ListNode {
    int val;
    ListNode* next;
    explicit ListNode(int v) : val(v), next(nullptr) {}
};

ListNode* build_linked_list(const std::vector<int>& values) {
    ListNode dummy(0);
    ListNode* curr = &dummy;
    for (int v : values) {
        curr->next = new ListNode(v);
        curr = curr->next;
    }
    return dummy.next;
}

std::vector<int> linked_list_to_vector(ListNode* head) {
    std::vector<int> values;
    while (head) {
        values.push_back(head->val);
        head = head->next;
    }
    return values;
}

// Space - Time Complexity analysis:
// space:
// time:

ListNode* reverse_list_ugly([[maybe_unused]] ListNode* head) {
    // TODO: implement
    return nullptr;
}

// Space - Time Complexity analysis:
// space:
// time:

ListNode* reverse_list(ListNode* head) {
    return reverse_list_ugly(head);
}

// Tests:
void validate() {
    struct Case {
        std::vector<int> values;
        std::vector<int> expected;
    };
    std::vector<Case> cases = {
        {{1, 2, 3, 4, 5}, {5, 4, 3, 2, 1}},
        {{1, 2}, {2, 1}},
        {{}, {}},
        {{1}, {1}},
    };
    for (const auto& c : cases) {
        assert(linked_list_to_vector(reverse_list_ugly(build_linked_list(c.values))) == c.expected);
        assert(linked_list_to_vector(reverse_list(build_linked_list(c.values))) == c.expected);
    }
    std::cout << "SUCCESS" << std::endl;
}

int main() {
    validate();
    return 0;
}
