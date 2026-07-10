# Theory:
## Solving a linear system Ax = b by hand means Gaussian elimination:
## repeatedly combine rows to zero out entries below the diagonal (forward
## elimination), then substitute back from the last row upward
## (back-substitution) - O(n^3) time, and easy to get numerically unstable
## without pivoting (swapping rows to avoid dividing by a tiny number).
## scipy.linalg.solve calls LAPACK routines that perform LU decomposition
## with partial pivoting automatically, giving both better numerical
## stability and a heavily optimized O(n^3) implementation. This is the
## direct workhorse behind linear regression (the normal equations reduce
## to solving a linear system), portfolio optimization, and any problem
## that reduces to "find x such that this linear relationship holds."


# Packages:
## scipy.linalg.solve - solve Ax=b directly via LU decomposition with partial pivoting
## numpy.linalg.solve - numpy's equivalent (scipy.linalg is a superset with more specialized solvers)
## numpy.linalg.inv - compute the matrix inverse directly (works, but less numerically stable/efficient than solve)


# Task:
## Given a square matrix A (list of lists) and a vector b (list),
## representing the linear system Ax = b, return the solution vector x,
## with each entry rounded to 2 decimal places. Assume A is invertible.
## Test1: Inputs: A = [[3,1],[1,2]], b = [9,8]   Outputs: [2.0, 3.0]
## Test2: Inputs: A = [[1,0],[0,1]], b = [5,7]   Outputs: [5.0, 7.0]
## Test3: Inputs: A = [[2,0,0],[0,3,0],[0,0,4]], b = [4,9,8]   Outputs: [2.0, 3.0, 2.0]
## Hint:
## Ugly way: manual Gaussian elimination - forward-eliminate below the
## diagonal, then back-substitute, O(n^3) with no pivoting.
## Right way: scipy.linalg.solve - LAPACK-backed LU decomposition with
## partial pivoting, O(n^3) but numerically stable and heavily optimized.


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def solve_linear_system_ugly(a, b):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def solve_linear_system(a, b):
    return solve_linear_system_ugly(a, b)


# Tests:
def validate():
    cases = [
        ([[3, 1], [1, 2]], [9, 8], [2.0, 3.0]),
        ([[1, 0], [0, 1]], [5, 7], [5.0, 7.0]),
        ([[2, 0, 0], [0, 3, 0], [0, 0, 4]], [4, 9, 8], [2.0, 3.0, 2.0]),
    ]
    for fn in (solve_linear_system_ugly, solve_linear_system):
        for a, b, expected in cases:
            result = [round(v, 2) for v in fn(a, b)]
            assert result == expected, (
                f"{fn.__name__}({a!r}, {b!r}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(solve_linear_system_ugly([[3, 1], [1, 2]], [9, 8]))
    print(solve_linear_system_ugly([[1, 0], [0, 1]], [5, 7]))
    print(solve_linear_system_ugly([[2, 0, 0], [0, 3, 0], [0, 0, 4]], [4, 9, 8]))
