# Theory:
## Run-length encoding compresses a sequence by replacing runs of
## consecutive equal elements with a single (value, count) pair - useful
## whenever data has long stretches of repetition (simple image
## compression, encoding sparse categorical data). The core operation is
## grouping *consecutive* equal elements, which is different from grouping
## all equal elements regardless of position (that's what a dict/Counter
## does). itertools.groupby does exactly the consecutive-run version: it
## walks the iterable once and yields (key, group) pairs each time the key
## changes, which is precisely the "count of the current run" operation
## this task needs, without a hand-written index-tracking loop.


# Packages:
## itertools.groupby - group consecutive elements sharing a key, single pass
## collections.Counter - counts ALL occurrences regardless of position (a common confusion with groupby)
## itertools.chain - flatten an iterable of iterables, sometimes paired with groupby
## sum() with a generator - common way to count the size of each groupby group


# Task:
## Given a sequence, return a list of (value, count) pairs for each run of
## consecutive equal elements, in order.
## Test1: Inputs: seq = "aaabbbccd"   Outputs: [("a", 3), ("b", 3), ("c", 2), ("d", 1)]
## Test2: Inputs: seq = [1, 1, 2, 2, 2, 3]   Outputs: [(1, 2), (2, 3), (3, 1)]
## Test3: Inputs: seq = ""   Outputs: []
## Hint:
## Ugly way: a for loop tracking the previous element and a running counter
## by hand, flushing a (value, count) pair whenever the element changes.
## Right way: itertools.groupby - group consecutive equal elements
## directly, count each group's size.


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def run_length_encode_ugly(seq):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def run_length_encode(seq):
    return run_length_encode_ugly(seq)


# Tests:
def validate():
    cases = [
        ("aaabbbccd", [("a", 3), ("b", 3), ("c", 2), ("d", 1)]),
        ([1, 1, 2, 2, 2, 3], [(1, 2), (2, 3), (3, 1)]),
        ("", []),
        ("aaaa", [("a", 4)]),
        ("abcd", [("a", 1), ("b", 1), ("c", 1), ("d", 1)]),
    ]
    for fn in (run_length_encode_ugly, run_length_encode):
        for seq, expected in cases:
            result = fn(seq)
            assert result == expected, (
                f"{fn.__name__}({seq!r}): expected {expected!r}, got {result!r}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(run_length_encode_ugly("aaabbbccd"))
    print(run_length_encode_ugly([1, 1, 2, 2, 2, 3]))
    print(run_length_encode_ugly(""))
    print(run_length_encode_ugly("aaaa"))
    print(run_length_encode_ugly("abcd"))
