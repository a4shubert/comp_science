# Theory:
## A trie (prefix tree) stores a set of strings by sharing common
## prefixes: each node represents one character position, with children
## for each possible next character, and a marker for "a word ends here."
## Looking up or inserting a string of length L costs O(L), independent of
## how many other strings are stored - compare this to a hash set of
## strings, where insertion/lookup is O(L) to hash the string but checking
## "does any word start with this prefix?" would require scanning every
## stored string, O(n*L) in the worst case. A trie answers prefix queries
## in O(L) by simply walking down the tree as far as the prefix goes,
## which is exactly what autocomplete, spell-checkers, and IP routing
## tables rely on.


# Packages:
## collections.defaultdict - each node's children as a dict of char -> node, auto-creating on first access
## dict - the plain alternative to defaultdict for children
## dataclasses.dataclass - a concise way to define the node structure


# Task:
## Design a trie (prefix tree) supporting:
## - insert(word): add word to the trie.
## - search(word): return True if word was exactly inserted before.
## - starts_with(prefix): return True if any inserted word starts with
##   prefix.
## Test1: Inputs: ops=[insert("apple"), search("apple"), search("app"), starts_with("app"), insert("app"), search("app")]   Outputs: [None, True, False, True, None, True]
## Test2: Inputs: ops=[insert("cat"), starts_with("ca"), starts_with("dog")]   Outputs: [None, True, False]
## Test3: Inputs: ops=[search("missing")]   Outputs: [False]
## Hint:
## Ugly way: list of strings - insert appends to a list; search/starts_with
## do an O(n) scan (or O(n*L) with startswith) over every stored word.
## Right way: nested dict (trie nodes) - each character step is an O(1)
## dict lookup, so search/starts_with cost O(L), not O(n*L).


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

class TrieUgly:
    def __init__(self):
        pass

    def insert(self, word):
        pass

    def search(self, word):
        pass

    def starts_with(self, prefix):
        pass


# Space - Time Complexity analysis:
## space:
## time:

class Trie:
    def __init__(self):
        pass

    def insert(self, word):
        pass

    def search(self, word):
        pass

    def starts_with(self, prefix):
        pass


# Tests:
def validate():
    scenarios = [
        ([("insert", "apple", None), ("search", "apple", None), ("search", "app", None),
          ("starts_with", "app", None), ("insert", "app", None), ("search", "app", None)],
         [None, True, False, True, None, True]),
        ([("insert", "cat", None), ("starts_with", "ca", None), ("starts_with", "dog", None)],
         [None, True, False]),
        ([("search", "missing", None)], [False]),
    ]
    for cls in (TrieUgly, Trie):
        for ops, expected in scenarios:
            trie = cls()
            results = []
            for op, arg, _ in ops:
                if op == "insert":
                    results.append(trie.insert(arg))
                elif op == "search":
                    results.append(trie.search(arg))
                else:
                    results.append(trie.starts_with(arg))
            assert results == expected, (
                f"{cls.__name__}: expected {expected}, got {results}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    trie1 = TrieUgly()
    trie1.insert("apple")
    print([trie1.search("apple"), trie1.search("app"), trie1.starts_with("app")])
    trie1.insert("app")
    print(trie1.search("app"))
    trie2 = TrieUgly()
    trie2.insert("cat")
    print([trie2.starts_with("ca"), trie2.starts_with("dog")])
    trie3 = TrieUgly()
    print(trie3.search("missing"))
