# Theory:
## Linear interpolation fills in a missing value between two known points
## by assuming the data changes at a constant rate between them: for a
## missing value at position x between known points (x0, y0) and (x1, y1),
## the estimate is y0 + (y1-y0) * (x-x0)/(x1-x0) - the same formula you'd
## derive by hand for a straight line through two points. Doing this
## manually for a whole series means finding the surrounding known points
## for each gap and applying the formula in a loop. scipy.interpolate.
## interp1d builds a reusable interpolating function from the known
## points once, then evaluates it at any x (or array of x's) in a
## vectorized call - useful for filling gaps in a time series or
## resampling data onto a different set of x-coordinates entirely.


# Packages:
## scipy.interpolate.interp1d - build a reusable linear (or higher-order) interpolator from known points
## numpy.interp - a simpler one-shot linear interpolation function, no separate interpolator object
## pandas.Series.interpolate - the pandas-native equivalent for filling gaps in a Series


# Task:
## Given known x-coordinates xs, their corresponding y-values ys (both
## sorted by x, no gaps), and a list of query x-coordinates queries (each
## within the range of xs), return the linearly interpolated y-value at
## each query point, rounded to 2 decimal places.
## Test1: Inputs: xs = [0, 10], ys = [0, 100], queries = [5]   Outputs: [50.0]
## Test2: Inputs: xs = [0, 1, 2], ys = [0, 10, 0], queries = [0.5, 1.5]   Outputs: [5.0, 5.0]
## Test3: Inputs: xs = [0, 4], ys = [10, 10], queries = [1, 2, 3]   Outputs: [10.0, 10.0, 10.0]
## Hint:
## Ugly way: manual formula - for each query, find the bracketing known
## points with a linear scan, then apply the two-point line formula.
## Right way: scipy.interpolate.interp1d - build the interpolator once,
## then evaluate all queries in a vectorized call.


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def interpolate_ugly(xs, ys, queries):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def interpolate(xs, ys, queries):
    return interpolate_ugly(xs, ys, queries)


# Tests:
def validate():
    cases = [
        ([0, 10], [0, 100], [5], [50.0]),
        ([0, 1, 2], [0, 10, 0], [0.5, 1.5], [5.0, 5.0]),
        ([0, 4], [10, 10], [1, 2, 3], [10.0, 10.0, 10.0]),
    ]
    for fn in (interpolate_ugly, interpolate):
        for xs, ys, queries, expected in cases:
            result = [round(v, 2) for v in fn(xs, ys, queries)]
            assert result == expected, (
                f"{fn.__name__}({xs!r}, {ys!r}, {queries!r}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(interpolate_ugly([0, 10], [0, 100], [5]))
    print(interpolate_ugly([0, 1, 2], [0, 10, 0], [0.5, 1.5]))
    print(interpolate_ugly([0, 4], [10, 10], [1, 2, 3]))
