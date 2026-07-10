# Theory:
## A heap is a tree-shaped structure that keeps the minimum (or maximum)
## element accessible in O(1), with O(log n) insert and removal - Python's
## heapq module implements a min-heap directly atop a plain list. For
## "kth largest/smallest" or "top-k" problems, you don't need to sort
## everything: maintain a heap of only k elements, pushing new candidates
## and popping the smallest whenever the heap exceeds size k, so the root
## always holds the answer once the pass finishes - O(n log k) time instead
## of the O(n log n) a full sort would cost, and O(k) space instead of
## O(n). This pattern generalizes to any streaming "keep the best k seen
## so far" problem, not just a single final answer.


# Packages:
## heapq.heappush / heapq.heappop - core min-heap operations, O(log n) each
## heapq.heapify - turn an existing list into a heap in O(n)
## heapq.nlargest / heapq.nsmallest - direct top-k helpers without manual heap management
## sorted() - the brute-force baseline, O(n log n)


# Task:
## Given an integer array nums and an integer k, return the k-th largest
## element in the array. (k=1 means the largest element.) Duplicates count
## by position, not by distinct value - e.g. [3,3,4] with k=2 is 3.
## Test1: Inputs: nums = [3, 2, 1, 5, 6, 4], k = 2   Outputs: 5
## Test2: Inputs: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4   Outputs: 4
## Test3: Inputs: nums = [1], k = 1   Outputs: 1
## Hint:
## Ugly way: sorted() - sort the whole array, then index into it.
## Right way: heapq - maintain a size-k min-heap without sorting everything.


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

from heapq import h
def kth_largest_ugly(nums, k):
    
    for i,v in enumerate(nums):
        
        


# Space - Time Complexity analysis:
## space:
## time:

def kth_largest(nums, k):
    return kth_largest_ugly(nums, k)


# Tests:
def validate():
    cases = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
        ([2, 1], 2, 1),
    ]
    for fn in (kth_largest_ugly, kth_largest):
        for nums, k, expected in cases:
            result = fn(nums, k)
            assert result == expected, (
                f"{fn.__name__}({nums!r}, {k}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(kth_largest_ugly([3, 2, 1, 5, 6, 4], 2))
