# Theory:
## GroupBy implements the "split-apply-combine" pattern: split the data
## into groups by some key, apply a function (sum, mean, count, ...) to
## each group independently, then combine the results back into a single
## structure. Doing this manually means building a dict keyed by group,
## appending each row's value to the right bucket in a loop, then a second
## pass to reduce each bucket - straightforward but entirely Python-level.
## pandas.DataFrame.groupby does the same conceptual thing, but the
## grouping and aggregation both run as vectorized operations over NumPy
## arrays underneath, and it composes cleanly with any aggregation
## function (or several at once via .agg()) without writing new looping
## code each time - the pattern generalizes instead of being rewritten
## per aggregation.


# Packages:
## pandas.DataFrame.groupby - split-apply-combine, the core grouping operation
## pandas.core.groupby.GroupBy.agg - apply one or more aggregation functions to each group
## collections.defaultdict(list) - the manual, dict-based equivalent of grouping
## statistics.mean - compute an average by hand for the brute-force baseline


# Task:
## Given a list of (category, value) tuples, return a dict mapping each
## category to the average value for that category, rounded to 2 decimal
## places.
## Test1: Inputs: rows = [("a",10),("b",20),("a",30),("b",40)]   Outputs: {"a": 20.0, "b": 30.0}
## Test2: Inputs: rows = [("x",1),("x",2),("x",3)]   Outputs: {"x": 2.0}
## Test3: Inputs: rows = []   Outputs: {}
## Hint:
## Ugly way: dict of lists - loop through rows, append each value to a
## dict bucket keyed by category, then average each bucket manually.
## Right way: pandas.DataFrame.groupby - build a DataFrame, then
## groupby("category")["value"].mean() in one vectorized call.


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def average_by_category_ugly(rows):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def average_by_category(rows):
    return average_by_category_ugly(rows)


# Tests:
def validate():
    cases = [
        ([("a", 10), ("b", 20), ("a", 30), ("b", 40)], {"a": 20.0, "b": 30.0}),
        ([("x", 1), ("x", 2), ("x", 3)], {"x": 2.0}),
        ([], {}),
    ]
    for fn in (average_by_category_ugly, average_by_category):
        for rows, expected in cases:
            result = {k: round(v, 2) for k, v in dict(fn(rows)).items()}
            assert result == expected, (
                f"{fn.__name__}({rows!r}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(dict(average_by_category_ugly([("a", 10), ("b", 20), ("a", 30), ("b", 40)])))
    print(dict(average_by_category_ugly([("x", 1), ("x", 2), ("x", 3)])))
    print(dict(average_by_category_ugly([])))
