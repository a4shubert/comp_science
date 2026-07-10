# Theory:
## Quicksort is the other classic divide-and-conquer sort: pick a pivot,
## partition the array so everything smaller than the pivot ends up to
## its left and everything larger to its right, then recursively sort
## each side. Unlike merge sort, partitioning can be done in place, so
## quicksort typically needs only O(log n) extra space (the recursion
## stack) rather than O(n) - but its worst-case time is O(n^2), which
## happens when the pivot choice repeatedly splits the array as unevenly
## as possible (e.g. always picking the first element on an
## already-sorted array). Randomizing the pivot choice (or using
## median-of-three) makes that worst case astronomically unlikely in
## practice, which is why quicksort - despite the theoretically worse
## bound - is often faster in practice than merge sort due to better cache
## locality and lower constant factors.


# Packages:
## random.randint / random.choice - randomize pivot selection to avoid worst-case O(n^2) on adversarial input
## sorted() / list.sort - Python's built-in Timsort, for comparison
## statistics.median - useful for a median-of-three pivot strategy


# Task:
## Given a list of integers, return it sorted in ascending order using
## quicksort.
## Test1: Inputs: nums = [5, 2, 4, 1, 3]   Outputs: [1, 2, 3, 4, 5]
## Test2: Inputs: nums = [3, 3, 1, 2]   Outputs: [1, 2, 3, 3]
## Test3: Inputs: nums = []   Outputs: []
## Hint:
## Ugly way: sorted() - Python's built-in sort, O(n log n), but doesn't
## demonstrate the partition mechanics.
## Right way: hand-written quicksort - pick a pivot, partition in place
## around it, recurse on each side.


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def quick_sort_ugly(nums):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def quick_sort(nums):
    return quick_sort_ugly(nums)


# Tests:
def validate():
    cases = [
        ([5, 2, 4, 1, 3], [1, 2, 3, 4, 5]),
        ([3, 3, 1, 2], [1, 2, 3, 3]),
        ([], []),
        ([1], [1]),
    ]
    for fn in (quick_sort_ugly, quick_sort):
        for nums, expected in cases:
            result = fn(list(nums))
            assert result == expected, (
                f"{fn.__name__}({nums!r}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(quick_sort_ugly([5, 2, 4, 1, 3]))
    print(quick_sort_ugly([3, 3, 1, 2]))
    print(quick_sort_ugly([]))
    print(quick_sort_ugly([1]))
