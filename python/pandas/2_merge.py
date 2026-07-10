# Theory:
## Joining two datasets on a common key - combining each row of one table
## with the matching row(s) of another - is one of the most common data
## operations, and also one of the easiest to implement naively-but-slowly:
## a nested loop comparing every row of table A against every row of table
## B is O(n*m). The efficient approach builds a hash index on the join key
## for one side first (O(n) or O(m)), then does a single pass over the
## other side doing O(1) average lookups - O(n+m) total, the same
## "index once, probe many times" idea as a hash join in a database
## engine. pandas.merge implements exactly this (hash join, or a
## sort-merge join depending on the data), so joining two DataFrames on a
## key column is a single vectorized call rather than hand-rolled nested
## loops.


# Packages:
## pandas.merge / pandas.DataFrame.merge - join two DataFrames on a key column, hash-join under the hood
## dict - build a hash index manually for the brute-force baseline
## itertools.product - the naive nested-loop cartesian-product alternative


# Task:
## Given two lists of (key, value) tuples, left and right, return a list
## of (key, left_value, right_value) tuples for every key present in
## both, sorted by key.
## Test1: Inputs: left = [(1,"a"),(2,"b")], right = [(1,"x"),(2,"y"),(3,"z")]   Outputs: [(1,"a","x"),(2,"b","y")]
## Test2: Inputs: left = [(1,"a")], right = [(2,"b")]   Outputs: []
## Test3: Inputs: left = [], right = [(1,"x")]   Outputs: []
## Hint:
## Ugly way: nested loop - for each row in left, scan every row in right
## looking for a matching key, O(n*m).
## Right way: pandas.merge - build a DataFrame from each side and
## pd.merge(left_df, right_df, on="key"), a single hash-join call.


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def inner_join_ugly(left, right):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def inner_join(left, right):
    return inner_join_ugly(left, right)


# Tests:
def validate():
    cases = [
        ([(1, "a"), (2, "b")], [(1, "x"), (2, "y"), (3, "z")], [(1, "a", "x"), (2, "b", "y")]),
        ([(1, "a")], [(2, "b")], []),
        ([], [(1, "x")], []),
    ]
    for fn in (inner_join_ugly, inner_join):
        for left, right, expected in cases:
            result = sorted(tuple(row) for row in fn(left, right))
            assert result == expected, (
                f"{fn.__name__}({left!r}, {right!r}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(inner_join_ugly([(1, "a"), (2, "b")], [(1, "x"), (2, "y"), (3, "z")]))
    print(inner_join_ugly([(1, "a")], [(2, "b")]))
    print(inner_join_ugly([], [(1, "x")]))
