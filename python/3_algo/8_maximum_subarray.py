# Theory:
## Kadane's algorithm finds the maximum-sum contiguous subarray in O(n)
## time by making a simple local decision at each position: either extend
## the current subarray by including this element, or start a new
## subarray here - whichever gives a larger running sum. The insight is
## that a negative running sum can never help a future subarray, so as
## soon as the running total drops below zero (or below just the current
## element), it's better to restart from the current element than to drag
## the negative baggage forward. This is a form of dynamic programming
## where the "state" is compressed to a single running value (best sum
## ending exactly at the current index) rather than a full table, since
## each step only depends on the immediately preceding one.


# Packages:
## itertools.accumulate - running prefix sums, useful for the brute-force O(n^2) approach
## math.inf - initial "negative infinity" baseline for tracking a running maximum


# Task:
## Given an integer array, find the contiguous subarray (containing at
## least one number) with the largest sum, and return that sum.
## Test1: Inputs: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]   Outputs: 6
## Test2: Inputs: nums = [1]   Outputs: 1
## Test3: Inputs: nums = [5, 4, -1, 7, 8]   Outputs: 23
## Hint:
## Ugly way: nested loop over every (i, j) pair - sum each subarray from
## scratch, O(n^2) or O(n^3) depending on how the sum is computed.
## Right way: Kadane's algorithm - a single pass, extending or restarting
## the running sum at each element, O(n).


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def max_subarray_ugly(nums):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def max_subarray(nums):
    return max_subarray_ugly(nums)


# Tests:
def validate():
    cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
        ([-1], -1),
    ]
    for fn in (max_subarray_ugly, max_subarray):
        for nums, expected in cases:
            result = fn(nums)
            assert result == expected, (
                f"{fn.__name__}({nums!r}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(max_subarray_ugly([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(max_subarray_ugly([1]))
    print(max_subarray_ugly([5, 4, -1, 7, 8]))
    print(max_subarray_ugly([-1]))
