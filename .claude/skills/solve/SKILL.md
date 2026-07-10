---
name: solve
description: >
  Write a complete, correct solution for a specific numbered interview-prep
  task, in Python, e.g. "solve 6" (searches all topic folders) or "solve
  2_ds/3" (folder-qualified, unambiguous) implements the matching
  python/<folder>/N_whatever.py properly. Use this whenever the user says
  "solve <number>" or "solve <folder>/<number>", asks you to
  implement/fix/finish a specific numbered task, or wants you to write the
  answer yourself rather than write it themselves. Fills in the Solutions,
  per-line space|time comments, a Space - Time Complexity analysis block
  above each function, and tests - to the same standard used throughout
  this repo (see python/1_core/1_factorial.py, python/1_core/3_two_sum.py).
---

# solve

Write the real solution for the task the user names — not a hint, not a
stub, the actual working implementation, commented the way every other
solved file in this repo is commented. This is the opposite mode from
normal practice (where the user writes and you review/grade) — here
they're explicitly asking you to do the writing.

This repo is Python-only (there used to be a mirrored `c++/` tree, but it
was deleted — don't create or reference C++ files). It's split into topic
folders: `python/1_core/`, `python/2_ds/`, `python/3_algo/`,
`python/numpy/`, `python/scipy/`, `python/pandas/`. Each folder numbers its
own files independently starting from 1, so a bare number like `solve 3` is
ambiguous — it could match `1_core/3`, `2_ds/3`, `3_algo/3`, `numpy/3`,
`scipy/3`, or `pandas/3` all at once.

## Step 1 — Locate the file and read the task

If the user gave a folder-qualified argument (`2_ds/3`, `2_ds 3`, `numpy/2`,
etc.), go straight to `python/<folder>/<number>_*.py`. Otherwise, search
`python/1_core/`, `python/2_ds/`, `python/3_algo/`, `python/numpy/`,
`python/scipy/`, `python/pandas/` for a file matching `<number>_*.py`. If
it matches in exactly one folder, proceed. If it matches in more than one,
list the matches (e.g. "found 2_ds/3_number_of_islands.py and
3_algo/3_three_sum.py — which one?") and ask rather than guessing.

Read the file's `# Task:` / `# Hint:` section — the hint names tools by
"Ugly way:" / "Right way:" (e.g. "nested loops" vs "dict"). Implement
**both** named approaches as separate functions when the hint gives two,
matching the pattern in `1_core/3_two_sum.py` (`two_sum_ugly` / `two_sum`)
and `1_core/5_valid_parentheses.py` (`is_valid_ugly` / `is_valid`) — the
point of keeping both is comparing complexity, not just shipping the fast
one.

The optimized function **must actually call** whatever tool the "Right
way:" line names — `numpy.cumsum`, `bisect_left`, `heapq`, `pandas.merge`,
whatever it says — not a hand-rolled reimplementation of the same idea in
plain Python. If the Hint says "Right way: numpy.cumsum" and the function
is a hand-written prefix-sum loop instead, that's not solved correctly,
even if it's O(n) and passes the tests — the whole point of the optimized
version is demonstrating the library call, not just hitting the right
complexity by coincidence. This matters most for the numpy/scipy/
pandas-flavored tasks, where "the right way" specifically means the
vectorized library call, not a fast-but-manual Python equivalent. (numpy,
scipy, and pandas may not be installed in this environment — if imports
fail when verifying in Step 5, install them into the repo's `.venv` (see
`requirements.txt`) rather than falling back to a pure-Python
reimplementation to dodge the missing dependency.)

If the file already has a partial/buggy attempt in it, you don't need to
preserve its structure — write it properly, the way you would in a review
where you'd flag it as needing a real fix rather than a patch. Don't leave
dead code, shadowed builtins/names, or unhandled edge cases (e.g. empty
input, input with no valid answer) that a live interviewer would flag.

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
`1_core/7_climbing_stairs.py`), with a `## space:` line and a `## time:` line,
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

## Step 5 — Verify

These filenames start with a digit and can't be imported normally, load
by path and call `validate()` directly:

```python
import importlib.util
spec = importlib.util.spec_from_file_location("task", "python/<folder>/<number>_whatever.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
mod.validate()
```

Must print `SUCCESS`. If it doesn't, fix the actual bug before reporting
back — don't hand over something that fails its own tests.

## Step 6 — Report back

Briefly: which file, which function(s) written, and their complexities.
State them as plain facts, not as fixes or corrections to what was there
before — no "was wrong, now it's...", just what it is. Keep it to a few
lines — the file is the deliverable.
