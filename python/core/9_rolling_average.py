# Theory:
## NumPy's core advantage over plain Python loops is vectorization:
## operations like sums, means, and elementwise arithmetic run as compiled
## C loops over contiguous memory, avoiding Python's per-iteration
## interpreter overhead - often 10-100x faster for numeric workloads. A
## naive rolling-window computation (like a moving average) recomputes the
## sum of each window from scratch, costing O(n*w) time for n elements and
## window size w. The vectorized fix uses a prefix-sum (cumulative sum)
## trick: precompute cumulative sums once in O(n), then each window's sum
## is just a difference of two prefix-sum entries, dropping the total cost
## to O(n) regardless of window size - the same algorithmic idea NumPy's
## cumsum-based tricks (and pandas' .rolling()) exploit under the hood.


# Packages:
## numpy.cumsum - cumulative sum, the basis of an O(n) rolling-window trick
## numpy.convolve - sliding-window sum/correlation in one vectorized call
## pandas.Series.rolling - built-in rolling-window aggregations (mean, sum, std, ...)
## numpy.mean / numpy.array - vectorized elementwise operations over arrays


# Task:
## Given a list of numbers prices and a window size w, return the simple
## moving average over each full window of size w - a list of length
## len(prices) - w + 1. Assume 1 <= w <= len(prices).
## Test1: Inputs: prices = [1, 2, 3, 4, 5], w = 2   Outputs: [1.5, 2.5, 3.5, 4.5]
## Test2: Inputs: prices = [1, 2, 3, 4, 5], w = 3   Outputs: [2.0, 3.0, 4.0]
## Test3: Inputs: prices = [5, 5, 5, 5], w = 2   Outputs: [5.0, 5.0, 5.0]
## Hint:
## Ugly way: nested loop - sum each window of w elements from scratch.
## Right way: prefix sums (or numpy.cumsum) - precompute cumulative sums
## once, then each window's sum is a single subtraction.


# Solutions:
import numpy as np


# Space - Time Complexity analysis:
## space: O(n) - result list holds n-w+1 averages
## time: O(n*w) - n windows, each summed from scratch in O(w) via slicing

def rolling_average_ugly(prices, w):
    result = []  # O(1) | O(1)
    for i in range(len(prices) - w + 1):  # O(1) | O(n)
        window_sum = sum(prices[i:i + w])  # O(w) | O(w)
        result.append(window_sum / w)  # O(n) | O(1)
    return result  # O(1) | O(1)


# Space - Time Complexity analysis:
## space: O(n) - the numpy array, prefix-sum array, and result all scale with n
## time: O(n) - np.cumsum is a single vectorized pass; the window-sum subtraction is vectorized over all windows at once

def rolling_average(prices, w):
    # numpy array so cumsum runs as a vectorized C loop, not a Python loop
    arr = np.array(prices, dtype=float)  # O(n) | O(n)
    # prefix[i] = sum of the first i prices; a leading 0 makes prefix[0] = 0
    prefix = np.cumsum(np.insert(arr, 0, 0))  # O(n) | O(n)
    # every window's sum at once: prefix[w:] - prefix[:-w], no explicit loop over windows
    window_sums = prefix[w:] - prefix[:-w]  # O(n) | O(n)
    return (window_sums / w).tolist()  # O(n) | O(n)


# Tests:
def validate():
    cases = [
        ([1, 2, 3, 4, 5], 2, [1.5, 2.5, 3.5, 4.5]),
        ([1, 2, 3, 4, 5], 3, [2.0, 3.0, 4.0]),
        ([5, 5, 5, 5], 2, [5.0, 5.0, 5.0]),
        ([2, 4, 6], 3, [4.0]),
    ]
    for fn in (rolling_average_ugly, rolling_average):
        for prices, w, expected in cases:
            result = fn(prices, w)
            assert result == expected, (
                f"{fn.__name__}({prices!r}, {w}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    validate()
