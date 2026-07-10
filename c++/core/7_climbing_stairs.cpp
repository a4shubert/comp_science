// Theory:
// Dynamic programming solves problems whose recurrence branches into
// overlapping subproblems (unlike divide-and-conquer, where subproblems
// don't overlap) by ensuring each distinct subproblem is computed once
// and reused. Two equivalent strategies: top-down memoization, where you
// keep the natural recursive structure but cache each return value
// (in C++, typically a hand-rolled std::unordered_map<int, long long>
// cache, since there's no built-in lru_cache), and bottom-up tabulation,
// where you iteratively build a table of answers from the base cases
// upward - usually trading the recursion's call-stack space for an
// explicit array (or just a few variables, if only the last couple of
// states matter).

// Headers & STL components:
// <unordered_map> - hand-rolled memoization cache (no built-in lru_cache)
// <vector> - explicit table for bottom-up tabulation
// <stdexcept> - std::invalid_argument, for rejecting invalid input

// Task:
// You're climbing a staircase with n steps. Each move you can climb
// either 1 or 2 steps. Return the number of distinct ways to reach the
// top. (n is a positive integer.)
// Test1: Inputs: n = 1   Outputs: 1
// Test2: Inputs: n = 4   Outputs: 5
// Test3: Inputs: n = 10   Outputs: 89
// Hint:
// Ugly way: naive recursion - same recurrence shape as the naive
// Fibonacci you already wrote, no caching.
// Right way: std::unordered_map - memoize the recursive calls so each n
// is only computed once.

// Solutions:
#include <cassert>
#include <iostream>
#include <stdexcept>
#include <unordered_map>
#include <vector>

// Space - Time Complexity analysis:
// space: O(n) - call stack depth n
// time: O(2^n) - same recurrence shape as naive Fibonacci; total calls double each level
long long climb_stairs_ugly(int n) {
    if (n <= 0) throw std::invalid_argument("n must be positive");  // O(1) | O(1)
    if (n == 1) return 1;  // O(1) | O(1)
    if (n == 2) return 2;  // O(1) | O(1)
    return climb_stairs_ugly(n - 1) + climb_stairs_ugly(n - 2);  // O(n) | O(2^n)
}

// Space - Time Complexity analysis:
// space: O(n) - cache holds one entry per distinct n, plus call stack depth n
// time: O(n) - each distinct n is computed once thanks to the cache; O(1) work per call after that
long long climb_stairs(int n, std::unordered_map<int, long long>& cache) {
    if (n <= 0) throw std::invalid_argument("n must be positive");  // O(1) | O(1)
    // base case: one step, one way
    if (n == 1) return 1;  // O(1) | O(1)
    // base case: two steps, two ways (1+1 or 2)
    if (n == 2) return 2;  // O(1) | O(1)
    // has this n already been computed?
    auto it = cache.find(n);  // O(1) | O(1)
    if (it != cache.end()) return it->second;  // O(1) | O(1)
    // ways to reach n = ways to reach n-1, plus ways to reach n-2
    long long result = climb_stairs(n - 1, cache) + climb_stairs(n - 2, cache);  // O(n) | O(n)
    // cache this n so it's never recomputed
    cache[n] = result;  // O(n) | O(1)
    return result;  // O(1) | O(1)
}

long long climb_stairs(int n) {
    // fresh cache for this top-level call
    std::unordered_map<int, long long> cache;  // O(1) | O(1)
    return climb_stairs(n, cache);  // O(1) | O(1)
}

// Tests:
void validate() {
    struct Case {
        int n;
        long long expected;
    };
    std::vector<Case> cases = {
        {1, 1}, {2, 2}, {3, 3}, {4, 5}, {5, 8}, {6, 13}, {10, 89},
    };
    for (const auto& c : cases) {
        assert(climb_stairs_ugly(c.n) == c.expected);
        assert(climb_stairs(c.n) == c.expected);
    }
    std::cout << "SUCCESS" << std::endl;
}

int main() {
    validate();
    return 0;
}
