# Theory:
## Finding the k largest values doesn't require fully sorting an array -
## full sorting costs O(n log n) but gives you far more ordering
## information than needed. NumPy's argpartition rearranges an array so
## that the element at a given index is in its final sorted position, with
## everything smaller to its left and everything larger to its right
## (each side individually unordered) - this is the same partial-sort
## idea as quickselect, running in O(n) average time versus O(n log n) for
## a full sort. Asking for the top k is then just argpartition around the
## (n-k)-th position and slicing off the top k indices, which you can sort
## afterward in O(k log k) if you need them ordered - much cheaper than
## sorting all n elements when k is small.


# Packages:
## numpy.argpartition - partial sort, O(n) average, puts the k largest/smallest in place without ordering them
## numpy.argsort - full sort, O(n log n), returns sorted indices
## numpy.partition - like argpartition but returns values instead of indices
## heapq.nlargest - the pure-Python heap-based equivalent for finding top-k


# Task:
## Given a list of numbers and an integer k, return the k largest values,
## sorted in descending order.
## Test1: Inputs: nums = [3, 1, 4, 1, 5, 9, 2, 6], k = 3   Outputs: [9, 6, 5]
## Test2: Inputs: nums = [1, 2, 3], k = 1   Outputs: [3]
## Test3: Inputs: nums = [5], k = 1   Outputs: [5]
## Hint:
## Ugly way: sorted() - fully sort the whole list, then slice the last k
## elements, O(n log n) even though only k results are needed.
## Right way: numpy.argpartition - partition around the top-k boundary in
## O(n) average, then sort just those k values.


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def top_k_ugly(nums, k):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def top_k(nums, k):
    return top_k_ugly(nums, k)


# Tests:
def validate():
    cases = [
        ([3, 1, 4, 1, 5, 9, 2, 6], 3, [9, 6, 5]),
        ([1, 2, 3], 1, [3]),
        ([5], 1, [5]),
    ]
    for fn in (top_k_ugly, top_k):
        for nums, k, expected in cases:
            result = list(fn(nums, k))
            assert result == expected, (
                f"{fn.__name__}({nums!r}, {k}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(list(top_k_ugly([3, 1, 4, 1, 5, 9, 2, 6], 3)))
    print(list(top_k_ugly([1, 2, 3], 1)))
    print(list(top_k_ugly([5], 1)))
