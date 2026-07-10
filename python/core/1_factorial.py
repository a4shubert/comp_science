# Theory:
## Factorial is a small case study in iteration vs. recursion. An iterative
## loop keeps a fixed amount of state (a running product) regardless of
## input size - O(1) space. Recursion instead breaks the problem into a
## smaller subproblem (n! = n * (n-1)!), but every call adds a frame to the
## call stack until the base case is hit, giving O(n) space and risking a
## RecursionError for large n, since Python's default recursion limit is
## around 1000. A third style, functional/fold-based (functools.reduce),
## expresses the computation as folding a binary operator over a sequence -
## it reads declaratively but is still iterative underneath, so it keeps
## the O(1) space of the loop version.


# Packages:
## math.factorial - built-in factorial, handy for sanity-checking your answer
## functools.reduce - fold a sequence with a binary operator (e.g. multiply)
## operator.mul - multiplication as a plain function, handy with reduce
## sys.setrecursionlimit / sys.getrecursionlimit - inspect/raise Python's recursion depth ceiling


# Task:
## Write a function factorial(n) which returns the n-th factorial
## Test1: Inputs: n = 0   Outputs: 1
## Test2: Inputs: n = 4   Outputs: 24
## Test3: Inputs: n = 7   Outputs: 5040


# Solutions:

from functools import reduce
from operator import mul


# Space - Time Complexity analysis:
## space: O(1) - only a few scalar variables (res, i) are kept regardless of n
## time: O(n) - the loop runs n-1 times, one multiplication per iteration

def factorial_iterative(n):
    # n! = 1 * 2 * 3 * .... n
    # reject negative input up front
    if n < 0:  # O(1) | O(1)
        raise ValueError("N must be non-negative")  # O(1) | O(1)
    # running product, starts at the multiplicative identity
    res = 1  # O(1) | O(1)
    # multiply in each factor from n down to 2
    for i in range(n, 1, -1):  # O(1) | O(n)
        res *= i  # O(1) | O(1)
    return res  # O(1) | O(1)


# Space - Time Complexity analysis:
## space: O(n) - call stack depth n
## time: O(n) - one recursive call per level, from n down to the base case

def factorial_recursive(n):
    # n! = n * (n-1) * (n-2) * ... * 1
    # reject negative input up front
    if n < 0:  # O(1) | O(1)
        raise ValueError("N must be non-negative")  # O(1) | O(1)
    # base case: 0! = 1
    if n == 0:  # exit recursion  # O(1) | O(1)
        return 1  # O(1) | O(1)
    # n! = n times (n-1)!
    return n * factorial_recursive(n - 1)  # O(n) | O(n)


# Space - Time Complexity analysis:
## space: O(1) - reduce is iterative under the hood, no extra structure held
## time: O(n) - reduce folds over n-1 elements, one multiplication per element

def factorial_functional(n):
    # n! expressed as a fold over range(2, n+1)
    # reject negative input up front
    if n < 0:  # O(1) | O(1)
        raise ValueError("N must be non-negative")  # O(1) | O(1)
    # fold multiplication over 2..n, starting from the identity 1
    return reduce(mul, range(2, n + 1), 1)  # O(1) | O(n)


# Tests:
def validate():
    inputs = [0, 1, 2, 3, 4, 5, 6, 7]
    expected = [1, 1, 2, 6, 24, 120, 720, 5040]
    for fn in (factorial_iterative, factorial_recursive, factorial_functional):
        outputs = list(map(fn, inputs))
        assert all(x == y for x, y in zip(expected, outputs)), (
            f"{fn.__name__}: expected {expected}, got {outputs}"
        )
    print("SUCCESS")


if __name__ == "__main__":
    validate()
