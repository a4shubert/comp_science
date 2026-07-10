# Theory:
## Lazy evaluation means computing values only as they're consumed, instead
## of eagerly building a full data structure up front - this matters most
## for sequences that are unbounded or expensive to fully materialize, like
## "the primes" (there's no natural stopping point) or a live data stream.
## A generator function is Python's tool for this: each `yield` pauses
## execution and hands back one value, resuming from that exact point on
## the next request, so an infinite sequence can be expressed directly
## without ever holding more than one value in memory at a time.
## itertools.islice then lets you take a fixed number of items off the
## front of that infinite generator, the lazy equivalent of slicing a list.
## The eager alternative - guessing an upper bound, generating every
## candidate up to it, and filtering - either wastes work (bound too high)
## or silently under-delivers (bound too low).


# Packages:
## itertools.islice - take a slice of an iterable without materializing the whole thing
## itertools.count - lazy infinite counter, a common generator building block
## math.isqrt - integer square root, useful for trial-division primality checks
## functools.lru_cache - memoize a pure function's results (unrelated tool, same laziness spirit)


# Task:
## Implement first_n_primes(n) which returns a list of the first n prime
## numbers (2, 3, 5, 7, 11, ...).
## Test1: Inputs: n = 5   Outputs: [2, 3, 5, 7, 11]
## Test2: Inputs: n = 1   Outputs: [2]
## Test3: Inputs: n = 10   Outputs: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
## Hint:
## Ugly way: pick a fixed candidate upper bound, generate every integer up
## to it, and filter for primality - wrong/wasteful if the guessed bound is
## too low or too high.
## Right way: an infinite generator (yield) that produces primes one at a
## time, combined with itertools.islice to take exactly n of them.


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def first_n_primes_ugly(n):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def first_n_primes(n):
    return first_n_primes_ugly(n)


# Tests:
def validate():
    cases = [
        (5, [2, 3, 5, 7, 11]),
        (1, [2]),
        (10, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]),
        (2, [2, 3]),
    ]
    for fn in (first_n_primes_ugly, first_n_primes):
        for n, expected in cases:
            result = fn(n)
            assert result == expected, (
                f"{fn.__name__}({n!r}): expected {expected!r}, got {result!r}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(first_n_primes_ugly(5))
    print(first_n_primes_ugly(1))
    print(first_n_primes_ugly(10))
    print(first_n_primes_ugly(2))
