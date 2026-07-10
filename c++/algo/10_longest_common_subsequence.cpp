// Theory:
// The longest common subsequence (LCS) of two strings is the longest
// sequence of characters that appears in both, in the same relative
// order, but not necessarily contiguously. It's a classic 2D dynamic
// programming problem: define dp[i][j] as the LCS length using the first
// i characters of one string and the first j of the other. If those two
// characters match, dp[i][j] = dp[i-1][j-1] + 1 (extend the previous
// LCS); otherwise dp[i][j] = max(dp[i-1][j], dp[i][j-1]) (skip one
// character from either string, whichever preserves the longer match).
// This gives O(m*n) time and O(m*n) space for the full table - which can
// be reduced to O(min(m,n)) space, since each row only ever depends on
// the row directly above it. The naive alternative, trying every
// subsequence of one string against the other, is exponential.

// Headers & STL components:
// <vector> - the 2D DP table
// <string> - the input types here
// <algorithm> - std::max, choosing the better of two DP transitions

// Task:
// Given two strings text1 and text2, return the length of their longest
// common subsequence. If there is no common subsequence, return 0.
// Test1: Inputs: text1 = "abcde", text2 = "ace"   Outputs: 3
// Test2: Inputs: text1 = "abc", text2 = "abc"   Outputs: 3
// Test3: Inputs: text1 = "abc", text2 = "def"   Outputs: 0
// Hint:
// Ugly way: recursive subsequence enumeration - try every subsequence of
// the shorter string and check if it appears (in order) in the other,
// O(2^n).
// Right way: dynamic programming (2D table) - build dp[i][j] bottom-up
// from matches/skips, O(m*n).

// Solutions:
#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>

// Space - Time Complexity analysis:
// space:
// time:

int longest_common_subsequence_ugly([[maybe_unused]] const std::string& text1,
                                     [[maybe_unused]] const std::string& text2) {
    // TODO: implement
    return 0;
}

// Space - Time Complexity analysis:
// space:
// time:

int longest_common_subsequence(const std::string& text1, const std::string& text2) {
    return longest_common_subsequence_ugly(text1, text2);
}

// Tests:
void validate() {
    struct Case {
        std::string text1;
        std::string text2;
        int expected;
    };
    std::vector<Case> cases = {
        {"abcde", "ace", 3},
        {"abc", "abc", 3},
        {"abc", "def", 0},
        {"", "abc", 0},
    };
    for (const auto& c : cases) {
        assert(longest_common_subsequence_ugly(c.text1, c.text2) == c.expected);
        assert(longest_common_subsequence(c.text1, c.text2) == c.expected);
    }
    std::cout << "SUCCESS" << std::endl;
}

int main() {
    validate();
    return 0;
}
