// Theory:
// Hash maps (C++'s std::unordered_map) give average O(1) lookup, insert,
// and delete by mapping keys to array slots via a hash function, trading
// the O(log n) of a balanced tree (std::map) or the O(n) of a linear scan
// for near-constant time - at the cost of no ordering guarantee and
// occasional collision overhead. The classic pattern for pair-finding
// problems - two-sum, anagram grouping, duplicate detection - is a single
// pass that checks "have I seen the complement/target already?" before
// inserting the current element, turning an O(n^2) nested-loop brute
// force into O(n) time. The tradeoff is O(n) extra space to hold the
// elements seen so far.

// Headers & STL components:
// <unordered_map> - hash map, average O(1) lookup/insert/delete
// <map> - ordered alternative, O(log n), useful when iteration order matters
// <algorithm> - std::find, std::sort, general-purpose algorithms
// <vector> - the input container type here

// Task:
// Given a vector of integers nums and an integer target, return the
// indices of the two numbers that add up to target. Assume exactly one
// valid answer exists, and you may not use the same element twice.
// Test1: Inputs: nums = {2, 7, 11, 15}, target = 9   Outputs: {0, 1}
// Test2: Inputs: nums = {3, 2, 4}, target = 6   Outputs: {1, 2}
// Test3: Inputs: nums = {3, 3}, target = 6   Outputs: {0, 1}
// Hint:
// Ugly way: nested loop - check every pair of indices directly.
// Right way: std::unordered_map - check before you insert, so you don't
// accidentally pair an element with itself.

// Solutions:
#include <algorithm>
#include <cassert>
#include <iostream>
#include <unordered_map>
#include <vector>

// Space - Time Complexity analysis:
// space: O(1) - no extra structure beyond the loop indices
// time: O(n^2) - a nested loop checks every pair of indices
std::vector<int> two_sum_ugly(const std::vector<int>& nums, int target) {
    for (size_t i = 0; i < nums.size(); ++i) {
        for (size_t j = i + 1; j < nums.size(); ++j) {
            if (nums[i] + nums[j] == target) {
                return {static_cast<int>(i), static_cast<int>(j)};
            }
        }
    }
    return {-1, -1};
}

// Space - Time Complexity analysis:
// space: O(n) - seen map can hold up to n-1 entries in the worst case
// time: O(n) - single pass, O(1) average unordered_map lookup/insert
std::vector<int> two_sum(const std::vector<int>& nums, int target) {
    std::unordered_map<int, int> seen;
    for (size_t i = 0; i < nums.size(); ++i) {
        int complement = target - nums[i];
        auto it = seen.find(complement);
        if (it != seen.end()) {
            return {it->second, static_cast<int>(i)};
        }
        seen[nums[i]] = static_cast<int>(i);
    }
    return {-1, -1};
}

// Tests:
void validate() {
    struct Case {
        std::vector<int> nums;
        int target;
        std::vector<int> expected;
    };
    std::vector<Case> cases = {
        {{2, 7, 11, 15}, 9, {0, 1}},
        {{3, 2, 4}, 6, {1, 2}},
        {{3, 3}, 6, {0, 1}},
    };
    for (const auto& c : cases) {
        auto r1 = two_sum_ugly(c.nums, c.target);
        auto r2 = two_sum(c.nums, c.target);
        std::vector<int> s1 = r1, s2 = r2;
        std::sort(s1.begin(), s1.end());
        std::sort(s2.begin(), s2.end());
        std::vector<int> expected_sorted = c.expected;
        std::sort(expected_sorted.begin(), expected_sorted.end());
        assert(s1 == expected_sorted);
        assert(s2 == expected_sorted);
    }
    std::cout << "SUCCESS" << std::endl;
}

int main() {
    validate();
    return 0;
}
