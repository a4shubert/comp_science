# Theory:
## Naive recursive Fibonacci looks elegant but recomputes the same
## subproblems exponentially many times - F(n-1) and F(n-2) each
## independently recompute F(n-3), and so on - giving O(2^n) time despite
## there being only O(n) distinct subproblems. This is the classic argument
## for memoization: caching each computed F(k) (via a dict or
## functools.lru_cache) collapses the exponential blowup down to O(n),
## since every subproblem is now solved once. The iterative two-variable
## version sidesteps the issue entirely by building up from the base cases
## with O(1) space. Recognizing this recompute pattern - a recurrence that
## branches into overlapping subproblems - is the entry point into dynamic
## programming.


# Packages:
## functools.lru_cache / functools.cache - memoize a recursive function automatically
## functools.reduce - fold-based iterative approach without an explicit loop
## itertools.islice - take a lazily-generated sequence up to n items
## collections.deque(maxlen=2) - a fixed-size rolling window of the last two values


# Task:
## Write a function that returns the n-th Fibonacci number
## (1-indexed convention: F(1) = 1, F(2) = 1, F(3) = 2, F(4) = 3, F(5) = 5, ...)
## Test1: Inputs: n = 1   Outputs: 1
## Test2: Inputs: n = 6   Outputs: 8
## Test3: Inputs: n = 11   Outputs: 89


# Solutions:

from functools import reduce


# Space - Time Complexity analysis:
## space: O(n) - list grows to hold n elements
## time: O(n) - the loop runs n-2 times to build up the list

def fibonacci_iterative_ugly(n):
    # keeps the whole sequence in a list - deliberately not space-optimal
    if n < 0:  # O(1) | O(1)
        raise ValueError("N must be non-negative")  # O(1) | O(1)
    if n == 1 or n == 2:  # O(1) | O(1)
        return 1  # O(1) | O(1)
    fib = [1, 1]  # O(1) | O(1)
    for i in range(2, n):  # O(1) | O(n)
        fib.append(fib[-2] + fib[-1])  # O(n) | O(1)
    return fib[-1]  # O(1) | O(1)


# Space - Time Complexity analysis:
## space: O(1) - only two running values (x, y) are kept regardless of n
## time: O(n) - the loop runs n-1 times, updating the pair once per iteration

def fibonacci_iterative_nice(n):
    # only tracks the last two values
    # reject non-positive input up front
    if n <= 0:  # O(1) | O(1)
        raise ValueError("N must be positive")  # O(1) | O(1)
    # base cases: F(1) = F(2) = 1
    if n == 1 or n == 2:  # O(1) | O(1)
        return 1  # O(1) | O(1)
    # x, y track F(2), F(1) initially
    x = y = 1  # O(1) | O(1)
    # advance the pair one Fibonacci step at a time
    for i in range(1, n):  # O(1) | O(n)
        x, y = x + y, x  # O(1) | O(1)
    return y  # O(1) | O(1)


# Space - Time Complexity analysis:
## space: O(n) - call stack depth
## time: O(2^n) - naive, no memoization; total calls double each level

def fibonacci_recursive(n):
    # naive recursion, no memoization
    # reject non-positive input up front
    if n <= 0:  # O(1) | O(1)
        raise ValueError("N must be positive")  # O(1) | O(1)
    # base cases: F(1) = F(2) = 1
    if n == 1 or n == 2:  # O(1) | O(1)
        return 1  # O(1) | O(1)
    # F(n) = F(n-1) + F(n-2), recomputed independently each time
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)  # O(n) | O(2^n)


# Space - Time Complexity analysis:
## space: O(1) - fixed-size tuple accumulator
## time: O(n) - reduce advances the (prev, cur) pair n-1 times

def fibonacci_functional(n):
    # same (prev, cur) update as fibonacci_iterative_nice, expressed as a fold:
    # start from (F(1), F(2)) = (1, 1) and advance the pair n-1 times
    # reject negative input up front
    if n < 0:  # O(1) | O(1)
        raise ValueError("N must be non-negative")  # O(1) | O(1)
    # fold the pair-update lambda over range(n-1), then take the second element
    return reduce(lambda pair, _: (pair[0] + pair[1], pair[0]), range(n - 1), (1, 1))[1]  # O(1) | O(n)


# Tests:
def validate():
    inputs = list(range(1, 12))
    expected = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for fn in (fibonacci_iterative_ugly, fibonacci_iterative_nice, fibonacci_recursive, fibonacci_functional):
        outputs = list(map(fn, inputs))
        assert all(x == y for x, y in zip(expected, outputs)), (
            f"{fn.__name__}: expected {expected}, got {outputs}"
        )
    print("SUCCESS")


if __name__ == "__main__":
    validate()
