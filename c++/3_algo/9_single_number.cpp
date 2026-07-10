// Theory:
// XOR (^) has two properties that make it a powerful bit-manipulation
// tool: x ^ x == 0 (anything XORed with itself cancels to zero), and
// x ^ 0 == x (XOR with zero is a no-op), and it's both commutative and
// associative, so the order of operations doesn't matter. XOR every
// element of an array together, and every value that appears an even
// number of times cancels itself out completely, leaving only whatever
// appears an odd number of times. This solves "find the single element
// that doesn't appear twice" in O(n) time and O(1) space - no hash set
// needed to track what's been seen, which is normally the O(n) space
// you'd reach for first. Bit tricks like this show up whenever a problem
// has an "everything pairs up except one thing" structure.

// Headers & STL components:
// <numeric> - std::accumulate, fold XOR across the whole vector in one call
// <unordered_map> - frequency counting, the straightforward O(n) space alternative
// <functional> - std::bit_xor<int>, the XOR operator as a callable, usable with accumulate

// Task:
// Given a non-empty vector of integers where every element appears twice
// except for one, find that single element. Your solution should ideally
// use O(1) extra space.
// Test1: Inputs: nums = {2, 2, 1}   Outputs: 1
// Test2: Inputs: nums = {4, 1, 2, 1, 2}   Outputs: 4
// Test3: Inputs: nums = {1}   Outputs: 1
// Hint:
// Ugly way: std::unordered_map - count occurrences of every value, then
// return the one with count 1; O(n) space.
// Right way: XOR fold - XOR every element together; pairs cancel to zero,
// leaving only the single element; O(1) space.

// Solutions:
#include <cassert>
#include <functional>
#include <iostream>
#include <numeric>
#include <unordered_map>
#include <vector>

// Space - Time Complexity analysis:
// space:
// time:

int single_number_ugly([[maybe_unused]] const std::vector<int>& nums) {
    // TODO: implement
    return 0;
}

// Space - Time Complexity analysis:
// space:
// time:

int single_number(const std::vector<int>& nums) {
    return single_number_ugly(nums);
}

// Tests:
void validate() {
    struct Case {
        std::vector<int> nums;
        int expected;
    };
    std::vector<Case> cases = {
        {{2, 2, 1}, 1},
        {{4, 1, 2, 1, 2}, 4},
        {{1}, 1},
        {{-1, -1, -2}, -2},
    };
    for (const auto& c : cases) {
        assert(single_number_ugly(c.nums) == c.expected);
        assert(single_number(c.nums) == c.expected);
    }
    std::cout << "SUCCESS" << std::endl;
}

int main() {
    validate();
    return 0;
}
