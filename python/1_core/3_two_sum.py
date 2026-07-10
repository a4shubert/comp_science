# Theory:
## Hash maps (Python's dict) give average O(1) lookup, insert, and delete
## by mapping keys to array slots via a hash function, trading the
## O(log n) of a balanced tree or the O(n) of a linear scan for near-
## constant time - at the cost of no ordering guarantee and occasional
## collision overhead. The classic pattern for pair-finding problems -
## two-sum, anagram grouping, duplicate detection - is a single pass that
## checks "have I seen the complement/target already?" before inserting
## the current element, turning an O(n^2) nested-loop brute force into
## O(n) time. The tradeoff is O(n) extra space to hold the elements seen
## so far.


# Packages:
## dict - hash map, average O(1) lookup/insert/delete
## collections.Counter - frequency counting, dict subclass with default 0
## collections.defaultdict - dict with an automatic default value/factory
## itertools.combinations - generate all pairs/combinations of a sequence
## bisect - binary search insertion points, useful for sorted-array variants


# Task:
## Given a list of integers `nums` and an integer `target`, return the indices
## of the two numbers that add up to `target`. Assume exactly one valid answer
## exists, and you may not use the same element twice.
## Test1: Inputs: nums = [2, 7, 11, 15], target = 9   Outputs: [0, 1]
## Test2: Inputs: nums = [3, 2, 4], target = 6   Outputs: [1, 2]
## Test3: Inputs: nums = [3, 3], target = 6   Outputs: [0, 1]
##
## Hint: There's an O(n^2) brute-force approach (nested loop, or
## itertools.combinations(range(len(nums)), 2) to enumerate index pairs) -
## start there if you want to state the naive complexity out loud first,
## that's normal and expected in a real interview.
##
## For the O(n) approach: think about a single pass where you maintain a
## dict mapping value -> index of numbers you've already seen. Python dict
## lookup/insert is O(1) average case (hash table underneath).
## Best practice: check "have I seen (target - current) already?" BEFORE
## inserting the current number into the dict, so you don't accidentally
## pair an element with itself.


# Solutions:

from itertools import combinations


# Space - Time Complexity analysis:
## space: O(1) - combinations is a lazy generator, no pairs materialized at once
## time: O(n^2) - n choose 2 = n(n-1)/2 pairs

def two_sum_ugly(nums, target):
    # brute force: check every pair of indices
    for i, j in combinations(range(len(nums)), 2):  # O(1) | O(n^2)
        if nums[i] + nums[j] == target:  # O(1) | O(1)
            return [i, j]  # O(1) | O(1)


# Space - Time Complexity analysis:
## space: O(n) - seen dict can hold up to n-1 entries in the worst case
## time: O(n) - single pass, O(1) average dict lookup/insert

def two_sum(nums, target):
    # dict mapping each value seen so far to its index
    seen = {}  # O(1) | O(1)
    # walk through nums once, tracking value and index together
    for i, v in enumerate(nums):  # O(1) | O(n)
        # the value that would complete the pair with v
        complement = target - v  # O(1) | O(1)
        # has the complement already been seen?
        if complement in seen:  # O(1) | O(1)
            # found the pair - return both indices
            return [seen[complement], i]  # O(1) | O(1)
        # record this value's index for future lookups
        seen[v] = i  # O(n) | O(1)


# Tests:
def validate():
    cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]
    for fn in (two_sum_ugly, two_sum):
        for nums, target, expected in cases:
            result = fn(nums, target)
            assert sorted(result) == sorted(expected), (
                f"{fn.__name__}({nums!r}, {target}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    validate()
