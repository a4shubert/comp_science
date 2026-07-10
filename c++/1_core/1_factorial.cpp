// Theory:
// Factorial is a small case study in iteration vs. recursion. An iterative
// loop keeps a fixed amount of state (a running product) regardless of
// input size - O(1) space. Recursion instead breaks the problem into a
// smaller subproblem (n! = n * (n-1)!), but every call adds a frame to the
// call stack until the base case is hit, giving O(n) space. Unlike
// Python, C++ has no default recursion depth ceiling - it's bounded only
// by the OS thread stack size (typically a few MB) - so this recurses far
// deeper before crashing, but a stack overflow here is undefined behavior
// rather than a catchable exception. A third style, functional/fold-based
// (std::accumulate over a std::views::iota range), expresses the
// computation as folding a binary operator over a lazily-generated range -
// it reads declaratively but is still iterative underneath, so it keeps
// the O(1) space of the loop version.

// Headers & STL components:
// <numeric> - std::accumulate, folds a binary operator over a range
// <ranges> - std::views::iota, a lazy integer range (C++20)
// <functional> - std::multiplies<>, multiplication as a callable object
// <stdexcept> - std::invalid_argument, for rejecting negative input

// Task:
// Write a function factorial(n) which returns the n-th factorial.
// Test1: Inputs: n = 0   Outputs: 1
// Test2: Inputs: n = 4   Outputs: 24
// Test3: Inputs: n = 7   Outputs: 5040

// Solutions:
#include <algorithm>
#include <cassert>
#include <functional>
#include <iostream>
#include <numeric>
#include <ranges>
#include <stdexcept>
#include <vector>

// Space - Time Complexity analysis:
// space: O(1) - only a running product and loop counter are kept
// time: O(n) - the loop runs n times, one multiplication per iteration
unsigned long long factorial_iterative(int n) {
    // reject negative input up front
    if (n < 0) throw std::invalid_argument("n must be non-negative");  // O(1) | O(1)
    // running product, starts at the multiplicative identity
    unsigned long long res = 1;  // O(1) | O(1)
    // multiply in each factor from 2 up to n
    for (int i = 2; i <= n; ++i) {  // O(1) | O(n)
        res *= i;  // O(1) | O(1)
    }
    return res;  // O(1) | O(1)
}

// Space - Time Complexity analysis:
// space: O(n) - call stack depth n
// time: O(n) - one recursive call per level, from n down to the base case
unsigned long long factorial_recursive(int n) {
    // reject negative input up front
    if (n < 0) throw std::invalid_argument("n must be non-negative");  // O(1) | O(1)
    // base case: 0! = 1
    if (n == 0) return 1;  // O(1) | O(1)
    // n! = n times (n-1)!
    return static_cast<unsigned long long>(n) * factorial_recursive(n - 1);  // O(n) | O(n)
}

// Space - Time Complexity analysis:
// space: O(1) - views::iota is a lazy range, nothing is materialized
// time: O(n) - accumulate performs n-1 multiplications
unsigned long long factorial_functional(int n) {
    // reject negative input up front
    if (n < 0) throw std::invalid_argument("n must be non-negative");  // O(1) | O(1)
    // lazy range 2..n (clamped so n=0/1 produce an empty range, not an invalid one)
    auto range = std::views::iota(2, std::max(2, n + 1));  // O(1) | O(1)
    // fold multiplication over the range, starting from the identity 1
    return std::accumulate(range.begin(), range.end(), 1ULL,
                            std::multiplies<unsigned long long>());  // O(1) | O(n)
}

// Tests:
void validate() {
    std::vector<int> inputs = {0, 1, 2, 3, 4, 5, 6, 7};
    std::vector<unsigned long long> expected = {1, 1, 2, 6, 24, 120, 720, 5040};
    for (size_t i = 0; i < inputs.size(); ++i) {
        assert(factorial_iterative(inputs[i]) == expected[i]);
        assert(factorial_recursive(inputs[i]) == expected[i]);
        assert(factorial_functional(inputs[i]) == expected[i]);
    }
    std::cout << "SUCCESS" << std::endl;
}

int main() {
    validate();
    return 0;
}
