# Theory:
## A pipeline applies a sequence of single-argument functions to a value in
## order, left to right, like a Unix shell pipe (value | f | g | h) - the
## opposite direction convention from compose, which runs right-to-left.
## Pipelines are common wherever data passes through a series of
## independent transformation steps (parsing, cleaning, formatting), and
## keeping each step as a small standalone function makes the sequence easy
## to reorder, test, or extend. Like compose, the imperative version is a
## for loop reassigning an accumulator; functools.reduce expresses the same
## thing as a single fold, using the pipeline's starting value as reduce's
## initial value and "call the next function on the accumulator" as the
## combining step.


# Packages:
## functools.reduce - fold an iterable into one value using a binary function and an initial value
## functools.partial - fix arguments ahead of time, often used to build pipeline steps
## operator module - functional operators, useful as pipeline steps
## itertools.chain - lazily concatenate iterables, useful when composing pipelines of pipelines


# Task:
## Implement pipe(value, *funcs) which applies funcs to value in order, left
## to right: the first function receives value, the second receives the
## first function's output, and so on. With zero functions, return value
## unchanged.
## Test1: Inputs: value = 3, funcs = [lambda x: x + 1, lambda x: x * 2]   Outputs: 8
## Test2: Inputs: value = "hello", funcs = [str.upper, lambda s: s[::-1]]   Outputs: "OLLEH"
## Test3: Inputs: value = 5, funcs = []   Outputs: 5
## Hint:
## Ugly way: a for loop over funcs, reassigning value on every iteration.
## Right way: functools.reduce - fold funcs over value with
## `lambda acc, f: f(acc)` as the combining function.


import functools


# Solutions:

# Space - Time Complexity analysis:
## space: O(1) - only the accumulator variable is held, no extra structure grows with input
## time: O(k) - one call per function in funcs

def pipe_ugly(value, funcs):
    for f in funcs:  # O(1) | O(k)
        value = f(value)  # O(1) | O(1)
    return value  # O(1) | O(1)


# Space - Time Complexity analysis:
## space: O(1) - functools.reduce folds to a single accumulated value, no intermediate results kept
## time: O(k) - one call per function in funcs, same as the ugly loop

def pipe(value, funcs):
    return functools.reduce(lambda acc, f: f(acc), funcs, value)  # O(k) | O(k)


# Tests:
def validate():
    cases = [
        (3, [lambda x: x + 1, lambda x: x * 2], 8),
        ("hello", [str.upper, lambda s: s[::-1]], "OLLEH"),
        (5, [], 5),
        (10, [lambda x: x - 1, lambda x: x - 1, lambda x: x - 1], 7),
    ]
    for fn in (pipe_ugly, pipe):
        for value, funcs, expected in cases:
            result = fn(value, funcs)
            assert result == expected, (
                f"{fn.__name__}({value!r}, {funcs!r}): expected {expected!r}, got {result!r}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    validate()
