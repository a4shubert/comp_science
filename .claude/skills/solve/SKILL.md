---
name: solve
description: >
  Write a complete, correct solution for a specific numbered interview-prep
  task, in BOTH Python and C++, e.g. "solve 6" or "/solve 6" implements
  python/6_whatever.py AND c++/6_whatever.cpp properly. Use this whenever
  the user says "solve <number>", asks you to implement/fix/finish a
  specific numbered task, or wants you to write the answer yourself rather
  than write it themselves. Fills in the Solutions, per-line space|time
  comments, a Space - Time Complexity analysis block above each function,
  and tests - to the same standard used throughout this repo (see
  python/1_factorial.py, python/3_two_sum.py, c++/3_two_sum.cpp).
---

# solve

Write the real solution for task `<number>` — not a hint, not a stub, the
actual working implementation in **both** `python/<number>_*.py` and
`c++/<number>_*.cpp`, commented the way every other solved file in this
repo is commented. This is the opposite mode from normal practice (where
the user writes and you review/grade) — here they're explicitly asking you
to do the writing, in both languages.

## Step 1 — Locate the files and read the task

Find `python/<number>_*.py`. Read its `# Task:` / `# Hint:` section — the
hint names tools by "Ugly way:" / "Right way:" (e.g. "nested loops" vs
"dict"). Implement **both** named approaches as separate functions when
the hint gives two, matching the pattern in `3_two_sum.py`
(`two_sum_ugly` / `two_sum`) and `5_valid_parentheses.py`
(`is_valid_ugly` / `is_valid`) — the point of keeping both is comparing
complexity, not just shipping the fast one.

The optimized function **must actually call** whatever tool the "Right
way:" line names — `numpy.cumsum`, `bisect_left`, `heapq`, `pandas.merge`,
whatever it says — not a hand-rolled reimplementation of the same idea in
plain Python/C++. If the Hint says "Right way: numpy.cumsum" and the
function is a hand-written prefix-sum loop instead, that's not solved
correctly, even if it's O(n) and passes the tests — the whole point of the
optimized version is demonstrating the library call, not just hitting the
right complexity by coincidence. This matters most for the numpy/scipy/
pandas-flavored tasks, where "the right way" specifically means the
vectorized library call, not a fast-but-manual Python equivalent.

Then check for `c++/<number>_*.cpp`. If it exists, solve it too (Step 5).
If it doesn't exist yet (e.g. the number predates this skill writing both
languages), create it first — mirror the Python file's Theory/Task/Hint/
Tests, translated to C++ comment syntax with a `// Headers & STL
components:` section in place of `# Packages:` (see the `next` skill's
Step 6 for the exact template) — then solve it the same as if it already
existed.

If either file already has a partial/buggy attempt in it, you don't need
to preserve its structure — write it properly, the way you would in a
review where you'd flag it as needing a real fix rather than a patch.
Don't leave dead code, shadowed builtins/names, or unhandled edge cases
(e.g. empty input, input with no valid answer) that a live interviewer
would flag.

The rest of this skill is organized in two halves: Steps 2-4 are Python,
Step 5 is the C++ equivalent of all three, Step 6 verifies both, Step 7
reports back on both.

## Step 2 — Comment every line with space | time complexity

Every executable line in each solution function gets a trailing comment in
the form `# O(space) | O(time)` — bare complexity only, no parenthetical
explanation on the line itself:

```python
for i, v in enumerate(nums):  # O(1) | O(n)
    seen[v] = i  # O(n) | O(1)
```

All reasoning/explanation belongs in the `# Space - Time Complexity
analysis:` block above the function (Step 3), not scattered across
individual lines — the per-line comments are just the numbers, so the
block above is the one place a reader looks for the "why".

Reason about each line honestly when deciding the number, don't just
default to O(1) everywhere:
- `range()`/`enumerate()` themselves are O(1) space (lazy), but the loop's
  own iteration count belongs on the `for`/`while` line as its time
  complexity.
- Slicing (`s[i:j]`), `set(x)`, `list(x)`, string concatenation, and
  similar copying operations cost O(k) in both space and time where k is
  the size involved — never mark these O(1).
- A line that grows a data structure across iterations (append, dict
  insert) gets the *cumulative* worst-case size as its space mark (e.g.
  O(n) if it can grow to hold n items by the end), even though the single
  operation is O(1) time (amortized).
- A recursive call line gets the function's overall contribution: call
  stack depth for space, total calls for time (e.g. naive Fibonacci's
  recursive line is `O(n) | O(2^n)`).
- Container end-access matters: `deque` supports O(1) access at both
  ends; a plain `list` is O(1) at the end but O(n) to insert/remove at the
  front.
- When two operations happen on one line, the line's cost is dominated by
  the more expensive one, not the sum of small differences in order.

State only the correct complexity — never phrase a comment or the report
as a correction or comparison against a wrong/previous value (e.g. don't
write "O(1) not O(n)" or "this is actually O(n), unlike before"). There's
no prior version in this mode; write the right answer plainly as if it
were the only one that ever existed.

In the **optimized function only** (`<function_name>`, not `_ugly`), add
a second comment directly above each line — a short plain-English phrase
for what that line *does*, separate from the `# O(space) | O(time)` that
stays trailing on the code line itself:

