# Theory:
## Reduction operations (sum, mean, max, ...) collapse an array along one
## or more dimensions. NumPy's axis parameter controls which dimension
## gets collapsed: for a 2D array, axis=0 reduces down the rows (giving a
## per-column result), and axis=1 reduces across the columns (giving a
## per-row result) - it's easy to mix these up, so a good mental model is
## "axis=k means the result loses dimension k." Doing this manually means
## nested loops (outer over rows, inner over columns, or vice versa)
## re-summing each row/column from scratch; NumPy's axis-aware reductions
## do the same work as a single vectorized C-level pass over contiguous
## memory, and generalize cleanly to arrays with more than two dimensions
## where manual nested loops get unwieldy fast.


# Packages:
## numpy.sum(axis=...) / numpy.mean(axis=...) - axis-aware reductions, collapse one dimension
## numpy.max(axis=...) / numpy.min(axis=...) - same idea for max/min instead of sum/mean
## numpy.array - construct the 2D array being reduced


# Task:
## Given a matrix (list of lists) of numbers, return a tuple (row_sums,
## col_sums): row_sums is a list with the sum of each row, col_sums is a
## list with the sum of each column.
## Test1: Inputs: matrix = [[1,2,3],[4,5,6]]   Outputs: ([6, 15], [5, 7, 9])
## Test2: Inputs: matrix = [[1]]   Outputs: ([1], [1])
## Test3: Inputs: matrix = [[1,1],[1,1],[1,1]]   Outputs: ([2, 2, 2], [3, 3])
## Hint:
## Ugly way: nested loops - one pass summing each row manually, another
## pass summing each column manually.
## Right way: numpy.sum(axis=1) for row sums, numpy.sum(axis=0) for column
## sums - each a single vectorized reduction.


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def row_col_sums_ugly(matrix):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def row_col_sums(matrix):
    return row_col_sums_ugly(matrix)


# Tests:
def validate():
    cases = [
        ([[1, 2, 3], [4, 5, 6]], ([6, 15], [5, 7, 9])),
        ([[1]], ([1], [1])),
        ([[1, 1], [1, 1], [1, 1]], ([2, 2, 2], [3, 3])),
    ]
    for fn in (row_col_sums_ugly, row_col_sums):
        for matrix, expected in cases:
            row_sums, col_sums = fn(matrix)
            result = (list(row_sums), list(col_sums))
            assert result == expected, (
                f"{fn.__name__}({matrix!r}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(row_col_sums_ugly([[1, 2, 3], [4, 5, 6]]))
    print(row_col_sums_ugly([[1]]))
    print(row_col_sums_ugly([[1, 1], [1, 1], [1, 1]]))
