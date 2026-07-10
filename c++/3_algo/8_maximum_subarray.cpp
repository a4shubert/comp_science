// Theory:
// Kadane's algorithm finds the maximum-sum contiguous subarray in O(n)
// time by making a simple local decision at each position: either extend
// the current subarray by including this element, or start a new
// subarray here - whichever gives a larger running sum. The insight is
// that a negative running sum can never help a future subarray, so as
// soon as the running total drops below zero (or below just the current
// element), it's better to restart from the current element than to drag
// the negative baggage forward. This is a form of dynamic programming
// where the "state" is compressed to a single running value (best sum
// ending exactly at the current index) rather than a full table, since
// each step only depends on the immediately preceding one.

// Headers & STL components:
// <numeric> - std::accumulate, running sums for the brute-force O(n^2) approach
// <limits> - std::numeric_limits<int>::min(), initial baseline for tracking a running maximum
// <algorithm> - std::max, comparing extend-vs-restart at each step

// Task:
// Given an integer vector, find the contiguous subarray (containing at
// least one number) with the largest sum, and return that sum.
// Test1: Inputs: nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4}   Outputs: 6
// Test2: Inputs: nums = {1}   Outputs: 1
// Test3: Inputs: nums = {5, 4, -1, 7, 8}   Outputs: 23
// Hint:
// Ugly way: nested loop over every (i, j) pair - sum each subarray from
// scratch, O(n^2) or O(n^3) depending on how the sum is computed.
// Right way: Kadane's algorithm - a single pass, extending or restarting
// the running sum at each element, O(n).

// Solutions:
#include <algorithm>
#include <cassert>
#include <iostream>
#include <limits>
#include <vector>

// Space - Time Complexity analysis:
// space:
// time:

int max_subarray_ugly([[maybe_unused]] const std::vector<int>& nums) {
    // TODO: implement
    return 0;
}

// Space - Time Complexity analysis:
// space:
// time:

int max_subarray(const std::vector<int>& nums) {
    return max_subarray_ugly(nums);
}

// Tests:
void validate() {
    struct Case {
        std::vector<int> nums;
        int expected;
    };
    std::vector<Case> cases = {
        {{-2, 1, -3, 4, -1, 2, 1, -5, 4}, 6},
        {{1}, 1},
        {{5, 4, -1, 7, 8}, 23},
        {{-1}, -1},
    };
    for (const auto& c : cases) {
        assert(max_subarray_ugly(c.nums) == c.expected);
        assert(max_subarray(c.nums) == c.expected);
    }
    std::cout << "SUCCESS" << std::endl;
}

int main() {
    validate();
    return 0;
}
