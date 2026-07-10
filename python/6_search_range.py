# Theory:
## Binary search finds a target in a sorted sequence in O(log n) by
## repeatedly halving the search space: compare the middle element, then
## recurse into whichever half could still contain the target. Python's
## bisect module (bisect_left, bisect_right) implements this without you
## writing the low/high/mid loop by hand, returning insertion points rather
## than a boolean match - bisect_left finds the first valid position,
## bisect_right the position after any equal run. This makes it easy to
## answer "first/last occurrence" or "how many elements are less than x"
## questions on sorted data directly, without any extra pass over the
## array.


# Packages:
## bisect.bisect_left / bisect.bisect_right - find insertion boundaries in O(log n)
## bisect.insort - insert into a sorted list while keeping it sorted
## sorted() - general-purpose sort, O(n log n)
## functools.cmp_to_key - build a sort key from an old-style comparator function


# Task:
## Given a sorted array of integers nums and a target value, return the
## [start, end] indices of the range where target appears. If target isn't
## in nums, return [-1, -1]. Assume nums is sorted in ascending order (may
## contain duplicates).
## Test1: Inputs: nums = [5, 7, 7, 8, 8, 10], target = 8   Outputs: [3, 4]
## Test2: Inputs: nums = [5, 7, 7, 8, 8, 10], target = 6   Outputs: [-1, -1]
## Test3: Inputs: nums = [], target = 0   Outputs: [-1, -1]
## Hint:
## Ugly way: linear scan - walk the array and track the first/last index
## where you see target.
## Right way: bisect (bisect_left, bisect_right) - each finds a boundary
## in O(log n) without you writing the binary search by hand.


# Solutions:

from bisect import bisect_left, bisect_right


# Space - Time Complexity analysis:
## space: O(1) - only a couple of index variables are kept regardless of n
## time: O(n) - single linear pass

def search_range_ugly(nums, target):
    first, last = -1, -1  # O(1) | O(1)
    for i, v in enumerate(nums):  # O(1) | O(n)
        if v == target:  # O(1) | O(1)
            if first == -1:  # O(1) | O(1)
                first = i  # O(1) | O(1)
            last = i  # O(1) | O(1)
    return [first, last]  # O(1) | O(1)


# Space - Time Complexity analysis:
## space: O(1) - bisect uses no extra structures beyond a few index variables
## time: O(log n) - two binary searches via bisect

def search_range(nums, target):
    left = bisect_left(nums, target)  # O(1) | O(log n)
    if left == len(nums) or nums[left] != target:  # O(1) | O(1)
        return [-1, -1]
    right = bisect_right(nums, target) - 1  # O(1) | O(log n)
    return [left, right]  # O(1) | O(1)


# Tests:
def validate():
    cases = [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
        ([1], 1, [0, 0]),
        ([2, 2, 2, 2], 2, [0, 3]),
        ([5, 7, 7, 8, 8, 10], 5, [0, 0]),
        ([5, 7, 7, 8, 8, 10], 10, [5, 5]),
    ]
    for fn in (search_range_ugly, search_range):
        for nums, target, expected in cases:
            result = fn(nums, target)
            assert result == expected, (
                f"{fn.__name__}({nums!r}, {target}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    validate()
