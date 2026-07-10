// Theory:
// Backtracking builds a solution incrementally, exploring one choice at a
// time, and undoes ("backtracks") a choice as soon as it can't lead to a
// valid complete solution - it's DFS over a tree of partial solutions.
// Generating all permutations is the canonical backtracking exercise: at
// each step, choose one of the remaining unused elements to place next,
// recurse, then undo that choice (mark it unused again) before trying the
// next option. There are n! permutations of n elements, and building each
// one takes O(n) (placing each of n elements), so the total work is
// O(n * n!) - this is fundamentally exponential, not a complexity you can
// improve algorithmically, since the answer itself has that many entries.
// The value of backtracking here is systematically covering every
// possibility without missing or repeating one.

// Headers & STL components:
// <algorithm> - std::next_permutation, direct built-in in-place permutation generator
// <vector> - the input/output container type here

// Task:
// Given a vector of distinct integers, return all possible permutations,
// in any order.
// Test1: Inputs: nums = {1, 2, 3}   Outputs: {{1,2,3},{1,3,2},{2,1,3},{2,3,1},{3,1,2},{3,2,1}}
// Test2: Inputs: nums = {0, 1}   Outputs: {{0,1},{1,0}}
// Test3: Inputs: nums = {1}   Outputs: {{1}}
// Hint:
// Ugly way: std::next_permutation - the standard library's in-place
// generator, correct but doesn't demonstrate the backtracking mechanics.
// Right way: hand-written backtracking - choose an unused element,
// recurse, then undo the choice before trying the next one.

// Solutions:
#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

// Space - Time Complexity analysis:
// space:
// time:

std::vector<std::vector<int>> permutations_ugly([[maybe_unused]] std::vector<int> nums) {
    // TODO: implement
    return {};
}

// Space - Time Complexity analysis:
// space:
// time:

std::vector<std::vector<int>> permutations(std::vector<int> nums) {
    return permutations_ugly(nums);
}

// Tests:
void validate() {
    struct Case {
        std::vector<int> nums;
        std::vector<std::vector<int>> expected;
    };
    std::vector<Case> cases = {
        {{1, 2, 3}, {{1, 2, 3}, {1, 3, 2}, {2, 1, 3}, {2, 3, 1}, {3, 1, 2}, {3, 2, 1}}},
        {{0, 1}, {{0, 1}, {1, 0}}},
        {{1}, {{1}}},
    };
    for (const auto& c : cases) {
        auto r1 = permutations_ugly(c.nums);
        auto r2 = permutations(c.nums);
        auto expected = c.expected;
        std::sort(r1.begin(), r1.end());
        std::sort(r2.begin(), r2.end());
        std::sort(expected.begin(), expected.end());
        assert(r1 == expected);
        assert(r2 == expected);
    }
    std::cout << "SUCCESS" << std::endl;
}

int main() {
    validate();
    return 0;
}
