// Theory:
// Merge sort is the canonical divide-and-conquer sorting algorithm: split
// the array in half, recursively sort each half, then merge the two
// sorted halves back together in linear time. Because the array is
// halved at each level (log n levels) and merging a level's worth of
// subarrays costs O(n) total per level, the whole algorithm runs in
// O(n log n) time - guaranteed, not just on average, unlike quicksort's
// O(n^2) worst case. The tradeoff is space: the merge step needs an
// auxiliary array to combine two sorted halves without overwriting data
// still being read, costing O(n) extra space. Merge sort is also stable
// (equal elements keep their relative order), which matters when sorting
// records by one field while preserving an earlier sort on another.

// Headers & STL components:
// <algorithm> - std::sort (introsort, not stable) and std::stable_sort (typically merge-sort-based)
// <algorithm> - std::merge, merges two sorted ranges in O(n)
// <vector> - the array type being sorted

// Task:
// Given a vector of integers, return it sorted in ascending order using
// merge sort.
// Test1: Inputs: nums = {5, 2, 4, 1, 3}   Outputs: {1, 2, 3, 4, 5}
// Test2: Inputs: nums = {3, 3, 1, 2}   Outputs: {1, 2, 3, 3}
// Test3: Inputs: nums = {}   Outputs: {}
// Hint:
// Ugly way: std::sort - the standard library's sort, O(n log n), but
// doesn't demonstrate the merge-sort mechanics.
// Right way: hand-written merge sort - recursively split, then merge two
// sorted halves with std::merge or a manual two-pointer merge.

// Solutions:
#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

// Space - Time Complexity analysis:
// space:
// time:

std::vector<int> merge_sort_ugly([[maybe_unused]] std::vector<int> nums) {
    // TODO: implement
    return {};
}

// Space - Time Complexity analysis:
// space:
// time:

std::vector<int> merge_sort(std::vector<int> nums) {
    return merge_sort_ugly(nums);
}

// Tests:
void validate() {
    struct Case {
        std::vector<int> nums;
        std::vector<int> expected;
    };
    std::vector<Case> cases = {
        {{5, 2, 4, 1, 3}, {1, 2, 3, 4, 5}},
        {{3, 3, 1, 2}, {1, 2, 3, 3}},
        {{}, {}},
        {{1}, {1}},
    };
    for (const auto& c : cases) {
        assert(merge_sort_ugly(c.nums) == c.expected);
        assert(merge_sort(c.nums) == c.expected);
    }
    std::cout << "SUCCESS" << std::endl;
}

int main() {
    validate();
    return 0;
}
