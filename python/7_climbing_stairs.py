# Theory:
## Dynamic programming solves problems whose recurrence branches into
## overlapping subproblems (unlike divide-and-conquer, where subproblems
## don't overlap) by ensuring each distinct subproblem is computed once and
## reused. Two equivalent strategies: top-down memoization, where you keep
## the natural recursive structure but cache each return value
## (functools.lru_cache is the easiest way in Python), and bottom-up
## tabulation, where you iteratively build a table of answers from the base
## cases upward - usually trading the recursion's call-stack space for an
## explicit array (or just a few variables, if only the last couple of
## states matter).


# Packages:
## functools.lru_cache / functools.cache - top-down memoization with minimal code change
## functools.reduce - fold-based bottom-up tabulation without an explicit loop
## sys.setrecursionlimit - relevant if recursion depth becomes a concern for large n


# Task:
## You're climbing a staircase with n steps. Each move you can climb either
## 1 or 2 steps. Return the number of distinct ways to reach the top.
## (n is a positive integer.)
## Test1: Inputs: n = 1   Outputs: 1
## Test2: Inputs: n = 4   Outputs: 5
## Test3: Inputs: n = 10   Outputs: 89
## Hint:
## Ugly way: naive recursion - same recurrence shape as the naive Fibonacci
## you already wrote, no caching.
## Right way: functools.lru_cache - memoize the recursive calls so each n
## is only computed once.


# Solutions:
from functools import lru_cache


# Space - Time Complexity analysis:
## space: O(n) - call stack depth n
## time: O(2^n) - same recurrence shape as naive Fibonacci; total calls double each level


def climb_stairs_ugly(n):
    if n == 1:  # O(1) | O(1)
        return 1  # O(1) | O(1)
    if n == 2:  # O(1) | O(1)
        return 2  # O(1) | O(1)
    return climb_stairs_ugly(n - 1) + climb_stairs_ugly(n - 2)  # O(n) | O(2^n)


# Space - Time Complexity analysis:
## space: O(n) - cache holds one entry per distinct n, plus call stack depth n
## time: O(n) - each distinct n is computed once thanks to the cache; O(1) work per call after that


@lru_cache(maxsize=None)
def climb_stairs(n):
    # base case: one step, one way
    if n == 1:  # O(1) | O(1)
        return 1  # O(1) | O(1)
    # base case: two steps, two ways (1+1 or 2)
    if n == 2:  # O(1) | O(1)
        return 2  # O(1) | O(1)
    # ways to reach n = ways to reach n-1, plus ways to reach n-2 -
    # lru_cache means each distinct n is only ever computed once
    return climb_stairs(n - 1) + climb_stairs(n - 2)  # O(n) | O(n)


# Tests:
def validate():
    cases = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (6, 13),
        (10, 89),
    ]
    for fn in (climb_stairs_ugly, climb_stairs):
        for n, expected in cases:
            result = fn(n)
            assert result == expected, (
                f"{fn.__name__}({n}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    validate()
