# Theory:
## XOR (^) has two properties that make it a powerful bit-manipulation
## tool: x ^ x == 0 (anything XORed with itself cancels to zero), and
## x ^ 0 == x (XOR with zero is a no-op), and it's both commutative and
## associative, so the order of operations doesn't matter. XOR every
## element of an array together, and every value that appears an even
## number of times cancels itself out completely, leaving only whatever
## appears an odd number of times. This solves "find the single element
## that doesn't appear twice" in O(n) time and O(1) space - no hash set
## needed to track what's been seen, which is normally the O(n) space
## you'd reach for first. Bit tricks like this show up whenever a problem
## has an "everything pairs up except one thing" structure.


# Packages:
## functools.reduce - fold XOR across the whole array in one expression
## operator.xor_ - the XOR operator as a plain function, handy with reduce
## collections.Counter - frequency counting, the straightforward O(n) space alternative


# Task:
## Given a non-empty array of integers where every element appears twice
## except for one, find that single element. Your solution should ideally
## use O(1) extra space.
## Test1: Inputs: nums = [2, 2, 1]   Outputs: 1
## Test2: Inputs: nums = [4, 1, 2, 1, 2]   Outputs: 4
## Test3: Inputs: nums = [1]   Outputs: 1
## Hint:
## Ugly way: collections.Counter - count occurrences of every value, then
## return the one with count 1; O(n) space.
## Right way: XOR fold - XOR every element together; pairs cancel to zero,
## leaving only the single element; O(1) space.


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def single_number_ugly(nums):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def single_number(nums):
    return single_number_ugly(nums)


# Tests:
def validate():
    cases = [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
        ([-1, -1, -2], -2),
    ]
    for fn in (single_number_ugly, single_number):
        for nums, expected in cases:
            result = fn(nums)
            assert result == expected, (
                f"{fn.__name__}({nums!r}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(single_number_ugly([2, 2, 1]))
    print(single_number_ugly([4, 1, 2, 1, 2]))
    print(single_number_ugly([1]))
    print(single_number_ugly([-1, -1, -2]))
