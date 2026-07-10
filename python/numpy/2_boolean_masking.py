# Theory:
## Boolean masking is NumPy's vectorized replacement for filtering with a
## Python loop or list comprehension. Comparing an array to a value (e.g.
## arr > 5) produces a same-shaped boolean array in one vectorized pass;
## indexing the original array with that boolean mask (arr[arr > 5])
## returns only the elements where the mask is True. Both the comparison
## and the selection happen as compiled C loops over contiguous memory,
## instead of a Python-level loop testing and appending one element at a
## time. This same mechanism underlies conditional assignment
## (arr[mask] = value) and combining conditions with & / | (not `and`/`or`,
## which don't vectorize element-wise) - it's the core tool for "give me
## the subset of data matching a condition" without writing an explicit
## loop.


# Packages:
## numpy.array comparison operators (>, <, ==, etc.) - produce boolean masks in one vectorized pass
## numpy.where - vectorized if/else, choose between two arrays element-wise based on a condition
## numpy.extract / boolean indexing (arr[mask]) - select elements where a mask is True
## numpy.logical_and / numpy.logical_or (or & / |) - combine multiple boolean masks element-wise


# Task:
## Given a list of numbers and a threshold, return a new list containing
## only the numbers strictly greater than the threshold, preserving their
## original order.
## Test1: Inputs: nums = [1, 5, 3, 8, 2, 9], threshold = 4   Outputs: [5, 8, 9]
## Test2: Inputs: nums = [1, 2, 3], threshold = 10   Outputs: []
## Test3: Inputs: nums = [], threshold = 0   Outputs: []
## Hint:
## Ugly way: list comprehension - loop through nums, testing and
## collecting each element one at a time.
## Right way: numpy boolean masking - build a boolean array via
## nums_arr > threshold, then index with it in one vectorized step.


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def filter_greater_ugly(nums, threshold):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def filter_greater(nums, threshold):
    return filter_greater_ugly(nums, threshold)


# Tests:
def validate():
    cases = [
        ([1, 5, 3, 8, 2, 9], 4, [5, 8, 9]),
        ([1, 2, 3], 10, []),
        ([], 0, []),
        ([10, 10, 10], 10, []),
    ]
    for fn in (filter_greater_ugly, filter_greater):
        for nums, threshold, expected in cases:
            result = list(fn(nums, threshold))
            assert result == expected, (
                f"{fn.__name__}({nums!r}, {threshold}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(list(filter_greater_ugly([1, 5, 3, 8, 2, 9], 4)))
    print(list(filter_greater_ugly([1, 2, 3], 10)))
    print(list(filter_greater_ugly([], 0)))
    print(list(filter_greater_ugly([10, 10, 10], 10)))
