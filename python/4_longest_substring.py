# Theory:
## The sliding window technique solves "find the best contiguous
## subarray/substring satisfying some property" problems in O(n) instead
## of the O(n^2) or O(n^3) of checking every substring explicitly. Two
## pointers (left, right) define the current window: right expands to
## include new elements, and left contracts only when the window violates
## the property (e.g. a repeated character). Because each pointer only
## ever moves forward, total pointer movement is bounded by 2n, giving
## linear time overall. A hash set or dict often tracks what's "in" the
## window (or each element's last-seen index), letting you shrink or jump
## the window efficiently instead of rechecking it from scratch.


# Packages:
## set - track distinct elements currently "in" the window
## dict / collections.defaultdict - track counts or last-seen index per element
## collections.Counter - frequency counting within the current window
## collections.deque - a windowed queue when you need FIFO eviction


# Task:
## Given a string s, find the length of the longest substring without
## repeating characters.
## Test1: Inputs: s = "abcabcbb"   Outputs: 3
## Test2: Inputs: s = "bbbbb"   Outputs: 1
## Test3: Inputs: s = "pwwkew"   Outputs: 3
## Hint:
## Ugly way: nested loops
## Right way: dict (or set)


# Solutions:

# Space - Time Complexity analysis:
## space: O(n) - holding one substring up to length n at a time
## time: O(n^3) - O(n^2) (i, j) pairs, each costing O(n) to build substr + set

def length_of_longest_substring_ugly(s):
    res = 0  # O(1) | O(1)
    for i in range(len(s)):  # O(1) | O(n)
        for j in range(i + 1, len(s) + 1):  # O(1) | O(n)
            substr = s[i:j]  # O(n) | O(n)
            if len(set(substr)) == len(substr):  # O(n) | O(n)
                res = max(res, len(substr))  # O(1) | O(1)
    return res  # O(1) | O(1)


# Space - Time Complexity analysis:
## space: O(n) - window set can grow to hold up to n chars
## time: O(n) - each char enters/leaves the window at most once

def length_of_longest_substring_set(s):
    # sliding window, shrink from the left when a duplicate enters the window
    left = 0  # O(1) | O(1)
    window = set()  # O(1) | O(1)
    res = 0  # O(1) | O(1)
    for right in range(len(s)):  # O(1) | O(n)
        while s[right] in window:  # O(1) | O(1)
            window.remove(s[left])  # O(1) | O(1)
            left += 1  # O(1) | O(1)
        window.add(s[right])  # O(n) | O(1)
        res = max(res, right - left + 1)  # O(1) | O(1)
    return res  # O(1) | O(1)


# Space - Time Complexity analysis:
## space: O(n) - last_seen dict can grow to hold up to n entries
## time: O(n) - single pass, O(1) average dict ops

def length_of_longest_substring(s):
    # sliding window, jump left directly using each char's last-seen index
    left = 0  # O(1) | O(1)
    last_seen = {}  # O(1) | O(1)
    res = 0  # O(1) | O(1)
    for right, ch in enumerate(s):  # O(1) | O(n)
        if ch in last_seen and last_seen[ch] >= left:  # O(1) | O(1)
            left = last_seen[ch] + 1  # O(1) | O(1)
        last_seen[ch] = right  # O(n) | O(1)
        res = max(res, right - left + 1)  # O(1) | O(1)
    return res  # O(1) | O(1)


# Tests:
def validate():
    cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("dvdf", 3),
    ]
    for fn in (
        length_of_longest_substring_ugly,
        length_of_longest_substring_set,
        length_of_longest_substring,
    ):
        for s, expected in cases:
            result = fn(s)
            assert result == expected, (
                f"{fn.__name__}({s!r}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    validate()
