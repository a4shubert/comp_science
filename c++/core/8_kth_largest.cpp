// Theory:
// A heap is a tree-shaped structure that keeps the minimum (or maximum)
// element accessible in O(1), with O(log n) insert and removal - C++'s
// std::priority_queue implements a max-heap by default atop a
// std::vector, and takes std::greater<T> as its comparator to become a
// min-heap instead. For "kth largest/smallest" or "top-k" problems, you
// don't need to sort everything: maintain a heap of only k elements,
// pushing new candidates and popping the smallest whenever the heap
// exceeds size k, so the root always holds the answer once the pass
// finishes - O(n log k) time instead of the O(n log n) a full sort would
// cost, and O(k) space instead of O(n). This pattern generalizes to any
// streaming "keep the best k seen so far" problem, not just a single
// final answer.

// Headers & STL components:
// <queue> - std::priority_queue, a heap-backed container adaptor
// <functional> - std::greater<T>, the comparator that turns priority_queue into a min-heap
// <algorithm> - std::sort, the brute-force baseline, O(n log n)
// <vector> - the input container type here

// Task:
// Given a vector of integers nums and an integer k, return the k-th
// largest element in the vector. (k=1 means the largest element.)
// Duplicates count by position, not by distinct value - e.g. {3,3,4} with
// k=2 is 3.
// Test1: Inputs: nums = {3, 2, 1, 5, 6, 4}, k = 2   Outputs: 5
// Test2: Inputs: nums = {3, 2, 3, 1, 2, 4, 5, 5, 6}, k = 4   Outputs: 4
// Test3: Inputs: nums = {1}, k = 1   Outputs: 1
// Hint:
// Ugly way: std::sort - sort the whole vector, then index into it.
// Right way: std::priority_queue - maintain a size-k min-heap without
// sorting everything.

// Solutions:
#include <algorithm>
#include <cassert>
#include <functional>
#include <iostream>
#include <queue>
#include <vector>

// Space - Time Complexity analysis:
// space: O(n) - sorting a copy of nums holds all n elements
// time: O(n log n) - sorting dominates

int kth_largest_ugly(std::vector<int> nums, int k) {
    std::sort(nums.begin(), nums.end(), std::greater<int>());  // O(n) | O(n log n)
    return nums[k - 1];  // O(1) | O(1)
}

// Space - Time Complexity analysis:
// space: O(k) - the heap never holds more than k elements at once
// time: O(n log k) - n pushes/pops, each costing O(log k) on a size-k heap

int kth_largest(const std::vector<int>& nums, int k) {
    // min-heap that will hold the k largest values seen so far
    std::priority_queue<int, std::vector<int>, std::greater<int>> heap;  // O(1) | O(1)
    // walk through nums once
    for (int num : nums) {  // O(1) | O(n)
        // add the current number as a candidate
        heap.push(num);  // O(k) | O(log k)
        // heap grew past k - drop the smallest of the current top-k+1
        if (static_cast<int>(heap.size()) > k) {  // O(1) | O(1)
            heap.pop();  // O(1) | O(log k)
        }
    }
    // smallest of the k largest is exactly the k-th largest overall
    return heap.top();  // O(1) | O(1)
}

// Tests:
void validate() {
    struct Case {
        std::vector<int> nums;
        int k;
        int expected;
    };
    std::vector<Case> cases = {
        {{3, 2, 1, 5, 6, 4}, 2, 5},
        {{3, 2, 3, 1, 2, 4, 5, 5, 6}, 4, 4},
        {{1}, 1, 1},
        {{2, 1}, 2, 1},
    };
    for (const auto& c : cases) {
        assert(kth_largest_ugly(c.nums, c.k) == c.expected);
        assert(kth_largest(c.nums, c.k) == c.expected);
    }
    std::cout << "SUCCESS" << std::endl;
}

int main() {
    validate();
    return 0;
}
