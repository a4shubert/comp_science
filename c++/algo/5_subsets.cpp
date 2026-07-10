// Theory:
// Subsets (the power set) is another classic backtracking exercise, but
// with a different branching structure than permutations: at each
// element, you make a binary choice - include it in the current subset,
// or don't - rather than choosing among remaining unused items. This
// naturally produces 2^n subsets for n elements (each element
// independently in or out), so the total output size alone is
// exponential, same as permutations' n!. The backtracking template is
// identical in spirit though: append the current partial subset to the
// results, try including the next element and recurse, then undo that
// choice and recurse without it - covering both branches of the binary
// choice tree exhaustively.

// Headers & STL components:
// <vector> - the input/output container type here
// <bitset> - a fixed-size bitmask; each of 2^n bitmasks directly encodes one subset membership pattern
// <algorithm> - std::sort, useful when normalizing subsets for comparison

// Task:
// Given a vector of unique integers, return all possible subsets (the
// power set), in any order. The solution must not contain duplicate
// subsets.
// Test1: Inputs: nums = {1, 2, 3}   Outputs: {{},{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}}
// Test2: Inputs: nums = {0}   Outputs: {{},{0}}
// Test3: Inputs: nums = {}   Outputs: {{}}
// Hint:
// Ugly way: bitmask enumeration - iterate every integer from 0 to 2^n-1,
// treating each bit as "is this element included?"
// Right way: hand-written backtracking - for each element, recurse once
// including it and once excluding it.

// Solutions:
#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

// Space - Time Complexity analysis:
// space:
// time:

std::vector<std::vector<int>> subsets_ugly([[maybe_unused]] std::vector<int> nums) {
    // TODO: implement
    return {};
}

// Space - Time Complexity analysis:
// space:
// time:

std::vector<std::vector<int>> subsets(std::vector<int> nums) {
    return subsets_ugly(nums);
}

std::vector<std::vector<int>> normalize(std::vector<std::vector<int>> subsets_list) {
    for (auto& s : subsets_list) std::sort(s.begin(), s.end());
    std::sort(subsets_list.begin(), subsets_list.end());
    return subsets_list;
}

// Tests:
void validate() {
    struct Case {
        std::vector<int> nums;
        std::vector<std::vector<int>> expected;
    };
    std::vector<Case> cases = {
        {{1, 2, 3}, {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}},
        {{0}, {{}, {0}}},
        {{}, {{}}},
    };
    for (const auto& c : cases) {
        assert(normalize(subsets_ugly(c.nums)) == normalize(c.expected));
        assert(normalize(subsets(c.nums)) == normalize(c.expected));
    }
    std::cout << "SUCCESS" << std::endl;
}

int main() {
    validate();
    return 0;
}
