// Theory:
// The sliding window technique solves "find the best contiguous
// subarray/substring satisfying some property" problems in O(n) instead
// of the O(n^2) or O(n^3) of checking every substring explicitly. Two
// pointers (left, right) define the current window: right expands to
// include new elements, and left contracts only when the window violates
// the property (e.g. a repeated character). Because each pointer only
// ever moves forward, total pointer movement is bounded by 2n, giving
// linear time overall. A hash set or map often tracks what's "in" the
// window (or each element's last-seen index), letting you shrink or jump
// the window efficiently instead of rechecking it from scratch.

// Headers & STL components:
// <unordered_set> - track distinct characters currently "in" the window
// <unordered_map> - track counts or last-seen index per character
// <string> - the input container type here
// <algorithm> - std::max, for tracking the best window seen so far

// Task:
// Given a string s, find the length of the longest substring without
// repeating characters.
// Test1: Inputs: s = "abcabcbb"   Outputs: 3
// Test2: Inputs: s = "bbbbb"   Outputs: 1
// Test3: Inputs: s = "pwwkew"   Outputs: 3
// Hint:
// Ugly way: nested loops - check every substring for uniqueness directly.
// Right way: std::unordered_map (or set) - a sliding window avoids
// rechecking substrings from scratch.

// Solutions:
#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

// Space - Time Complexity analysis:
// space: O(n) - holding one substring's character set up to length n at a time
// time: O(n^3) - O(n^2) (i, j) pairs, each costing O(n) to build the substring + set
int length_of_longest_substring_ugly(const std::string& s) {
    int res = 0;
    for (size_t i = 0; i < s.size(); ++i) {
        for (size_t j = i + 1; j <= s.size(); ++j) {
            std::string substr = s.substr(i, j - i);
            std::unordered_set<char> chars(substr.begin(), substr.end());
            if (chars.size() == substr.size()) {
                res = std::max(res, static_cast<int>(substr.size()));
            }
        }
    }
    return res;
}

// Space - Time Complexity analysis:
// space: O(n) - last_seen map can grow to hold up to n entries
// time: O(n) - single pass, O(1) average unordered_map ops
int length_of_longest_substring(const std::string& s) {
    std::unordered_map<char, int> last_seen;
    int left = 0, res = 0;
    for (int right = 0; right < static_cast<int>(s.size()); ++right) {
        char ch = s[right];
        auto it = last_seen.find(ch);
        if (it != last_seen.end() && it->second >= left) {
            left = it->second + 1;
        }
        last_seen[ch] = right;
        res = std::max(res, right - left + 1);
    }
    return res;
}

// Tests:
void validate() {
    struct Case {
        std::string s;
        int expected;
    };
    std::vector<Case> cases = {
        {"abcabcbb", 3},
        {"bbbbb", 1},
        {"pwwkew", 3},
        {"", 0},
        {"dvdf", 3},
    };
    for (const auto& c : cases) {
        assert(length_of_longest_substring_ugly(c.s) == c.expected);
        assert(length_of_longest_substring(c.s) == c.expected);
    }
    std::cout << "SUCCESS" << std::endl;
}

int main() {
    validate();
    return 0;
}
