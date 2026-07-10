# Theory:
## Dijkstra's algorithm finds shortest paths from a source node to every
## other node in a graph with non-negative edge weights. It's greedy: at
## each step, pick the unvisited node with the smallest known distance,
## finalize that distance (it can't improve later, since all edge weights
## are non-negative), then relax its outgoing edges - updating neighbors'
## distances if going through this node is shorter than what's currently
## known. A min-heap keyed by distance makes "pick the smallest unvisited
## distance" an O(log n) operation instead of an O(n) scan, bringing the
## total time down to O((V + E) log V) with a binary heap - the same
## priority-queue pattern used in kth-largest-style streaming problems,
## just applied to graph traversal instead of a plain value stream.


# Packages:
## heapq - min-heap for picking the next-closest unvisited node in O(log n)
## collections.defaultdict(list) - adjacency list representation of a weighted graph
## math.inf - initial "unknown/unreached" distance for every node


# Task:
## Given a weighted directed graph as a list of edges [u, v, weight] over
## n nodes (labeled 0 to n-1), and a source node, return the shortest
## distance from source to every node as a list (index i = distance to
## node i), using infinity (float('inf')) for unreachable nodes.
## Test1: Inputs: n = 4, edges = [[0,1,4],[0,2,1],[2,1,2],[1,3,1],[2,3,5]], source = 0   Outputs: [0, 3, 1, 4]
## Test2: Inputs: n = 3, edges = [[0,1,1]], source = 0   Outputs: [0, 1, float("inf")]
## Test3: Inputs: n = 1, edges = [], source = 0   Outputs: [0]
## Hint:
## Ugly way: Bellman-Ford style - relax every edge n-1 times in a loop, no
## priority queue, O(V*E).
## Right way: heapq - greedy min-heap pop of the closest unvisited node,
## O((V+E) log V).


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def dijkstra_ugly(n, edges, source):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def dijkstra(n, edges, source):
    return dijkstra_ugly(n, edges, source)


# Tests:
def validate():
    cases = [
        (4, [[0, 1, 4], [0, 2, 1], [2, 1, 2], [1, 3, 1], [2, 3, 5]], 0, [0, 3, 1, 4]),
        (3, [[0, 1, 1]], 0, [0, 1, float("inf")]),
        (1, [], 0, [0]),
    ]
    for fn in (dijkstra_ugly, dijkstra):
        for n, edges, source, expected in cases:
            result = fn(n, edges, source)
            assert result == expected, (
                f"{fn.__name__}({n}, {edges!r}, {source}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(dijkstra_ugly(4, [[0, 1, 4], [0, 2, 1], [2, 1, 2], [1, 3, 1], [2, 3, 5]], 0))
    print(dijkstra_ugly(3, [[0, 1, 1]], 0))
    print(dijkstra_ugly(1, [], 0))
