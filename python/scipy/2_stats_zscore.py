# Theory:
## A z-score measures how many standard deviations a value is from a
## dataset's mean: z = (x - mean) / std. Computing it by hand means first
## looping through the data to sum values (for the mean), then looping
## again to sum squared deviations (for the standard deviation), then a
## final pass to compute each z-score - three explicit passes, each an
## O(n) Python loop. scipy.stats (and numpy) provide these as vectorized
## one-liners: numpy.mean, numpy.std, and scipy.stats.zscore compute the
## whole thing in compiled, vectorized passes. Z-scores are the basis of
## outlier detection (flag anything beyond +/-3 std), standardization
## before feeding data into many ML models, and comparing values measured
## on different scales.


# Packages:
## scipy.stats.zscore - compute z-scores for an entire array in one vectorized call
## numpy.mean / numpy.std - the two building blocks a z-score is made from
## scipy.stats.norm - the normal distribution object, for related pdf/cdf/percentile calculations


# Task:
## Given a list of numbers, return a list of their z-scores (using the
## population standard deviation, ddof=0), each rounded to 2 decimal
## places.
## Test1: Inputs: nums = [2, 4, 4, 4, 5, 5, 7, 9]   Outputs: [-1.5, -0.5, -0.5, -0.5, 0.0, 0.0, 1.0, 2.0]
## Test2: Inputs: nums = [5, 10, 15]   Outputs: [-1.22, 0.0, 1.22]
## Test3: Inputs: nums = [1, 2]   Outputs: [-1.0, 1.0]
## Hint:
## Ugly way: manual formula - loop once to compute the mean, loop again
## for the standard deviation, loop a third time to compute each z-score.
## Right way: scipy.stats.zscore - one vectorized call over the whole
## array.


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def zscores_ugly(nums):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def zscores(nums):
    return zscores_ugly(nums)


# Tests:
def validate():
    cases = [
        ([2, 4, 4, 4, 5, 5, 7, 9], [-1.5, -0.5, -0.5, -0.5, 0.0, 0.0, 1.0, 2.0]),
        ([5, 10, 15], [-1.22, 0.0, 1.22]),
        ([1, 2], [-1.0, 1.0]),
    ]
    for fn in (zscores_ugly, zscores):
        for nums, expected in cases:
            result = [round(z, 2) for z in fn(nums)]
            assert result == expected, (
                f"{fn.__name__}({nums!r}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print([round(z, 2) for z in zscores_ugly([2, 4, 4, 4, 5, 5, 7, 9])])
    print([round(z, 2) for z in zscores_ugly([5, 10, 15])])
    print([round(z, 2) for z in zscores_ugly([1, 2])])
