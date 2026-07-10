# Theory:
## A greedy algorithm makes the locally-best choice at each step and never
## reconsiders it, trusting that this leads to a globally optimal answer -
## which only works when the problem has the right structure (it doesn't
## for every problem). Jump Game is a clean example where greedy provably
## works: at each index, track the furthest index reachable so far; if you
## ever reach an index beyond that furthest reach, you're stuck. There's
## no need to explore every possible sequence of jumps (which would be
## exponential) - you only need to track one number, the best reach seen
## so far, updated in a single linear pass. Recognizing when a problem
## reduces to "track one running best value" instead of "explore all
## choices" is the key skill greedy problems test.


# Packages:
## max() (builtin) - track the running furthest-reachable index
## functools.reduce - fold-based way to compute the running max in one expression


# Task:
## Given an array of non-negative integers where each element represents
## the maximum jump length from that position, determine if you can reach
## the last index starting from index 0.
## Test1: Inputs: nums = [2, 3, 1, 1, 4]   Outputs: True
## Test2: Inputs: nums = [3, 2, 1, 0, 4]   Outputs: False
## Test3: Inputs: nums = [0]   Outputs: True
## Hint:
## Ugly way: recursive/backtracking - try every possible jump length from
## each position, exploring the full tree of jump sequences.
## Right way: greedy single pass - track the furthest index reachable so
## far, fail only if you reach a position beyond it.


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def can_jump_ugly(nums):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def can_jump(nums):
    return can_jump_ugly(nums)


# Tests:
def validate():
    cases = [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([0], True),
        ([1, 0, 1], False),
    ]
    for fn in (can_jump_ugly, can_jump):
        for nums, expected in cases:
            result = fn(nums)
            assert result == expected, (
                f"{fn.__name__}({nums!r}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(can_jump_ugly([2, 3, 1, 1, 4]))
    print(can_jump_ugly([3, 2, 1, 0, 4]))
    print(can_jump_ugly([0]))
    print(can_jump_ugly([1, 0, 1]))
