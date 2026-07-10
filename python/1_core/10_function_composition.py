# Theory:
## Function composition is the functional-programming idea of building a new
## function by chaining several smaller ones together: compose(f, g, h)(x)
## means h runs first, then g, then f - each function's output feeds the
## next one's input, same convention as mathematical composition f(g(h(x))).
## It's a way to build complex behavior out of small, independently testable
## pieces instead of one large imperative function. Python doesn't have a
## built-in compose, but functools.reduce is the natural tool for folding a
## list of functions into a single callable: it repeatedly combines pairs
## the same way it would repeatedly combine numbers when summing a list.
## The empty-composition case (no functions at all) should behave as the
## identity function, same as summing an empty list gives 0.


# Packages:
## functools.reduce - fold an iterable down to a single value/callable using a binary function
## functools.partial - fix some arguments of a function ahead of time
## operator module - functional versions of +, *, etc., often paired with reduce
## itertools.chain - lazily concatenate iterables, useful in other functional pipelines


# Task:
## Implement compose(*funcs) which returns a single function equivalent to
## applying the given functions right-to-left (the last function in funcs
## runs first, matching mathematical composition notation). Calling the
## returned function with one argument x should apply funcs[-1] to x, then
## funcs[-2] to that result, and so on down to funcs[0]. With zero functions
## passed, the returned function should be the identity (returns its input
## unchanged).
## Test1: Inputs: funcs = [lambda x: x + 1, lambda x: x * 2], x = 3   Outputs: 7
## Test2: Inputs: funcs = [str], x = 5   Outputs: "5"
## Test3: Inputs: funcs = [], x = 10   Outputs: 10
## Hint:
## Ugly way: a plain for loop over reversed(funcs), manually reassigning an
## accumulator variable on each iteration.
## Right way: functools.reduce - fold funcs into one callable without a
## hand-written accumulator loop.


import functools


# Solutions:

# Space - Time Complexity analysis:
## space: O(k) - the returned closure only holds a reference to funcs (length k), no copy is made
## time: O(k) - each call to the composed function walks reversed(funcs) once

def compose_ugly(funcs):
    def composed(x):  # O(1) | O(1)
        for f in reversed(funcs):  # O(1) | O(k)
            x = f(x)  # O(1) | O(1)
        return x  # O(1) | O(1)
    return composed  # O(1) | O(1)


# Space - Time Complexity analysis:
## space: O(k) - functools.reduce builds a chain of k nested closures, one per function composed
## time: O(k) - building the chain takes k reduce steps; invoking the result on one input is k nested calls

def compose(funcs):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), funcs, lambda x: x)  # O(k) | O(k)


# Tests:
def validate():
    cases = [
        ([lambda x: x + 1, lambda x: x * 2], 3, 7),
        ([str], 5, "5"),
        ([], 10, 10),
        ([lambda x: x - 1, lambda x: x - 1, lambda x: x - 1], 10, 7),
    ]
    for fn in (compose_ugly, compose):
        for funcs, x, expected in cases:
            result = fn(funcs)(x)
            assert result == expected, (
                f"{fn.__name__}({funcs!r})({x!r}): expected {expected!r}, got {result!r}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    validate()
