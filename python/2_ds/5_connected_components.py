# Theory:
## Union-Find (disjoint set union) tracks a partition of elements into
## disjoint groups, supporting two operations: find(x) - which group is x
## in? - and union(x, y) - merge x's group and y's group. A naive
## implementation makes find/union O(n) in the worst case (a long chain of
## parent pointers). Two optimizations fix this: path compression (during
## find, point every visited node directly at the root, flattening future
## lookups) and union by rank/size (always attach the smaller tree under
## the larger one's root, keeping trees shallow). Combined, both
## operations become nearly O(1) amortized (technically O(alpha(n)), the
## inverse Ackermann function, which is effectively constant for any
## realistic n). This makes Union-Find the standard tool for "connected
## components," cycle detection in undirected graphs, and Kruskal's MST.


# Packages:
## list - a plain array used as the parent[] pointer structure
## collections.defaultdict - alternative when node labels aren't small contiguous integers
## itertools.combinations - not for Union-Find itself, but common alongside it when pairing all edges


# Task:
## Given n nodes labeled 0 to n-1 and a list of undirected edges, return
## the number of connected components in the graph.
## Test1: Inputs: n = 5, edges = [[0,1],[1,2],[3,4]]   Outputs: 2
## Test2: Inputs: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]   Outputs: 1
## Test3: Inputs: n = 4, edges = []   Outputs: 4
## Hint:
## Ugly way: DFS/BFS from each unvisited node - flood-fill each component
## using an adjacency list, counting how many flood-fills you needed.
## Right way: Union-Find (with path compression + union by rank) - union
## each edge's endpoints, then count distinct roots.


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def count_components_ugly(n, edges):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def count_components(n, edges):
    return count_components_ugly(n, edges)


# Tests:
def validate():
    cases = [
        (5, [[0, 1], [1, 2], [3, 4]], 2),
        (5, [[0, 1], [1, 2], [2, 3], [3, 4]], 1),
        (4, [], 4),
        (1, [], 1),
    ]
    for fn in (count_components_ugly, count_components):
        for n, edges, expected in cases:
            result = fn(n, edges)
            assert result == expected, (
                f"{fn.__name__}({n}, {edges!r}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(count_components_ugly(5, [[0, 1], [1, 2], [3, 4]]))
    print(count_components_ugly(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))
    print(count_components_ugly(4, []))
    print(count_components_ugly(1, []))
