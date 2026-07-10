# Theory:
## Real-world data almost always has gaps, and how you fill them matters:
## forward-fill (carry the last known value forward) assumes the value
## hasn't changed since the last observation - reasonable for something
## like a price that only updates on trades, wrong for something that
## should be interpolated smoothly. Implemented by hand, forward-fill
## means tracking "the last non-missing value seen" in a single loop and
## substituting it whenever the current value is missing. pandas.Series.
## ffill() (and the related bfill(), interpolate(), fillna()) do the same
## thing as a vectorized operation, and compose with the rest of pandas'
## missing-data handling (isna(), dropna()) so you rarely need to write
## the loop yourself once real data is involved.


# Packages:
## pandas.Series.ffill / pandas.DataFrame.ffill - forward-fill missing values with the last valid observation
## pandas.Series.fillna - fill missing values with a constant or a strategy
## pandas.isna / pandas.notna - vectorized missing-value detection
## numpy.nan - the standard "missing" sentinel value used throughout pandas/numpy


# Task:
## Given a list of numbers where None represents a missing value, return a
## new list with each None replaced by the most recent non-None value
## before it (forward-fill). Assume the first element is never None.
## Test1: Inputs: nums = [1, None, None, 4, None]   Outputs: [1, 1, 1, 4, 4]
## Test2: Inputs: nums = [5, 5, None]   Outputs: [5, 5, 5]
## Test3: Inputs: nums = [1, 2, 3]   Outputs: [1, 2, 3]
## Hint:
## Ugly way: manual loop - track the last seen non-None value, substitute
## it in whenever the current element is None.
## Right way: pandas.Series.ffill - build a Series, call .ffill(), convert
## back to a list.


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def forward_fill_ugly(nums):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def forward_fill(nums):
    return forward_fill_ugly(nums)


# Tests:
def validate():
    cases = [
        ([1, None, None, 4, None], [1, 1, 1, 4, 4]),
        ([5, 5, None], [5, 5, 5]),
        ([1, 2, 3], [1, 2, 3]),
    ]
    for fn in (forward_fill_ugly, forward_fill):
        for nums, expected in cases:
            result = list(fn(nums))
            assert result == expected, (
                f"{fn.__name__}({nums!r}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(list(forward_fill_ugly([1, None, None, 4, None])))
    print(list(forward_fill_ugly([5, 5, None])))
    print(list(forward_fill_ugly([1, 2, 3])))
