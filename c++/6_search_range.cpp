// Theory:
// Binary search finds a target in a sorted sequence in O(log n) by
// repeatedly halving the search space: compare the middle element, then
// recurse into whichever half could still contain the target. The
// <algorithm> header (std::lower_bound, std::upper_bound) implements this
// without you writing the low/high/mid loop by hand, returning iterators
// to insertion points rather than a boolean match - lower_bound finds the
// first valid position, upper_bound the position after any equal run.
// This makes it easy to answer "first/last occurrence" or "how many
// elements are less than x" questions on sorted data directly, without
// any extra pass over the container.

// Headers & STL components:
// <algorithm> - std::lower_bound / std::upper_bound, boundary search in O(log n)
// <algorithm> - std::binary_search, a plain boolean membership test
// <algorithm> - std::sort, general-purpose sort, O(n log n)
// <functional> - std::function, for a custom comparator if needed

// Task:
// Given a sorted vector of integers nums and a target value, return the
// [start, end] indices of the range where target appears. If target isn't
// in nums, return [-1, -1]. Assume nums is sorted in ascending order (may
// contain duplicates).
// Test1: Inputs: nums = {5, 7, 7, 8, 8, 10}, target = 8   Outputs: {3, 4}
// Test2: Inputs: nums = {5, 7, 7, 8, 8, 10}, target = 6   Outputs: {-1, -1}
// Test3: Inputs: nums = {}, target = 0   Outputs: {-1, -1}
// Hint:
// Ugly way: linear scan - walk the vector and track the first/last index
// where you see target.
// Right way: std::lower_bound / std::upper_bound - each finds a boundary
// in O(log n) without you writing the binary search by hand.

// Solutions:
#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

// Space - Time Complexity analysis:
// space: O(1) - only a couple of index variables are kept regardless of n
// time: O(n) - single linear pass
std::vector<int> search_range_ugly(const std::vector<int>& nums, int target) {
    int first = -1, last = -1;
    for (size_t i = 0; i < nums.size(); ++i) {
        if (nums[i] == target) {
            if (first == -1) first = static_cast<int>(i);
            last = static_cast<int>(i);
        }
    }
    return {first, last};
}

// Space - Time Complexity analysis:
// space: O(1) - lower_bound/upper_bound use no extra structures
// time: O(log n) - two binary searches
std::vector<int> search_range(const std::vector<int>& nums, int target) {
    auto left_it = std::lower_bound(nums.begin(), nums.end(), target);
    if (left_it == nums.end() || *left_it != target) {
        return {-1, -1};
    }
    auto right_it = std::upper_bound(nums.begin(), nums.end(), target);
    int left = static_cast<int>(left_it - nums.begin());
    int right = static_cast<int>(right_it - nums.begin()) - 1;
    return {left, right};
}

// Tests:
void validate() {
    struct Case {
        std::vector<int> nums;
        int target;
        std::vector<int> expected;
    };
    std::vector<Case> cases = {
        {{5, 7, 7, 8, 8, 10}, 8, {3, 4}},
        {{5, 7, 7, 8, 8, 10}, 6, {-1, -1}},
        {{}, 0, {-1, -1}},
        {{1}, 1, {0, 0}},
        {{2, 2, 2, 2}, 2, {0, 3}},
        {{5, 7, 7, 8, 8, 10}, 5, {0, 0}},
        {{5, 7, 7, 8, 8, 10}, 10, {5, 5}},
    };
    for (const auto& c : cases) {
        assert(search_range_ugly(c.nums, c.target) == c.expected);
        assert(search_range(c.nums, c.target) == c.expected);
    }
    std::cout << "SUCCESS" << std::endl;
}

int main() {
    validate();
    return 0;
}
