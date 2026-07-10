// Theory:
// NumPy's core advantage over plain Python loops is vectorization:
// operations run as compiled C loops over contiguous memory, avoiding
// per-iteration interpreter overhead. C++ is already compiled, so the
// analogous win here isn't interpreter-overhead avoidance - it's an
// algorithmic one: a naive rolling-window computation recomputes the sum
// of each window from scratch, costing O(n*w) time for n elements and
// window size w. The fix is the same prefix-sum (cumulative sum) trick
// NumPy's cumsum-based approach exploits: precompute cumulative sums once
// in O(n), then each window's sum is just a difference of two prefix-sum
// entries, dropping the total cost to O(n) regardless of window size -
// std::partial_sum is the STL's direct equivalent of numpy.cumsum.

// Headers & STL components:
// <numeric> - std::partial_sum (prefix sums), std::accumulate (a window sum directly)
// <vector> - the input/output container type here
// <algorithm> - std::transform, elementwise vectorized-style operations

// Task:
// Given a vector of numbers prices and a window size w, return the simple
// moving average over each full window of size w - a vector of length
// prices.size() - w + 1. Assume 1 <= w <= prices.size().
// Test1: Inputs: prices = {1, 2, 3, 4, 5}, w = 2   Outputs: {1.5, 2.5, 3.5, 4.5}
// Test2: Inputs: prices = {1, 2, 3, 4, 5}, w = 3   Outputs: {2.0, 3.0, 4.0}
// Test3: Inputs: prices = {5, 5, 5, 5}, w = 2   Outputs: {5.0, 5.0, 5.0}
// Hint:
// Ugly way: nested loop - sum each window of w elements from scratch.
// Right way: std::partial_sum - precompute prefix sums once, then each
// window's sum is a single subtraction.

// Solutions:
#include <cassert>
#include <iostream>
#include <numeric>
#include <vector>

// Space - Time Complexity analysis:
// space: O(n) - result vector holds n-w+1 averages
// time: O(n*w) - n windows, each summed from scratch in O(w) via accumulate

std::vector<double> rolling_average_ugly(const std::vector<double>& prices, int w) {
    size_t window = static_cast<size_t>(w);  // O(1) | O(1)
    std::vector<double> result;  // O(1) | O(1)
    for (size_t i = 0; i + window <= prices.size(); ++i) {  // O(1) | O(n)
        double window_sum = std::accumulate(prices.begin() + i, prices.begin() + i + window, 0.0);  // O(w) | O(w)
        result.push_back(window_sum / w);  // O(n) | O(1)
    }
    return result;  // O(1) | O(1)
}

// Space - Time Complexity analysis:
// space: O(n) - the prefix-sum vector and the result vector both scale with n
// time: O(n) - two separate linear passes: build prefix sums, then one O(1) subtraction per window

std::vector<double> rolling_average(const std::vector<double>& prices, int w) {
    // prefix[i] = sum of the first i prices; prefix[0] = 0
    std::vector<double> prefix(prices.size() + 1, 0.0);  // O(n) | O(n)
    // build the cumulative sums in one pass
    std::partial_sum(prices.begin(), prices.end(), prefix.begin() + 1);  // O(1) | O(n)
    size_t window = static_cast<size_t>(w);  // O(1) | O(1)
    std::vector<double> result;  // O(1) | O(1)
    // each window's sum is just the difference of two prefix entries
    for (size_t i = 0; i + window <= prices.size(); ++i) {  // O(1) | O(n)
        double window_sum = prefix[i + window] - prefix[i];  // O(1) | O(1)
        result.push_back(window_sum / w);  // O(n) | O(1)
    }
    return result;  // O(1) | O(1)
}

// Tests:
void validate() {
    struct Case {
        std::vector<double> prices;
        int w;
        std::vector<double> expected;
    };
    std::vector<Case> cases = {
        {{1, 2, 3, 4, 5}, 2, {1.5, 2.5, 3.5, 4.5}},
        {{1, 2, 3, 4, 5}, 3, {2.0, 3.0, 4.0}},
        {{5, 5, 5, 5}, 2, {5.0, 5.0, 5.0}},
        {{2, 4, 6}, 3, {4.0}},
    };
    for (const auto& c : cases) {
        assert(rolling_average_ugly(c.prices, c.w) == c.expected);
        assert(rolling_average(c.prices, c.w) == c.expected);
    }
    std::cout << "SUCCESS" << std::endl;
}

int main() {
    validate();
    return 0;
}
