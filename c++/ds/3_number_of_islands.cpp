// Theory:
// A grid of cells is really just a graph in disguise: each cell is a
// node, connected to its (up to 4) orthogonal neighbors. "Number of
// islands" - counting connected groups of land cells - is the classic
// connected-components problem on that implicit graph. You scan every
// cell; whenever you find unvisited land, that's a brand new island, so
// you flood-fill outward (DFS or BFS) marking every reachable land cell
// as visited so it's never counted again. The choice between DFS
// (recursion or an explicit stack) and BFS (a queue) doesn't change the
// O(rows*cols) time complexity - each cell is visited once - but DFS
// recursion depth can hit an island's full size, while BFS's queue holds
// at most one "frontier" of cells at a time.

// Headers & STL components:
// <queue> - std::queue, for BFS flood-fill
// <vector> - the grid's row/column container type
// <utility> - std::pair<int,int>, for queueing cell coordinates

// Task:
// Given a 2D grid of '1' (land) and '0' (water) characters, return the
// number of islands. An island is formed by connecting adjacent land
// cells horizontally or vertically (not diagonally).
// Test1: Inputs: grid = {{1,1,0},{1,0,0},{0,0,1}}   Outputs: 2
// Test2: Inputs: grid = {{1,1,1},{0,1,0},{1,0,1}}   Outputs: 3
// Test3: Inputs: grid = {{0,0},{0,0}}   Outputs: 0
// Hint:
// Ugly way: DFS via recursion - recursively flood-fill each new island,
// marking visited cells directly on the grid.
// Right way: std::queue - BFS flood-fill, avoiding deep recursion for
// large islands.

// Solutions:
#include <cassert>
#include <iostream>
#include <queue>
#include <utility>
#include <vector>

// Space - Time Complexity analysis:
// space:
// time:

int num_islands_ugly([[maybe_unused]] std::vector<std::vector<char>> grid) {
    // TODO: implement
    return 0;
}

// Space - Time Complexity analysis:
// space:
// time:

int num_islands(std::vector<std::vector<char>> grid) {
    return num_islands_ugly(grid);
}

// Tests:
void validate() {
    struct Case {
        std::vector<std::vector<char>> grid;
        int expected;
    };
    std::vector<Case> cases = {
        {{{'1', '1', '0'}, {'1', '0', '0'}, {'0', '0', '1'}}, 2},
        {{{'1', '1', '1'}, {'0', '1', '0'}, {'1', '0', '1'}}, 3},
        {{{'0', '0'}, {'0', '0'}}, 0},
        {{{'1'}}, 1},
    };
    for (const auto& c : cases) {
        assert(num_islands_ugly(c.grid) == c.expected);
        assert(num_islands(c.grid) == c.expected);
    }
    std::cout << "SUCCESS" << std::endl;
}

int main() {
    validate();
    return 0;
}
