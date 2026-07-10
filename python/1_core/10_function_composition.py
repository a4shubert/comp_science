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


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def compose_ugly(funcs):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def compose(funcs):
    return compose_ugly(funcs)


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
    # validate()
    print(compose_ugly([lambda x: x + 1, lambda x: x * 2])(3))
    print(compose_ugly([str])(5))
    print(compose_ugly([])(10))
    print(compose_ugly([lambda x: x - 1, lambda x: x - 1, lambda x: x - 1])(10))
