// Theory:
// Quicksort is the other classic divide-and-conquer sort: pick a pivot,
// partition the array so everything smaller than the pivot ends up to
// its left and everything larger to its right, then recursively sort
// each side. Unlike merge sort, partitioning can be done in place, so
// quicksort typically needs only O(log n) extra space (the recursion
// stack) rather than O(n) - but its worst-case time is O(n^2), which
// happens when the pivot choice repeatedly splits the array as unevenly
// as possible. Randomizing the pivot choice (or using median-of-three)
// makes that worst case astronomically unlikely in practice, which is
// why quicksort - despite the theoretically worse bound - is often
// faster in practice than merge sort due to better cache locality and
// lower constant factors. std::sort itself is typically introsort:
// quicksort that falls back to heapsort if recursion gets too deep.

// Headers & STL components:
// <algorithm> - std::sort (introsort), std::nth_element (partial quickselect-style partitioning)
// <random> - std::mt19937/std::uniform_int_distribution, for randomized pivot selection
// <vector> - the array type being sorted

// Task:
// Given a vector of integers, return it sorted in ascending order using
// quicksort.
// Test1: Inputs: nums = {5, 2, 4, 1, 3}   Outputs: {1, 2, 3, 4, 5}
// Test2: Inputs: nums = {3, 3, 1, 2}   Outputs: {1, 2, 3, 3}
// Test3: Inputs: nums = {}   Outputs: {}
// Hint:
// Ugly way: std::sort - the standard library's sort, O(n log n), but
// doesn't demonstrate the partition mechanics.
// Right way: hand-written quicksort - pick a pivot, partition in place
// around it, recurse on each side.

// Solutions:
#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

// Space - Time Complexity analysis:
// space:
// time:

std::vector<int> quick_sort_ugly([[maybe_unused]] std::vector<int> nums) {
    // TODO: implement
    return {};
}

// Space - Time Complexity analysis:
// space:
// time:

std::vector<int> quick_sort(std::vector<int> nums) {
    return quick_sort_ugly(nums);
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
        assert(quick_sort_ugly(c.nums) == c.expected);
        assert(quick_sort(c.nums) == c.expected);
    }
    std::cout << "SUCCESS" << std::endl;
}

int main() {
    validate();
    return 0;
}
