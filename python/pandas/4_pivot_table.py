# Theory:
## A pivot table reshapes "long" data (one row per observation, with
## columns identifying what's being measured) into "wide" data (one row
## per category, one column per sub-category, cells holding an aggregated
## value) - the same reshape spreadsheets do with PivotTables. Done by
## hand, it's a nested dict: outer key is the row category, inner key is
## the column category, value is the running aggregate, built up by
## iterating every record once and updating the right (row, col) bucket.
## pandas.pivot_table generalizes this: it groups by the row and column
## keys simultaneously and applies an aggregation function (default mean,
## but sum/count/etc. all work), producing the reshaped DataFrame directly
## without manually managing the nested bucket structure.


# Packages:
## pandas.pivot_table - reshape long data into a row x column summary table with an aggregation function
## pandas.DataFrame.pivot - similar reshape, but requires unique (row, col) pairs (no aggregation)
## collections.defaultdict - nested dict as the manual pivot-table equivalent


# Task:
## Given a list of (row_key, col_key, value) tuples, return a dict of
## dicts pivot[row_key][col_key] = sum of all values with that
## (row_key, col_key) pair.
## Test1: Inputs: rows = [("a","x",1),("a","y",2),("b","x",3),("a","x",4)]   Outputs: {"a": {"x": 5, "y": 2}, "b": {"x": 3}}
## Test2: Inputs: rows = [("p","q",10)]   Outputs: {"p": {"q": 10}}
## Test3: Inputs: rows = []   Outputs: {}
## Hint:
## Ugly way: nested dict with manual accumulation - loop through rows,
## adding each value into dict[row_key][col_key], creating buckets as needed.
## Right way: pandas.pivot_table - build a DataFrame, then
## pivot_table(index="row", columns="col", values="value", aggfunc="sum").


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def pivot_sum_ugly(rows):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def pivot_sum(rows):
    return pivot_sum_ugly(rows)


# Tests:
def validate():
    cases = [
        ([("a", "x", 1), ("a", "y", 2), ("b", "x", 3), ("a", "x", 4)],
         {"a": {"x": 5, "y": 2}, "b": {"x": 3}}),
        ([("p", "q", 10)], {"p": {"q": 10}}),
        ([], {}),
    ]
    for fn in (pivot_sum_ugly, pivot_sum):
        for rows, expected in cases:
            result = {r: dict(c) for r, c in dict(fn(rows)).items()}
            assert result == expected, (
                f"{fn.__name__}({rows!r}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(pivot_sum_ugly([("a", "x", 1), ("a", "y", 2), ("b", "x", 3), ("a", "x", 4)]))
    print(pivot_sum_ugly([("p", "q", 10)]))
    print(pivot_sum_ugly([]))
