# Theory:
## Backtracking builds a solution incrementally, exploring one choice at a
## time, and undoes ("backtracks") a choice as soon as it can't lead to a
## valid complete solution - it's DFS over a tree of partial solutions.
## Generating all permutations is the canonical backtracking exercise:
## at each step, choose one of the remaining unused elements to place
## next, recurse, then undo that choice (mark it unused again) before
## trying the next option. There are n! permutations of n elements, and
## building each one takes O(n) (placing each of n elements), so the
## total work is O(n * n!) - this is fundamentally exponential, not a
## complexity you can improve algorithmically, since the answer itself has
## that many entries. The value of backtracking here is systematically
## covering every possibility without missing or repeating one.


# Packages:
## itertools.permutations - direct built-in permutation generator, O(n!) results
## copy.deepcopy / list slicing - snapshot a partial permutation before appending it to results
## functools.reduce - not typically used for backtracking itself, but sometimes combined with itertools output


# Task:
## Given an array of distinct integers, return all possible permutations,
## in any order.
## Test1: Inputs: nums = [1, 2, 3]   Outputs: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
## Test2: Inputs: nums = [0, 1]   Outputs: [[0,1],[1,0]]
## Test3: Inputs: nums = [1]   Outputs: [[1]]
## Hint:
## Ugly way: itertools.permutations - the built-in generator, correct but
## doesn't demonstrate the backtracking mechanics.
## Right way: hand-written backtracking - choose an unused element, recurse,
## then undo the choice before trying the next one.


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def permutations_ugly(nums):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def permutations(nums):
    return permutations_ugly(nums)


# Tests:
def validate():
    cases = [
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        ([0, 1], [[0, 1], [1, 0]]),
        ([1], [[1]]),
    ]
    for fn in (permutations_ugly, permutations):
        for nums, expected in cases:
            result = fn(nums)
            assert sorted(result) == sorted(expected), (
                f"{fn.__name__}({nums!r}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(permutations_ugly([1, 2, 3]))
    print(permutations_ugly([0, 1]))
    print(permutations_ugly([1]))
