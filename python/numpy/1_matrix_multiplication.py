# Theory:
## Matrix multiplication is the textbook example of why vectorization
## matters for numeric code. The naive definition - for each output cell,
## sum the products of a row and a column - is a triple-nested loop,
## O(n^3) for n x n matrices, and in pure Python each of those inner
## multiply-adds pays interpreter overhead per element. NumPy's np.dot
## (and the @ operator) delegates to BLAS (Basic Linear Algebra
## Subprograms) - highly optimized, often multi-threaded C/Fortran
## routines that exploit CPU cache lines and SIMD instructions. The
## algorithmic complexity doesn't change (still roughly O(n^3) for naive
## BLAS, better for advanced algorithms like Strassen's), but the constant
## factor difference between a Python triple loop and BLAS is often
## 100-1000x for realistic matrix sizes.


# Packages:
## numpy.dot / the @ operator - matrix multiplication, delegates to BLAS
## numpy.matmul - the explicit matrix-multiply function (what @ calls)
## numpy.array - construct/represent matrices as ndarrays
## numpy.zeros - preallocate an output matrix for the manual triple-loop version


# Task:
## Given two 2D lists (matrices) A (m x n) and B (n x p), return their
## matrix product A @ B as a 2D list (m x p). Assume the dimensions are
## compatible for multiplication.
## Test1: Inputs: A = [[1,2],[3,4]], B = [[5,6],[7,8]]   Outputs: [[19,22],[43,50]]
## Test2: Inputs: A = [[1,0],[0,1]], B = [[5,6],[7,8]]   Outputs: [[5,6],[7,8]]
## Test3: Inputs: A = [[1,2,3]], B = [[1],[1],[1]]   Outputs: [[6]]
## Hint:
## Ugly way: triple nested loop - manually sum row*column products,
## O(m*n*p), pure Python overhead per multiply-add.
## Right way: numpy.dot (or @) - vectorized, delegates to BLAS.


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def matmul_ugly(a, b):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def matmul(a, b):
    return matmul_ugly(a, b)


# Tests:
def validate():
    cases = [
        ([[1, 2], [3, 4]], [[5, 6], [7, 8]], [[19, 22], [43, 50]]),
        ([[1, 0], [0, 1]], [[5, 6], [7, 8]], [[5, 6], [7, 8]]),
        ([[1, 2, 3]], [[1], [1], [1]], [[6]]),
    ]
    for fn in (matmul_ugly, matmul):
        for a, b, expected in cases:
            result = fn(a, b)
            result = [list(row) for row in result]
            assert result == expected, (
                f"{fn.__name__}({a!r}, {b!r}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(matmul_ugly([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
    print(matmul_ugly([[1, 0], [0, 1]], [[5, 6], [7, 8]]))
    print(matmul_ugly([[1, 2, 3]], [[1], [1], [1]]))
