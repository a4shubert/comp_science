// Theory:
// A stack is a LIFO (last-in-first-out) structure supporting O(1)
// push/pop from one end - C++'s std::vector or std::deque both work as
// the underlying container for std::stack, with deque preferred when
// you'll also need O(1) operations from the other end. Stacks are the
// natural fit for any "matching/nesting" problem: parentheses validation,
// undo history, DFS traversal, expression parsing. The core invariant for
// bracket matching is that whatever opened most recently must be the next
// thing closed - so you push openers and, on a closer, check it against
// whatever is currently on top, popping only on a match and failing
// immediately otherwise.

// Headers & STL components:
// <stack> - std::stack, a container adaptor giving LIFO push/pop/top
// <deque> - O(1) operations at both ends, the default underlying container for std::stack
// <unordered_map> - map each closing bracket to its matching opener
// <string> - repeated substring removal, the brute-force approach here

// Task:
// Given a string s containing just the characters '(', ')', '{', '}', '[',
// ']', determine if it is valid. A string is valid if every opening
// bracket is closed by the same type of bracket, and brackets close in
// the correct order.
// Test1: Inputs: s = "()"   Outputs: true
// Test2: Inputs: s = "()[]{}"   Outputs: true
// Test3: Inputs: s = "(]"   Outputs: false
// Hint:
// Ugly way: string replacement in a loop - repeatedly strip out matched
// adjacent pairs until nothing changes, then check what's left over.
// Right way: std::stack - push opening brackets as you go, and check each
// closing bracket against whatever is currently on top.

// Solutions:
#include <cassert>
#include <iostream>
#include <stack>
#include <string>
#include <unordered_map>
#include <vector>

// Space - Time Complexity analysis:
// space: O(n) - one current string alive at a time
// time: O(n^2) - up to n passes for deeply nested input, each pass O(n)
bool is_valid_ugly(std::string s) {
    while (true) {  // O(1) | O(n)
        std::string new_s = s;  // O(n) | O(n)
        for (const auto& pair : {"()", "[]", "{}"}) {  // O(1) | O(1)
            size_t pos;  // O(1) | O(1)
            while ((pos = new_s.find(pair)) != std::string::npos) {  // O(1) | O(n)
                new_s.erase(pos, 2);  // O(n) | O(n)
            }
        }
        if (new_s == s) break;  // O(1) | O(n)
        s = new_s;  // O(n) | O(n)
    }
    return s.empty();  // O(1) | O(1)
}

// Space - Time Complexity analysis:
// space: O(n) - stack can hold up to n opens
// time: O(n) - single pass, O(1) average unordered_map lookup + O(1) stack top/pop
bool is_valid(const std::string& s) {
    // stack of opening brackets seen so far, not yet closed
    std::stack<char> st;  // O(1) | O(1)
    // maps each closing bracket to the opener it must match
    std::unordered_map<char, char> pairs = {{')', '('}, {'}', '{'}, {']', '['}};  // O(1) | O(1)
    // walk through s once
    for (char elem : s) {  // O(1) | O(n)
        // opening bracket: push it
        if (elem == '(' || elem == '{' || elem == '[') {  // O(1) | O(1)
            st.push(elem);  // O(n) | O(1)
        } else {
            // closing bracket: it must match whatever is on top
            if (st.empty() || st.top() != pairs[elem]) {  // O(1) | O(1)
                return false;
            }
            // matched - remove that opener from the stack
            st.pop();  // O(1) | O(1)
        }
    }
    // valid only if every opener got closed
    return st.empty();  // O(1) | O(1)
}

// Tests:
void validate() {
    struct Case {
        std::string s;
        bool expected;
    };
    std::vector<Case> cases = {
        {"()", true},       {"()[]{}", true}, {"(]", false},
        {"([)]", false},    {"{[]}", true},   {"", true},
        {"(((", false},     {"(])", false},   {")", false},
    };
    for (const auto& c : cases) {
        assert(is_valid_ugly(c.s) == c.expected);
        assert(is_valid(c.s) == c.expected);
    }
    std::cout << "SUCCESS" << std::endl;
}

int main() {
    validate();
    return 0;
}
