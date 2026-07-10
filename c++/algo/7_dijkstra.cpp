// Theory:
// Dijkstra's algorithm finds shortest paths from a source node to every
// other node in a graph with non-negative edge weights. It's greedy: at
// each step, pick the unvisited node with the smallest known distance,
// finalize that distance (it can't improve later, since all edge weights
// are non-negative), then relax its outgoing edges - updating neighbors'
// distances if going through this node is shorter than what's currently
// known. A min-heap keyed by distance makes "pick the smallest unvisited
// distance" an O(log n) operation instead of an O(n) scan, bringing the
// total time down to O((V + E) log V) with a binary heap - the same
// priority-queue pattern used in kth-largest-style streaming problems,
// just applied to graph traversal instead of a plain value stream.

// Headers & STL components:
// <queue> - std::priority_queue (with std::greater) for picking the next-closest unvisited node
// <vector> - adjacency list representation of a weighted graph
// <limits> - std::numeric_limits<double>::infinity(), initial "unreached" distance

// Task:
// Given a weighted directed graph as a list of edges {u, v, weight} over
// n nodes (labeled 0 to n-1), and a source node, return the shortest
// distance from source to every node as a vector (index i = distance to
// node i), using infinity for unreachable nodes.
// Test1: Inputs: n = 4, edges = {{0,1,4},{0,2,1},{2,1,2},{1,3,1},{2,3,5}}, source = 0   Outputs: {0, 3, 1, 4}
// Test2: Inputs: n = 3, edges = {{0,1,1}}, source = 0   Outputs: {0, 1, inf}
// Test3: Inputs: n = 1, edges = {}, source = 0   Outputs: {0}
// Hint:
// Ugly way: Bellman-Ford style - relax every edge n-1 times in a loop, no
// priority queue, O(V*E).
// Right way: std::priority_queue - greedy min-heap pop of the closest
// unvisited node, O((V+E) log V).

// Solutions:
#include <cassert>
#include <iostream>
#include <limits>
#include <queue>
#include <vector>

// Space - Time Complexity analysis:
// space:
// time:

std::vector<double> dijkstra_ugly([[maybe_unused]] int n,
                                   [[maybe_unused]] const std::vector<std::vector<int>>& edges,
                                   [[maybe_unused]] int source) {
    // TODO: implement
    return {};
}

// Space - Time Complexity analysis:
// space:
// time:

std::vector<double> dijkstra(int n, const std::vector<std::vector<int>>& edges, int source) {
    return dijkstra_ugly(n, edges, source);
}

// Tests:
void validate() {
    double inf = std::numeric_limits<double>::infinity();
    struct Case {
        int n;
        std::vector<std::vector<int>> edges;
        int source;
        std::vector<double> expected;
    };
    std::vector<Case> cases = {
        {4, {{0, 1, 4}, {0, 2, 1}, {2, 1, 2}, {1, 3, 1}, {2, 3, 5}}, 0, {0, 3, 1, 4}},
        {3, {{0, 1, 1}}, 0, {0, 1, inf}},
        {1, {}, 0, {0}},
    };
    for (const auto& c : cases) {
        assert(dijkstra_ugly(c.n, c.edges, c.source) == c.expected);
        assert(dijkstra(c.n, c.edges, c.source) == c.expected);
    }
    std::cout << "SUCCESS" << std::endl;
}

int main() {
    validate();
    return 0;
}
