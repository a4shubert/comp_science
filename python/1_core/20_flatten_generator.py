# Theory:
## A generator function uses yield to produce a sequence of values lazily,
## one at a time, pausing its execution state between each request instead
## of computing everything up front. `yield from` lets a generator delegate
## to another iterable (including another generator) transparently - useful
## for recursive structures like arbitrarily nested lists, where flattening
## naturally wants to recurse into sub-lists and yield whatever they
## produce. The eager alternative builds one big result list by recursively
## extending it, which is simple but means the caller can't start
## processing the first element until the *entire* structure has been
## walked and fully materialized in memory - a real cost for large or deep
## nesting where only the first few elements are actually needed.


# Packages:
## yield / yield from - define a generator, delegate to a nested iterable
## isinstance() - distinguish a list to recurse into from a plain element
## itertools.chain.from_iterable - lazily flatten one level of nesting (non-recursive)
## collections.abc.Iterable - check for "is this iterable" more generally than isinstance(x, list)


# Task:
## Given an arbitrarily nested list, produce a flat sequence of its
## non-list elements, in order.
## Test1: Inputs: nested = [1, [2, 3, [4, 5]], 6]   Outputs: [1, 2, 3, 4, 5, 6]
## Test2: Inputs: nested = [[1, 2], [3, [4, [5, 6]]]]   Outputs: [1, 2, 3, 4, 5, 6]
## Test3: Inputs: nested = []   Outputs: []
## Hint:
## Ugly way: recursive function that builds and returns one full result
## list eagerly (list.extend at every level of recursion).
## Right way: a generator function using yield from to recurse - lazy,
## O(1) space beyond the call stack itself, values available as produced.


# Solutions:

# Space - Time Complexity analysis:
## space: O(n) - the recursive call stack can go as deep as the nesting, plus the full result list holds all n leaf elements at once
## time: O(n) - every leaf element and every list boundary is visited exactly once

def flatten_ugly(nested):
    result = []  # O(1) | O(1)
    for item in nested:  # O(1) | O(k) - k elements at this level
        if isinstance(item, list):  # O(1) | O(1)
            result.extend(flatten_ugly(item))  # O(n) | O(n) - recurses into and copies the sub-result
        else:
            result.append(item)  # O(n) | O(1)
    return result  # O(1) | O(1)


# Space - Time Complexity analysis:
## space: O(d) - d is the max nesting depth (recursive generator call stack); no result list is ever fully materialized by this function itself
## time: O(n) - every leaf element and every list boundary is visited exactly once, one yield at a time

def flatten(nested):
    for item in nested:  # O(1) | O(k) - k elements at this level
        if isinstance(item, list):  # O(1) | O(1)
            yield from flatten(item)  # O(1) | O(1) - delegates lazily, no intermediate list built here
        else:
            yield item  # O(1) | O(1)


# Tests:
def validate():
    cases = [
        ([1, [2, 3, [4, 5]], 6], [1, 2, 3, 4, 5, 6]),
        ([[1, 2], [3, [4, [5, 6]]]], [1, 2, 3, 4, 5, 6]),
        ([], []),
        ([1, 2, 3], [1, 2, 3]),
    ]
    for nested, expected in cases:
        result_ugly = flatten_ugly(nested)
        assert result_ugly == expected, (
            f"flatten_ugly({nested!r}): expected {expected!r}, got {result_ugly!r}"
        )
        result = list(flatten(nested))
        assert result == expected, (
            f"list(flatten({nested!r})): expected {expected!r}, got {result!r}"
        )
    print("SUCCESS")


if __name__ == "__main__":
    validate()
