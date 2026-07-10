# Theory:
## A stack is a LIFO (last-in-first-out) structure supporting O(1)
## push/pop from one end - Python's list or collections.deque both work,
## with deque preferred when you'll also need O(1) operations from the
## other end. Stacks are the natural fit for any "matching/nesting"
## problem: parentheses validation, undo history, DFS traversal, expression
## parsing. The core invariant for bracket matching is that whatever opened
## most recently must be the next thing closed - so you push openers and,
## on a closer, check it against whatever is currently on top, popping
## only on a match and failing immediately otherwise.


# Packages:
## list - the simplest stack via append()/pop()
## collections.deque - O(1) operations at both ends, preferred for queue-like use
## str.replace - repeated substring removal, the brute-force approach here


# Task:
## Given a string s containing just the characters '(', ')', '{', '}', '[',
## ']', determine if it is valid. A string is valid if every opening bracket
## is closed by the same type of bracket, and brackets close in the correct
## order.
## Test1: Inputs: s = "()"   Outputs: True
## Test2: Inputs: s = "()[]{}"   Outputs: True
## Test3: Inputs: s = "(]"   Outputs: False
## Hint:
## Ugly way: str.replace in a loop - repeatedly strip out matched adjacent
## pairs until nothing changes, then check what's left over.
## Right way: list (as a stack) - push opening brackets as you go, and check
## each closing bracket against whatever is currently on top.


# Solutions:

from collections import deque


# Space - Time Complexity analysis:
## space: O(n) - one current string alive at a time
## time: O(n^2) - up to n passes for deeply nested input, each pass O(n)

def is_valid_ugly(s):
    # repeatedly remove matched adjacent pairs until nothing changes
    while True:  # O(1) | O(n)
        new_s = s  # O(n) | O(1)
        for pair in ("()", "[]", "{}"):  # O(1) | O(1)
            new_s = new_s.replace(pair, "")  # O(n) | O(n)
        if new_s == s:  # O(n) | O(n)
            break
        s = new_s
    return not s  # O(1) | O(1)


# Space - Time Complexity analysis:
## space: O(n) - stack can hold up to n opens
## time: O(n) - single pass, O(1) average dict lookup + O(1) deque end access

def is_valid(s):
    q = deque()  # O(1) | O(1)
    pairs = {")": "(", "}": "{", "]": "["}  # O(1) | O(1)
    for elem in s:  # O(1) | O(n)
        if elem in ("(", "{", "["):  # O(1) | O(1)
            q.append(elem)  # O(n) | O(1)
        else:
            if not q or q[-1] != pairs[elem]:  # O(1) | O(1)
                return False
            q.pop()  # O(1) | O(1)
    return not q  # O(1) | O(1)


# Tests:
def validate():
    cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(((", False),
        ("(])", False),
        (")", False),
    ]
    for fn in (is_valid_ugly, is_valid):
        for s, expected in cases:
            result = fn(s)
            assert result == expected, f"{fn.__name__}({s!r}): expected {expected}, got {result}"
    print("SUCCESS")


if __name__ == "__main__":
    validate()
