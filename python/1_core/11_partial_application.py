# Theory:
## Partial application means fixing some of a function's arguments ahead of
## time to produce a new, more specific function with fewer parameters left
## to fill in - e.g. turning a general power(base, exp) into a specific
## square(base) by fixing exp=2. It's distinct from currying (which
## transforms a function into a chain of single-argument functions) but
## solves a similar problem: reusing one general-purpose function to build a
## family of specialized ones without duplicating logic. Hand-rolling this
## with a closure works, but functools.partial does it directly, produces an
## object that behaves like a function, and is the idiomatic way to signal
## "this is the same function with some inputs pinned" rather than a
## bespoke wrapper.


# Packages:
## functools.partial - fix leading positional (or keyword) arguments of a callable
## functools.partialmethod - the same idea, for methods defined on a class
## functools.reduce - fold an iterable into one value/callable
## operator module - functional operators, commonly combined with partial


# Task:
## Implement specialize(fn, *fixed_args) which fixes the leading positional
## arguments of fn to fixed_args and returns a new callable that accepts the
## remaining arguments and forwards everything to fn.
## Test1: Inputs: fn = lambda base, exp: base ** exp, fixed_args = (2,), then call the result with (10,)   Outputs: 1024
## Test2: Inputs: fn = lambda a, b, c: a + b + c, fixed_args = (1, 2), then call the result with (3,)   Outputs: 6
## Test3: Inputs: fn = lambda x: x * 3, fixed_args = (), then call the result with (4,)   Outputs: 12
## Hint:
## Ugly way: a hand-written closure that captures fixed_args and calls
## fn(*fixed_args, *rest) when invoked.
## Right way: functools.partial - build the specialized callable directly
## instead of writing the closure by hand.


import functools


# Solutions:

# Space - Time Complexity analysis:
## space: O(k) - the closure captures fixed_args (k items) and a reference to fn
## time: O(1) to build; each call is O(k+m) to merge k fixed args with m call-time args before invoking fn

def specialize_ugly(fn, fixed_args):
    def specialized(*args):  # O(1) | O(1)
        return fn(*fixed_args, *args)  # O(k+m) | O(k+m)
    return specialized  # O(1) | O(1)


# Space - Time Complexity analysis:
## space: O(k) - functools.partial stores fixed_args (k items) and a reference to fn internally
## time: O(1) to build; each call is O(k+m) for functools.partial to merge fixed and call-time args

def specialize(fn, fixed_args):
    return functools.partial(fn, *fixed_args)  # O(k) | O(k)


# Tests:
def validate():
    cases = [
        (lambda base, exp: base ** exp, (2,), (10,), 1024),
        (lambda a, b, c: a + b + c, (1, 2), (3,), 6),
        (lambda x: x * 3, (), (4,), 12),
    ]
    for fn in (specialize_ugly, specialize):
        for target, fixed_args, call_args, expected in cases:
            result = fn(target, fixed_args)(*call_args)
            assert result == expected, (
                f"{fn.__name__}(..., {fixed_args!r})({call_args!r}): "
                f"expected {expected!r}, got {result!r}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    validate()