```python
def two_sum(nums, target):
    # dict mapping each value seen so far to its index
    seen = {}  # O(1) | O(1)
    # walk through nums once, tracking value and index together
    for i, v in enumerate(nums):  # O(1) | O(n)
        # the value that would complete the pair with v
        complement = target - v  # O(1) | O(1)
        # has the complement already been seen?
        if complement in seen:  # O(1) | O(1)
            # found the pair - return both indices
            return [seen[complement], i]  # O(1) | O(1)
        # record this value's index for future lookups
        seen[v] = i  # O(n) | O(1)
```

This is why the optimized function usually needs the walkthrough — it's
the one using the less-obvious tool, so a reader benefits from being told
what each step accomplishes, not just its cost. The `_ugly` function
stays as Step 2 describes it above (trailing complexity comment only, no
above-line description) — it's the brute-force approach, generally
self-explanatory without a line-by-line narration.

## Step 3 — Give each function its own Space - Time Complexity analysis block

Each function gets its own `# Space - Time Complexity analysis:` block
directly above it (not one combined block after all functions — see
`7_climbing_stairs.py`), with a `## space:` line and a `## time:` line,
each stating the complexity *and the reason for it*:

```python
# Space - Time Complexity analysis:
## space: O(1) - combinations is a lazy generator, no pairs held at once
## time: O(n^2) - n choose 2 = n(n-1)/2 pairs

def two_sum_ugly(nums, target):
    ...


# Space - Time Complexity analysis:
## space: O(n) - dict can grow to hold up to n entries
## time: O(n) - single pass, O(1) average dict lookup/insert

def two_sum(nums, target):
    ...
```

The reason clause is mandatory on *both* lines, every time — never leave
`## space:` or `## time:` as a bare `O(...)` with nothing after it, even
when the answer feels obvious (e.g. `O(1)` still needs "why nothing grows
with n" spelled out, one sentence). This is what makes `solve` different
from `next` (which leaves `## space:` / `## time:` blank for the user to
fill in themselves). State *why*, not just the order: what specifically
grows with input size, or how many operations actually happen.

This must actually match what Step 2's per-line comments add up to — if
they don't agree, one of them is wrong; re-check rather than picking
whichever sounds better.

## Step 4 — Update validate()

Keep the existing test cases (don't drop coverage), add any edge cases
your reasoning in Step 1 surfaced (empty input, single element, no valid
answer, all-duplicates, etc. — whatever's relevant to this problem), and
make sure the loop exercises every function variant you wrote, not just
one. `print("SUCCESS")` stays as the last line, after all asserts.

`__main__` should end up with only `validate()` — no `print(...)` calls
of any kind:

```python
if __name__ == "__main__":
    validate()
```

Don't leave `validate()` commented out — once `solve` produces a
finished, correct file, `validate()` should actually run and confirm
`SUCCESS`. Debug prints (per-case or otherwise) are the user's own
in-progress workflow for *their* unfinished attempts (see the `next`
skill); once `solve` hands back a finished file, that scaffolding is
gone — `validate()` passing is the only signal needed.

## Step 5 — Do the same for C++

Same standards as Steps 2-4, translated:

- **Per-line comments**: `// O(space) | O(time)`, bare, no parenthetical —
  same reasoning rules as Step 2 (recursive calls get the function's
  overall contribution; `std::deque` is O(1) at both ends, `std::vector`
  is O(1) at the back but O(n) at the front; slicing/copying containers
  costs O(k); a line that grows a container across iterations gets the
  cumulative worst-case size as its space mark). In the optimized
  function only, also add a `//` line above each statement describing
  what it does — same rule as Step 2's Python example, `//` instead of
  `#`, `_ugly` gets the trailing complexity comment only.
- **Complexity block**: `// Space - Time Complexity analysis:` directly
  above each function, with `// space:`/`// time:` lines and a mandatory
  one-sentence reason on both — same as Step 3, `//` instead of `#`.
- **Tests**: fill in `void validate()` with `assert(...)` per case (same
  coverage as the Python file's `validate()`, plus the same edge cases),
  ending with `std::cout << "SUCCESS" << std::endl;`. `main()` should
  contain only `validate(); return 0;` — no debug output, matching the
  Python side's Step 4 rule.

```cpp
// Space - Time Complexity analysis:
// space: O(n) - dict can grow to hold up to n entries
// time: O(n) - single pass, O(1) average unordered_map lookup/insert

std::vector<int> two_sum(const std::vector<int>& nums, int target) {
    ...
}

// Tests:
void validate() {
    ...
    std::cout << "SUCCESS" << std::endl;
}

int main() {
    validate();
    return 0;
}
```

Keep function names identical to the Python file's (`two_sum_ugly`,
`two_sum`, etc.) so the two languages read as direct translations of each
other, not divergent implementations.

## Step 6 — Verify both

Python — these filenames start with a digit and can't be imported
normally, load by path and call `validate()` directly:

```python
import importlib.util
spec = importlib.util.spec_from_file_location("task", "python/<number>_whatever.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
mod.validate()
```

C++ — compile with warnings on and run the binary:

```bash
g++ -std=c++20 -Wall -Wextra c++/<number>_whatever.cpp -o /tmp/<name> && /tmp/<name>
```

Both must print `SUCCESS`, and the C++ compile must produce no warnings.
If either doesn't, fix the actual bug before reporting back — don't hand
over something that fails its own tests.

## Step 7 — Report back

Briefly: which two files, which function(s) written in each, and their
complexities. State them as plain facts, not as fixes or corrections to
what was there before — no "was wrong, now it's...", just what it is.
Keep it to a few lines — the files are the deliverable.
