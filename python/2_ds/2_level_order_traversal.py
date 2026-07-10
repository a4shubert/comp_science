# Theory:
## A binary tree is a hierarchical structure where each node has at most
## two children. Traversing it "level order" (breadth-first, top to
## bottom, left to right within each level) needs a queue, not a stack:
## you process a node, then enqueue its children so they're visited after
## every other node already waiting at the current depth - a FIFO
## structure preserves that "finish this level before starting the next"
## ordering. This is different from depth-first traversals (preorder,
## inorder, postorder), which use a stack (explicit or the call stack) and
## dive to a leaf before backtracking. BFS-style level order is the
## natural choice whenever "shortest path" or "distance/depth" matters,
## since it explores everything at distance k before anything at k+1.


# Packages:
## collections.deque - O(1) append/popleft, the queue that drives BFS
## collections.defaultdict(list) - grouping nodes by level when building the result
## queue.Queue - the thread-safe alternative to deque (unneeded here, single-threaded)


# Task:
## Given the root of a binary tree (TreeNode with val/left/right), return
## its level order traversal as a list of lists - one inner list per
## depth, left to right.
## Test1: Inputs: root = [3,9,20,None,None,15,7]   Outputs: [[3],[9,20],[15,7]]
## Test2: Inputs: root = [1]   Outputs: [[1]]
## Test3: Inputs: root = []   Outputs: []
## Hint:
## Ugly way: recursive DFS - track each node's depth, append its value
## into a list indexed/grouped by depth.
## Right way: collections.deque - BFS, processing one full level (queue
## snapshot) per iteration.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    # level-order list with None for missing children, LeetCode-style
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def level_order_ugly(root):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def level_order(root):
    return level_order_ugly(root)


# Tests:
def validate():
    cases = [
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([1], [[1]]),
        ([], []),
        ([1, 2, 3], [[1], [2, 3]]),
    ]
    for fn in (level_order_ugly, level_order):
        for values, expected in cases:
            result = fn(build_tree(values))
            assert result == expected, (
                f"{fn.__name__}({values!r}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(level_order_ugly(build_tree([3, 9, 20, None, None, 15, 7])))
    print(level_order_ugly(build_tree([1])))
    print(level_order_ugly(build_tree([])))
    print(level_order_ugly(build_tree([1, 2, 3])))
