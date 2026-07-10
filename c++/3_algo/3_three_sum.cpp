// Theory:
// The two-pointer technique extends naturally from two-sum to three-sum:
// sort the array first (O(n log n)), then fix one element and use two
// pointers (from the two ends of the remaining subarray) to find pairs
// that sum to the target, moving inward based on whether the current sum
// is too high or too low - since the subarray is sorted, moving a
// pointer strictly increases or decreases the sum, so you never need to
// backtrack. This turns an O(n^3) brute-force triple-nested loop into
// O(n^2): O(n) choices for the fixed element, times O(n) for the
// two-pointer scan. The same pattern generalizes to k-sum problems by
// fixing k-2 elements and two-pointering the rest.

// Headers & STL components:
// <algorithm> - std::sort, the prerequisite that makes two-pointer scanning valid
// <set> - std::set<std::vector<int>>, deduplicate triplets automatically
// <vector> - the input/output container type here

// Task:
// Given a vector of integers, return all unique triplets {a, b, c} such
// that a + b + c == 0. The solution set must not contain duplicate
// triplets.
// Test1: Inputs: nums = {-1, 0, 1, 2, -1, -4}   Outputs: {{-1, -1, 2}, {-1, 0, 1}}
// Test2: Inputs: nums = {0, 1, 1}   Outputs: {}
// Test3: Inputs: nums = {0, 0, 0}   Outputs: {{0, 0, 0}}
// Hint:
// Ugly way: triple nested loop - enumerate every triple directly and
// keep the ones that sum to zero, O(n^3).
// Right way: sort + two pointers - fix one element, then two-pointer scan
// the rest, O(n^2) overall.

// Solutions:
#include <algorithm>
#include <cassert>
#include <iostream>
#include <set>
#include <vector>

// Space - Time Complexity analysis:
// space:
// time:

std::vector<std::vector<int>> three_sum_ugly([[maybe_unused]] std::vector<int> nums) {
    // TODO: implement
    return {};
}

// Space - Time Complexity analysis:
// space:
// time:

std::vector<std::vector<int>> three_sum(std::vector<int> nums) {
    return three_sum_ugly(nums);
}

std::set<std::vector<int>> normalize(const std::vector<std::vector<int>>& triplets) {
    std::set<std::vector<int>> result;
    for (auto t : triplets) {
        std::sort(t.begin(), t.end());
        result.insert(t);
    }
    return result;
}

// Tests:
void validate() {
    struct Case {
        std::vector<int> nums;
        std::vector<std::vector<int>> expected;
    };
    std::vector<Case> cases = {
        {{-1, 0, 1, 2, -1, -4}, {{-1, -1, 2}, {-1, 0, 1}}},
        {{0, 1, 1}, {}},
        {{0, 0, 0}, {{0, 0, 0}}},
        {{}, {}},
    };
    for (const auto& c : cases) {
        assert(normalize(three_sum_ugly(c.nums)) == normalize(c.expected));
        assert(normalize(three_sum(c.nums)) == normalize(c.expected));
    }
    std::cout << "SUCCESS" << std::endl;
}

int main() {
    validate();
    return 0;
}
