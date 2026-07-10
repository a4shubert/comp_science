# Theory:
## Resampling changes a time series' frequency - e.g. turning daily data
## into weekly data by aggregating every 7 consecutive days into one
## value. Done manually, this means walking the series in fixed-size
## chunks (or bucketing by computed date ranges) and reducing each chunk
## with sum/mean/etc. - a loop with careful off-by-one bucket-boundary
## bookkeeping. pandas.DataFrame.resample (built on a DatetimeIndex) does
## the bucketing and aggregation as one vectorized operation, correctly
## handling calendar-aware boundaries (weeks, months, quarters don't have
## a fixed number of days) that a naive fixed-size chunking loop would get
## wrong. This is the standard tool for downsampling high-frequency
## financial/sensor data to a coarser reporting frequency.


# Packages:
## pandas.DataFrame.resample - regroup a time-indexed DataFrame into a new frequency, then aggregate
## pandas.date_range - generate a DatetimeIndex, useful for building test data
## pandas.Grouper - a more general grouping-by-time-frequency object, usable inside groupby too


# Task:
## Given a list of daily values (assume they start on day 0 and are
## consecutive, one value per day, in order), return a list of weekly
## sums, where each week is 7 consecutive days. If the final week is
## incomplete, sum whatever days remain.
## Test1: Inputs: daily = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]   Outputs: [28, 77]
## Test2: Inputs: daily = [1,1,1,1,1,1,1,1,1,1]   Outputs: [7, 3]
## Test3: Inputs: daily = [5]   Outputs: [5]
## Hint:
## Ugly way: manual chunking loop - walk the list 7 elements at a time,
## summing each chunk directly with careful boundary bookkeeping.
## Right way: pandas.DataFrame.resample - build a date-indexed Series,
## then resample("7D").sum() in one vectorized call.


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def weekly_sums_ugly(daily):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def weekly_sums(daily):
    return weekly_sums_ugly(daily)


# Tests:
def validate():
    cases = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [28, 77]),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [7, 3]),
        ([5], [5]),
    ]
    for fn in (weekly_sums_ugly, weekly_sums):
        for daily, expected in cases:
            result = list(fn(daily))
            assert result == expected, (
                f"{fn.__name__}({daily!r}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(list(weekly_sums_ugly([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])))
    print(list(weekly_sums_ugly([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])))
    print(list(weekly_sums_ugly([5])))
