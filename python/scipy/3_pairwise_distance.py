# Theory:
## Computing pairwise Euclidean distances between every pair of points in
## two sets is a common building block in clustering, nearest-neighbor
## search, and similarity analysis. The direct approach nests a loop over
## each point in set A inside a loop over each point in set B, computing
## one distance at a time - O(n*m) distance computations, each itself
## O(d) for d-dimensional points, done with Python-level arithmetic.
## scipy.spatial.distance.cdist computes the entire n x m distance matrix
## in one vectorized call, using the same underlying trick as matrix
## multiplication: ||a-b||^2 = ||a||^2 + ||b||^2 - 2*a.b expands the
## squared distance into dot products, which BLAS computes for the whole
## matrix at once rather than point by point.


# Packages:
## scipy.spatial.distance.cdist - pairwise distances between two point sets, one vectorized call
## scipy.spatial.distance.pdist - pairwise distances within a single point set (condensed form)
## scipy.spatial.distance.euclidean - single-pair distance, useful for the brute-force baseline
## numpy.linalg.norm - vector norm, another way to compute a single Euclidean distance


# Task:
## Given two lists of 2D points A and B, return the n x m matrix of
## Euclidean distances (as a list of lists) where entry [i][j] is the
## distance from A[i] to B[j], each rounded to 2 decimal places.
## Test1: Inputs: A = [[0,0]], B = [[3,4]]   Outputs: [[5.0]]
## Test2: Inputs: A = [[0,0],[1,1]], B = [[0,0]]   Outputs: [[0.0],[1.41]]
## Test3: Inputs: A = [[0,0]], B = [[0,0]]   Outputs: [[0.0]]
## Hint:
## Ugly way: nested loop - for each point in A, for each point in B,
## compute the Euclidean distance directly, O(n*m*d).
## Right way: scipy.spatial.distance.cdist - the entire distance matrix in
## one vectorized call.


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def pairwise_distances_ugly(a, b):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def pairwise_distances(a, b):
    return pairwise_distances_ugly(a, b)


# Tests:
def validate():
    cases = [
        ([[0, 0]], [[3, 4]], [[5.0]]),
        ([[0, 0], [1, 1]], [[0, 0]], [[0.0], [1.41]]),
        ([[0, 0]], [[0, 0]], [[0.0]]),
    ]
    for fn in (pairwise_distances_ugly, pairwise_distances):
        for a, b, expected in cases:
            result = fn(a, b)
            result = [[round(v, 2) for v in row] for row in result]
            assert result == expected, (
                f"{fn.__name__}({a!r}, {b!r}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(pairwise_distances_ugly([[0, 0]], [[3, 4]]))
    print(pairwise_distances_ugly([[0, 0], [1, 1]], [[0, 0]]))
    print(pairwise_distances_ugly([[0, 0]], [[0, 0]]))
