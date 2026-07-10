# Theory:
## A running (prefix) maximum turns a list into a same-length list where
## each position holds the maximum of every element up to and including
## that position - a common building block for problems like "best time to
## sell so far" or "highest score seen so far in a stream". The naive
## approach tracks a running variable in an explicit loop, which is
## perfectly correct but is exactly the kind of accumulation pattern
## itertools.accumulate exists to express directly: it takes an iterable and
## a binary combining function (max, by default operator.add) and yields the
## running result at each step, without a hand-written loop or mutable
## accumulator variable.


# Packages:
## itertools.accumulate - running reduction over an iterable, yields each intermediate result
## functools.reduce - folds to a single final value (no intermediate results)
## builtins.max / builtins.min - pairwise or iterable-wide max/min
## operator.add, operator.mul - functional binary operators, common accumulate combiners


# Task:
## Given a list of numbers, return a list of the same length where each
## position i holds the maximum of nums[0..i] inclusive.
## Test1: Inputs: nums = [3, 1, 4, 1, 5, 9, 2, 6]   Outputs: [3, 3, 4, 4, 5, 9, 9, 9]
## Test2: Inputs: nums = [5, 4, 3, 2, 1]   Outputs: [5, 5, 5, 5, 5]
## Test3: Inputs: nums = [-1, -5, -2, 0, -3]   Outputs: [-1, -1, -1, 0, 0]
## Hint:
## Ugly way: a for loop with a running_max variable, updated and appended
## each iteration.
## Right way: itertools.accumulate - pass max as the combining function
## instead of tracking the running value by hand.


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def running_maximum_ugly(nums):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def running_maximum(nums):
    return running_maximum_ugly(nums)


# Tests:
def validate():
    cases = [
        ([3, 1, 4, 1, 5, 9, 2, 6], [3, 3, 4, 4, 5, 9, 9, 9]),
        ([5, 4, 3, 2, 1], [5, 5, 5, 5, 5]),
        ([-1, -5, -2, 0, -3], [-1, -1, -1, 0, 0]),
        ([], []),
        ([7], [7]),
    ]
    for fn in (running_maximum_ugly, running_maximum):
        for nums, expected in cases:
            result = fn(nums)
            assert result == expected, (
                f"{fn.__name__}({nums!r}): expected {expected!r}, got {result!r}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(running_maximum_ugly([3, 1, 4, 1, 5, 9, 2, 6]))
    print(running_maximum_ugly([5, 4, 3, 2, 1]))
    print(running_maximum_ugly([-1, -5, -2, 0, -3]))
    print(running_maximum_ugly([]))
    print(running_maximum_ugly([7]))
