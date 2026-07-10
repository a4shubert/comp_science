// Theory:
// A binary tree is a hierarchical structure where each node has at most
// two children. Traversing it "level order" (breadth-first, top to
// bottom, left to right within each level) needs a queue, not a stack:
// you process a node, then enqueue its children so they're visited after
// every other node already waiting at the current depth - a FIFO
// structure preserves that "finish this level before starting the next"
// ordering. This is different from depth-first traversals (preorder,
// inorder, postorder), which use a stack (explicit or the call stack) and
// dive to a leaf before backtracking. BFS-style level order is the
// natural choice whenever "shortest path" or "distance/depth" matters,
// since it explores everything at distance k before anything at k+1.

// Headers & STL components:
// <queue> - std::queue, O(1) push/pop, the queue that drives BFS
// <optional> - std::optional<int>, represents a possibly-missing tree value when building test trees
// <vector> - the input/output container type here

// Task:
// Given the root of a binary tree (TreeNode with val/left/right), return
// its level order traversal as a vector of vectors - one inner vector per
// depth, left to right.
// Test1: Inputs: root = {3,9,20,-,-,15,7}   Outputs: {{3},{9,20},{15,7}}
// Test2: Inputs: root = {1}   Outputs: {{1}}
// Test3: Inputs: root = {}   Outputs: {}
// Hint:
// Ugly way: recursive DFS - track each node's depth, append its value
// into a vector indexed/grouped by depth.
// Right way: std::queue - BFS, processing one full level (queue
// snapshot) per iteration.

// Solutions:
#include <cassert>
#include <iostream>
#include <optional>
#include <queue>
#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    explicit TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

TreeNode* build_tree(const std::vector<std::optional<int>>& values) {
    if (values.empty() || !values[0].has_value()) return nullptr;
    auto* root = new TreeNode(*values[0]);
    std::queue<TreeNode*> q;
    q.push(root);
    size_t i = 1;
    while (!q.empty() && i < values.size()) {
        TreeNode* node = q.front();
        q.pop();
        if (i < values.size() && values[i].has_value()) {
            node->left = new TreeNode(*values[i]);
            q.push(node->left);
        }
        ++i;
        if (i < values.size() && values[i].has_value()) {
            node->right = new TreeNode(*values[i]);
            q.push(node->right);
        }
        ++i;
    }
    return root;
}

// Space - Time Complexity analysis:
// space:
// time:

std::vector<std::vector<int>> level_order_ugly([[maybe_unused]] TreeNode* root) {
    // TODO: implement
    return {};
}

// Space - Time Complexity analysis:
// space:
// time:

std::vector<std::vector<int>> level_order(TreeNode* root) {
    return level_order_ugly(root);
}

// Tests:
void validate() {
    struct Case {
        std::vector<std::optional<int>> values;
        std::vector<std::vector<int>> expected;
    };
    std::vector<Case> cases = {
        {{3, 9, 20, std::nullopt, std::nullopt, 15, 7}, {{3}, {9, 20}, {15, 7}}},
        {{1}, {{1}}},
        {{}, {}},
        {{1, 2, 3}, {{1}, {2, 3}}},
    };
    for (const auto& c : cases) {
        assert(level_order_ugly(build_tree(c.values)) == c.expected);
        assert(level_order(build_tree(c.values)) == c.expected);
    }
    std::cout << "SUCCESS" << std::endl;
}

int main() {
    validate();
    return 0;
}
