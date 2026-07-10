# Theory:
## Subsets (the power set) is another classic backtracking exercise, but
## with a different branching structure than permutations: at each
## element, you make a binary choice - include it in the current subset,
## or don't - rather than choosing among remaining unused items. This
## naturally produces 2^n subsets for n elements (each element
## independently in or out), so the total output size alone is
## exponential, same as permutations' n!. The backtracking template is
## identical in spirit though: append the current partial subset to the
## results, try including the next element and recurse, then undo that
## choice and recurse without it - covering both branches of the binary
## choice tree exhaustively.


# Packages:
## itertools.chain / itertools.combinations - build the power set as the union of all combinations(nums, r) for r in 0..n
## bitmask (plain int) - each of 2^n bitmasks directly encodes one subset membership pattern


# Task:
## Given an array of unique integers, return all possible subsets (the
## power set), in any order. The solution must not contain duplicate
## subsets.
## Test1: Inputs: nums = [1, 2, 3]   Outputs: [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
## Test2: Inputs: nums = [0]   Outputs: [[],[0]]
## Test3: Inputs: nums = []   Outputs: [[]]
## Hint:
## Ugly way: itertools.combinations - build the power set as the union of
## combinations(nums, r) for every r from 0 to len(nums).
## Right way: hand-written backtracking - for each element, recurse once
## including it and once excluding it.


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def subsets_ugly(nums):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def subsets(nums):
    return subsets_ugly(nums)


# Tests:
def validate():
    cases = [
        ([1, 2, 3], [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]),
        ([0], [[], [0]]),
        ([], [[]]),
    ]
    for fn in (subsets_ugly, subsets):
        for nums, expected in cases:
            result = fn(nums)
            normalized = sorted(sorted(s) for s in result)
            expected_normalized = sorted(sorted(s) for s in expected)
            assert normalized == expected_normalized, (
                f"{fn.__name__}({nums!r}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(subsets_ugly([1, 2, 3]))
    print(subsets_ugly([0]))
    print(subsets_ugly([]))
