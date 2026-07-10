// Theory:
// A greedy algorithm makes the locally-best choice at each step and never
// reconsiders it, trusting that this leads to a globally optimal answer -
// which only works when the problem has the right structure (it doesn't
// for every problem). Jump Game is a clean example where greedy provably
// works: at each index, track the furthest index reachable so far; if you
// ever reach an index beyond that furthest reach, you're stuck. There's
// no need to explore every possible sequence of jumps (which would be
// exponential) - you only need to track one number, the best reach seen
// so far, updated in a single linear pass. Recognizing when a problem
// reduces to "track one running best value" instead of "explore all
// choices" is the key skill greedy problems test.

// Headers & STL components:
// <algorithm> - std::max, track the running furthest-reachable index
// <vector> - the input container type here

// Task:
// Given a vector of non-negative integers where each element represents
// the maximum jump length from that position, determine if you can reach
// the last index starting from index 0.
// Test1: Inputs: nums = {2, 3, 1, 1, 4}   Outputs: true
// Test2: Inputs: nums = {3, 2, 1, 0, 4}   Outputs: false
// Test3: Inputs: nums = {0}   Outputs: true
// Hint:
// Ugly way: recursive/backtracking - try every possible jump length from
// each position, exploring the full tree of jump sequences.
// Right way: greedy single pass - track the furthest index reachable so
// far, fail only if you reach a position beyond it.

// Solutions:
#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

// Space - Time Complexity analysis:
// space:
// time:

bool can_jump_ugly([[maybe_unused]] const std::vector<int>& nums) {
    // TODO: implement
    return false;
}

// Space - Time Complexity analysis:
// space:
// time:

bool can_jump(const std::vector<int>& nums) {
    return can_jump_ugly(nums);
}

// Tests:
void validate() {
    struct Case {
        std::vector<int> nums;
        bool expected;
    };
    std::vector<Case> cases = {
        {{2, 3, 1, 1, 4}, true},
        {{3, 2, 1, 0, 4}, false},
        {{0}, true},
        {{1, 0, 1}, false},
    };
    for (const auto& c : cases) {
        assert(can_jump_ugly(c.nums) == c.expected);
        assert(can_jump(c.nums) == c.expected);
    }
    std::cout << "SUCCESS" << std::endl;
}

int main() {
    validate();
    return 0;
}
