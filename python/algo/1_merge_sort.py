# Theory:
## Merge sort is the canonical divide-and-conquer sorting algorithm:
## split the array in half, recursively sort each half, then merge the
## two sorted halves back together in linear time. Because the array is
## halved at each level (log n levels) and merging a level's worth of
## subarrays costs O(n) total per level, the whole algorithm runs in
## O(n log n) time - guaranteed, not just on average, unlike quicksort's
## O(n^2) worst case. The tradeoff is space: the merge step needs an
## auxiliary array to combine two sorted halves without overwriting data
## still being read, costing O(n) extra space. Merge sort is also stable
## (equal elements keep their relative order), which matters when sorting
## records by one field while preserving an earlier sort on another.


# Packages:
## heapq.merge - merge multiple already-sorted iterables in O(n log k)
## sorted() / list.sort - Python's built-in Timsort, O(n log n), a hybrid merge/insertion sort
## bisect.insort - insert into a sorted list while keeping it sorted, O(n) per insertion


# Task:
## Given a list of integers, return it sorted in ascending order using
## merge sort.
## Test1: Inputs: nums = [5, 2, 4, 1, 3]   Outputs: [1, 2, 3, 4, 5]
## Test2: Inputs: nums = [3, 3, 1, 2]   Outputs: [1, 2, 3, 3]
## Test3: Inputs: nums = []   Outputs: []
## Hint:
## Ugly way: sorted() - Python's built-in sort, O(n log n), but doesn't
## demonstrate the merge-sort mechanics.
## Right way: hand-written merge sort - recursively split, then merge two
## sorted halves with a linear-time two-pointer merge.


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def merge_sort_ugly(nums):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def merge_sort(nums):
    return merge_sort_ugly(nums)


# Tests:
def validate():
    cases = [
        ([5, 2, 4, 1, 3], [1, 2, 3, 4, 5]),
        ([3, 3, 1, 2], [1, 2, 3, 3]),
        ([], []),
        ([1], [1]),
    ]
    for fn in (merge_sort_ugly, merge_sort):
        for nums, expected in cases:
            result = fn(list(nums))
            assert result == expected, (
                f"{fn.__name__}({nums!r}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(merge_sort_ugly([5, 2, 4, 1, 3]))
    print(merge_sort_ugly([3, 3, 1, 2]))
    print(merge_sort_ugly([]))
    print(merge_sort_ugly([1]))
