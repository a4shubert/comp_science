// Theory:
// Naive recursive Fibonacci looks elegant but recomputes the same
// subproblems exponentially many times - F(n-1) and F(n-2) each
// independently recompute F(n-3), and so on - giving O(2^n) time despite
// there being only O(n) distinct subproblems. This is the classic
// argument for memoization: caching each computed F(k) collapses the
// exponential blowup down to O(n), since every subproblem is now solved
// once - C++ has no built-in equivalent to Python's functools.lru_cache,
// so the cache is usually hand-rolled with std::unordered_map. The
// iterative two-variable version sidesteps the issue entirely by building
// up from the base cases with O(1) space. Recognizing this recompute
// pattern - a recurrence that branches into overlapping subproblems - is
// the entry point into dynamic programming.

// Headers & STL components:
// <unordered_map> - hand-rolled memoization cache (no built-in lru_cache)
// <numeric> - std::accumulate, fold-based iterative approach
// <ranges> - std::views::iota, a lazy integer range (C++20)
// <utility> - std::pair, carries the (prev, cur) running state through the fold

// Task:
// Write a function that returns the n-th Fibonacci number
// (1-indexed convention: F(1) = 1, F(2) = 1, F(3) = 2, F(4) = 3, F(5) = 5, ...)
// Test1: Inputs: n = 1   Outputs: 1
// Test2: Inputs: n = 6   Outputs: 8
// Test3: Inputs: n = 11   Outputs: 89

// Solutions:
#include <algorithm>
#include <cassert>
#include <iostream>
#include <numeric>
#include <ranges>
#include <stdexcept>
#include <utility>
#include <vector>

// Space - Time Complexity analysis:
// space: O(n) - vector grows to hold n elements
// time: O(n) - the loop runs n-2 times to build up the vector
unsigned long long fibonacci_iterative_ugly(int n) {
    if (n < 0) throw std::invalid_argument("n must be non-negative");
    if (n == 1 || n == 2) return 1;
    std::vector<unsigned long long> fib = {1, 1};
    for (int i = 2; i < n; ++i) {
        fib.push_back(fib[fib.size() - 2] + fib[fib.size() - 1]);
    }
    return fib.back();
}

// Space - Time Complexity analysis:
// space: O(1) - only two running values (x, y) are kept regardless of n
// time: O(n) - the loop runs n-1 times, updating the pair once per iteration
unsigned long long fibonacci_iterative_nice(int n) {
    if (n <= 0) throw std::invalid_argument("n must be positive");
    if (n == 1 || n == 2) return 1;
    unsigned long long x = 1, y = 1;
    for (int i = 1; i < n; ++i) {
        unsigned long long next = x + y;
        y = x;
        x = next;
    }
    return y;
}

// Space - Time Complexity analysis:
// space: O(n) - call stack depth
// time: O(2^n) - naive, no memoization; total calls double each level
unsigned long long fibonacci_recursive(int n) {
    if (n <= 0) throw std::invalid_argument("n must be positive");
    if (n == 1 || n == 2) return 1;
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2);
}

// Space - Time Complexity analysis:
// space: O(1) - fixed-size pair accumulator, iota view is lazy
// time: O(n) - accumulate advances the (prev, cur) pair n-1 times
unsigned long long fibonacci_functional(int n) {
    if (n < 0) throw std::invalid_argument("n must be non-negative");
    auto range = std::views::iota(0, std::max(0, n - 1));
    auto result = std::accumulate(
        range.begin(), range.end(), std::make_pair(1ULL, 1ULL),
        [](std::pair<unsigned long long, unsigned long long> acc, int) {
            return std::make_pair(acc.first + acc.second, acc.first);
        });
    return result.second;
}

// Tests:
void validate() {
    std::vector<int> inputs;
    for (int n = 1; n <= 11; ++n) inputs.push_back(n);
    std::vector<unsigned long long> expected = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89};
    for (size_t i = 0; i < inputs.size(); ++i) {
        assert(fibonacci_iterative_ugly(inputs[i]) == expected[i]);
        assert(fibonacci_iterative_nice(inputs[i]) == expected[i]);
        assert(fibonacci_recursive(inputs[i]) == expected[i]);
        assert(fibonacci_functional(inputs[i]) == expected[i]);
    }
    std::cout << "SUCCESS" << std::endl;
}

int main() {
    validate();
    return 0;
}
