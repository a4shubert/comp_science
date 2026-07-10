# Theory:
## I/O-bound work (network calls, disk reads, anything that spends most of
## its time waiting rather than computing) wastes wall-clock time when run
## sequentially, since each call blocks the whole program until it
## finishes even though the CPU is idle during the wait. Python threads are
## a good fit for this specific case despite the GIL, because the GIL is
## released while a thread is blocked on I/O - so multiple threads can be
## "waiting" concurrently, and the total wall-clock time approaches the
## slowest single call instead of the sum of all of them.
## concurrent.futures.ThreadPoolExecutor manages a pool of worker threads
## and its .map() method preserves input order in the results, so it's a
## drop-in replacement for a sequential loop wherever the work is
## independent and I/O-bound. Note this is a wall-clock/throughput win, not
## a change in asymptotic time complexity - both approaches still do n
## units of work.


# Packages:
## concurrent.futures.ThreadPoolExecutor - a pool of worker threads, .map()/.submit() to run callables concurrently
## concurrent.futures.as_completed - iterate results as they finish rather than in submission order
## time.sleep - stand-in for a blocking I/O call in a test/example
## threading.Thread - lower-level building block ThreadPoolExecutor is built on top of


# Task:
## Given a list of items, "fetch" each one (simulated by a short sleep) and
## return the fetched results in the same order as the input items.
## Test1: Inputs: items = [1, 2, 3, 4, 5]   Outputs: [2, 4, 6, 8, 10]
## Test2: Inputs: items = []   Outputs: []
## Test3: Inputs: items = [10]   Outputs: [20]
## Hint:
## Ugly way: a sequential for loop calling fetch(item) one at a time -
## correct, but wall-clock time is the sum of every call's wait.
## Right way: concurrent.futures.ThreadPoolExecutor.map - run every fetch
## concurrently, results still come back in input order.


import time


def fetch(item):
    time.sleep(0.01)
    return item * 2


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def fetch_all_ugly(items):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def fetch_all(items):
    return fetch_all_ugly(items)


# Tests:
def validate():
    cases = [
        ([1, 2, 3, 4, 5], [2, 4, 6, 8, 10]),
        ([], []),
        ([10], [20]),
    ]
    for fn in (fetch_all_ugly, fetch_all):
        for items, expected in cases:
            result = fn(items)
            assert result == expected, (
                f"{fn.__name__}({items!r}): expected {expected!r}, got {result!r}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(fetch_all_ugly([1, 2, 3, 4, 5]))
    print(fetch_all_ugly([]))
    print(fetch_all_ugly([10]))
