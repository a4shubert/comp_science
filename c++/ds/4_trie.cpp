// Theory:
// A trie (prefix tree) stores a set of strings by sharing common
// prefixes: each node represents one character position, with children
// for each possible next character, and a marker for "a word ends here."
// Looking up or inserting a string of length L costs O(L), independent of
// how many other strings are stored - compare this to a hash set of
// strings, where checking "does any word start with this prefix?" would
// require scanning every stored string, O(n*L) in the worst case. A trie
// answers prefix queries in O(L) by simply walking down the tree as far
// as the prefix goes, which is exactly what autocomplete, spell-checkers,
// and IP routing tables rely on.

// Headers & STL components:
// <unordered_map> - each node's children as char -> node*, auto-creating on first access
// <memory> - std::unique_ptr, for owning child nodes safely
// <string> - the key type stored/queried

// Task:
// Design a trie (prefix tree) supporting:
// - insert(word): add word to the trie.
// - search(word): return true if word was exactly inserted before.
// - starts_with(prefix): return true if any inserted word starts with
//   prefix.
// Test1: Inputs: ops=[insert("apple"), search("apple"), search("app"), starts_with("app"), insert("app"), search("app")]   Outputs: {-, true, false, true, -, true}
// Test2: Inputs: ops=[insert("cat"), starts_with("ca"), starts_with("dog")]   Outputs: {-, true, false}
// Test3: Inputs: ops=[search("missing")]   Outputs: {false}
// Hint:
// Ugly way: vector<string> - insert appends to a vector; search/starts_with
// do an O(n) scan over every stored word.
// Right way: unordered_map-based trie nodes - each character step is an
// O(1) map lookup, so search/starts_with cost O(L), not O(n*L).

// Solutions:
#include <cassert>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

// Space - Time Complexity analysis:
// space:
// time:

class TrieUgly {
public:
    void insert([[maybe_unused]] const std::string& word) {
        // TODO: implement
    }

    bool search([[maybe_unused]] const std::string& word) {
        // TODO: implement
        return false;
    }

    bool starts_with([[maybe_unused]] const std::string& prefix) {
        // TODO: implement
        return false;
    }
};

// Space - Time Complexity analysis:
// space:
// time:

class Trie {
public:
    void insert([[maybe_unused]] const std::string& word) {
        // TODO: implement
    }

    bool search([[maybe_unused]] const std::string& word) {
        // TODO: implement
        return false;
    }

    bool starts_with([[maybe_unused]] const std::string& prefix) {
        // TODO: implement
        return false;
    }
};

// Tests:
template <typename TrieT>
void run_trie_tests() {
    {
        TrieT t;
        t.insert("apple");
        assert(t.search("apple") == true);
        assert(t.search("app") == false);
        assert(t.starts_with("app") == true);
        t.insert("app");
        assert(t.search("app") == true);
    }
    {
        TrieT t;
        t.insert("cat");
        assert(t.starts_with("ca") == true);
        assert(t.starts_with("dog") == false);
    }
    {
        TrieT t;
        assert(t.search("missing") == false);
    }
}

void validate() {
    run_trie_tests<TrieUgly>();
    run_trie_tests<Trie>();
    std::cout << "SUCCESS" << std::endl;
}

int main() {
    validate();
    return 0;
}
