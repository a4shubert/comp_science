# Theory:
## Broadcasting lets NumPy apply an operation between arrays of different
## (but compatible) shapes without writing an explicit loop or manually
## replicating data. When shapes don't match, NumPy compares them
## dimension by dimension from the right: dimensions are compatible if
## they're equal, or if one of them is 1 (in which case that dimension is
## conceptually "stretched" to match, without actually copying memory).
## Adding a 1D vector of length n to each row of an (m, n) matrix is the
## classic example: the vector's shape (n,) broadcasts against the
## matrix's (m, n) by treating the vector as if it were repeated m times,
## but the actual computation happens without materializing that
## repetition - it's done in a single vectorized pass, avoiding both an
## explicit Python loop and the O(m*n) memory a literal tile/repeat would
## cost.


# Packages:
## numpy.array arithmetic operators (+, -, *, /) - trigger broadcasting automatically on shape mismatch
## numpy.newaxis / numpy.reshape - explicitly add a dimension to control how broadcasting aligns shapes
## numpy.tile / numpy.repeat - the manual, memory-costly alternative to what broadcasting does implicitly
## numpy.broadcast_to - explicitly view an array as if broadcast to a target shape, without copying


# Task:
## Given a matrix (list of lists) and a vector (list) whose length matches
## the number of columns, return a new matrix where the vector has been
## added to every row.
## Test1: Inputs: matrix = [[1,2,3],[4,5,6]], vector = [10,20,30]   Outputs: [[11,22,33],[14,25,36]]
## Test2: Inputs: matrix = [[0,0],[0,0]], vector = [1,2]   Outputs: [[1,2],[1,2]]
## Test3: Inputs: matrix = [[5]], vector = [5]   Outputs: [[10]]
## Hint:
## Ugly way: nested loop - for each row, for each column, add the
## corresponding vector element manually.
## Right way: numpy broadcasting - matrix_arr + vector_arr, letting numpy
## stretch the vector across every row in one vectorized call.


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def add_vector_to_rows_ugly(matrix, vector):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def add_vector_to_rows(matrix, vector):
    return add_vector_to_rows_ugly(matrix, vector)


# Tests:
def validate():
    cases = [
        ([[1, 2, 3], [4, 5, 6]], [10, 20, 30], [[11, 22, 33], [14, 25, 36]]),
        ([[0, 0], [0, 0]], [1, 2], [[1, 2], [1, 2]]),
        ([[5]], [5], [[10]]),
    ]
    for fn in (add_vector_to_rows_ugly, add_vector_to_rows):
        for matrix, vector, expected in cases:
            result = fn(matrix, vector)
            result = [list(row) for row in result]
            assert result == expected, (
                f"{fn.__name__}({matrix!r}, {vector!r}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(add_vector_to_rows_ugly([[1, 2, 3], [4, 5, 6]], [10, 20, 30]))
    print(add_vector_to_rows_ugly([[0, 0], [0, 0]], [1, 2]))
    print(add_vector_to_rows_ugly([[5]], [5]))
