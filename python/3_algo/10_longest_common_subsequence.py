# Theory:
## The longest common subsequence (LCS) of two strings is the longest
## sequence of characters that appears in both, in the same relative
## order, but not necessarily contiguously. It's a classic 2D dynamic
## programming problem: define dp[i][j] as the LCS length using the first
## i characters of one string and the first j of the other. If those two
## characters match, dp[i][j] = dp[i-1][j-1] + 1 (extend the previous
## LCS); otherwise dp[i][j] = max(dp[i-1][j], dp[i][j-1]) (skip one
## character from either string, whichever preserves the longer match).
## This gives O(m*n) time and O(m*n) space for the full table - which can
## be reduced to O(min(m,n)) space, since each row only ever depends on
## the row directly above it. The naive alternative, trying every
## subsequence of one string against the other, is exponential.


# Packages:
## functools.lru_cache - memoize a recursive character-by-character LCS definition
## itertools.combinations - brute-force baseline: generate every subsequence of the shorter string
## difflib.SequenceMatcher - stdlib tool for related sequence-comparison tasks (diff, not exactly LCS length)


# Task:
## Given two strings text1 and text2, return the length of their longest
## common subsequence. If there is no common subsequence, return 0.
## Test1: Inputs: text1 = "abcde", text2 = "ace"   Outputs: 3
## Test2: Inputs: text1 = "abc", text2 = "abc"   Outputs: 3
## Test3: Inputs: text1 = "abc", text2 = "def"   Outputs: 0
## Hint:
## Ugly way: itertools.combinations - generate every subsequence of the
## shorter string and check if it appears (in order) in the other, O(2^n).
## Right way: dynamic programming (2D table) - build dp[i][j] bottom-up
## from matches/skips, O(m*n).


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def longest_common_subsequence_ugly(text1, text2):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def longest_common_subsequence(text1, text2):
    return longest_common_subsequence_ugly(text1, text2)


# Tests:
def validate():
    cases = [
        ("abcde", "ace", 3),
        ("abc", "abc", 3),
        ("abc", "def", 0),
        ("", "abc", 0),
    ]
    for fn in (longest_common_subsequence_ugly, longest_common_subsequence):
        for text1, text2, expected in cases:
            result = fn(text1, text2)
            assert result == expected, (
                f"{fn.__name__}({text1!r}, {text2!r}): expected {expected}, got {result}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(longest_common_subsequence_ugly("abcde", "ace"))
    print(longest_common_subsequence_ugly("abc", "abc"))
    print(longest_common_subsequence_ugly("abc", "def"))
    print(longest_common_subsequence_ugly("", "abc"))
