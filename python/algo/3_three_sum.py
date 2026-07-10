# Theory:
## The two-pointer technique extends naturally from two-sum to three-sum:
## sort the array first (O(n log n)), then fix one element and use two
## pointers (from the two ends of the remaining subarray) to find pairs
## that sum to the target, moving inward based on whether the current sum
## is too high or too low - since the subarray is sorted, moving a
## pointer strictly increases or decreases the sum, so you never need to
## backtrack. This turns an O(n^3) brute-force triple-nested loop into
## O(n^2): O(n) choices for the fixed element, times O(n) for the
## two-pointer scan. The same pattern generalizes to k-sum problems by
## fixing k-2 elements and two-pointering the rest.


# Packages:
## sorted() / list.sort - sorting is the prerequisite that makes two-pointer scanning valid
## itertools.combinations - brute-force baseline, enumerate all triples directly
## set - deduplicate triples if the problem requires unique answers only


# Task:
## Given an array of integers, return all unique triplets [a, b, c] such
## that a + b + c == 0. The solution set must not contain duplicate
## triplets.
## Test1: Inputs: nums = [-1, 0, 1, 2, -1, -4]   Outputs: [[-1, -1, 2], [-1, 0, 1]]
## Test2: Inputs: nums = [0, 1, 1]   Outputs: []
## Test3: Inputs: nums = [0, 0, 0]   Outputs: [[0, 0, 0]]
## Hint:
## Ugly way: itertools.combinations - enumerate every triple directly and
## keep the ones that sum to zero, O(n^3).
## Right way: sort + two pointers - fix one element, then two-pointer scan
## the rest, O(n^2) overall.


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def three_sum_ugly(nums):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def three_sum(nums):
    return three_sum_ugly(nums)


# Tests:
def validate():
    cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([], []),
    ]
    for fn in (three_sum_ugly, three_sum):
        for nums, expected in cases:
            result = fn(nums)
            normalized = sorted(sorted(triplet) for triplet in result)
            expected_normalized = sorted(sorted(triplet) for triplet in expected)
            assert normalized == expected_normalized, (
                f"{fn.__name__}({nums!r}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(three_sum_ugly([-1, 0, 1, 2, -1, -4]))
    print(three_sum_ugly([0, 1, 1]))
    print(three_sum_ugly([0, 0, 0]))
    print(three_sum_ugly([]))
