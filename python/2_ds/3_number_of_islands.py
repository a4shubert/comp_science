# Theory:
## A grid of cells is really just a graph in disguise: each cell is a
## node, and it's connected to its (up to 4) orthogonal neighbors. "Number
## of islands" - counting connected groups of land cells - is the classic
## connected-components problem on that implicit graph. You scan every
## cell; whenever you find unvisited land, that's a brand new island, so
## you flood-fill outward (DFS or BFS) marking every reachable land cell
## as visited so it's never counted again. The choice between DFS
## (recursion or an explicit stack) and BFS (a queue) doesn't change the
## O(rows*cols) time complexity - each cell is visited once - but DFS
## recursion depth can hit an island's full size, while BFS's queue holds
## at most one "frontier" of cells at a time.


# Packages:
## collections.deque - O(1) queue for BFS flood-fill
## sys.setrecursionlimit - relevant if DFS recursion depth could exceed Python's default limit for large islands
## copy.deepcopy - useful if you need to preserve the original grid while marking visited cells destructively


# Task:
## Given a 2D grid of '1' (land) and '0' (water) characters, return the
## number of islands. An island is formed by connecting adjacent land
## cells horizontally or vertically (not diagonally).
## Test1: Inputs: grid = [["1","1","0"],["1","0","0"],["0","0","1"]]   Outputs: 2
## Test2: Inputs: grid = [["1","1","1"],["0","1","0"],["1","0","1"]]   Outputs: 3
## Test3: Inputs: grid = [["0","0"],["0","0"]]   Outputs: 0
## Hint:
## Ugly way: DFS via recursion - recursively flood-fill each new island,
## marking visited cells directly on the grid.
## Right way: collections.deque - BFS flood-fill, avoiding deep recursion
## for large islands.


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def num_islands_ugly(grid):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def num_islands(grid):
    return num_islands_ugly(grid)


# Tests:
def validate():
    cases = [
        ([["1", "1", "0"], ["1", "0", "0"], ["0", "0", "1"]], 2),
        ([["1", "1", "1"], ["0", "1", "0"], ["1", "0", "1"]], 3),
        ([["0", "0"], ["0", "0"]], 0),
        ([["1"]], 1),
    ]
    for fn in (num_islands_ugly, num_islands):
        for grid, expected in cases:
            grid_copy = [row[:] for row in grid]
            result = fn(grid_copy)
            assert result == expected, (
                f"{fn.__name__}({grid!r}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(num_islands_ugly([["1", "1", "0"], ["1", "0", "0"], ["0", "0", "1"]]))
    print(num_islands_ugly([["1", "1", "1"], ["0", "1", "0"], ["1", "0", "1"]]))
    print(num_islands_ugly([["0", "0"], ["0", "0"]]))
    print(num_islands_ugly([["1"]]))
