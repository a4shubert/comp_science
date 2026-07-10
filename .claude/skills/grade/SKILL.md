---
name: grade
description: >
  Grade/review a specific numbered interview-prep task file in this repo,
  e.g. "grade 4" (searches all topic folders) or "grade 2_ds/3"
  (folder-qualified, unambiguous). Use this whenever the user says "grade
  <number>", "grade <folder>/<number>", "review <number>", or asks you to
  check/grade a specific numbered task file. Runs the file's tests, checks
  the complexity analysis against the real implementation, checks whether
  the optimized function actually uses the hinted library tool (not a
  hand-rolled reimplementation), and reviews code quality — same standard
  as manual reviews done elsewhere in this session, just triggered by
  number.
---

# grade

Grade the `<number>_*.py` task file the user names, the same way you'd
review it manually mid-conversation: verify correctness by actually running
it, check whether the stated complexity analysis matches the real
implementation, and flag code-quality issues. Don't rewrite their solution
for them — this is a review, not a fix, unless they separately ask you to
patch something.

This repo is Python-only (there used to be a mirrored `c++/` tree, but it
was deleted). It's split into topic folders — `python/1_core/`,
`python/2_ds/`, `python/3_algo/`, `python/numpy/`, `python/scipy/`,
`python/pandas/` — each numbered independently from 1, so a bare number is
ambiguous.

## Step 1 — Locate the file

If the user gave a folder-qualified argument (`2_ds/3`, `2_ds 3`, etc.), go
straight to `python/<folder>/<number>_*.py`. Otherwise, search
`python/1_core/`, `python/2_ds/`, `python/3_algo/`, `python/numpy/`,
`python/scipy/`, `python/pandas/` for a file matching `<number>_*.py`. If
it matches in exactly one folder, proceed. If it matches in more than one,
list the matches and ask which one they mean rather than guessing.

## Step 2 — Run it for correctness

`validate()` is intentionally left commented out of `__main__` (the user's
debugging convention — they call the function directly on one case instead
while working on it). To grade correctness you need to call `validate()`
yourself, not just run the file as-is. Since these filenames start with a
digit, they can't be imported as normal Python modules — load by path
instead:

```python
import importlib.util
spec = importlib.util.spec_from_file_location("task", "python/<folder>/<number>_whatever.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
mod.validate()
```

For `numpy/`/`scipy`/`pandas/` tasks, those packages may not be installed
in this environment — if the import itself fails, install them (e.g. via a
venv) before concluding the solution is broken.

- If it prints `SUCCESS` cleanly: correctness passes.
- If an `assert` fails: report which specific case failed and what the
  assertion message says.
- If some other exception fires (`TypeError`, `RecursionError`, an
  unhandled edge case, etc.): report it plainly — that's real signal, not
  noise to smooth over.

If the file defines multiple solution variants (e.g. an "ugly" and an
optimized version, matching the task's Ugly-way/Right-way hint), confirm
`validate()` actually exercises all of them, not just one.

## Step 3 — Check the complexity analysis

Read the `# Space - Time Complexity analysis:` section and reason through
the actual implementation yourself — don't just trust what's written.
Walk through what grows with input size (data structures allocated, max
recursion/stack depth, number of operations) versus what's fixed.

If their stated complexity is correct, say so plainly. If it's wrong, don't
just hand over the right answer — ask the same kind of guiding question
used throughout this session (e.g. "what happens to X as n grows — does it
scale with n, or stay fixed?", "how many total calls happen here versus how
many are on the stack at once?"). Save direct explanations for cases where
they're clearly stuck or ask for one outright, same as the rest of this
session's tutoring style.

## Step 4 — Code quality pass

Look for things like:
- Leftover debug prints or commented-out dead code
- Inconsistent edge-case handling between sibling functions (e.g. one
  variant guards against negative input, another doesn't)
- Whether the optimized function actually calls the tool the "Right way:"
  hint names (e.g. `numpy.cumsum`, `heapq`, `bisect_left`) — a hand-rolled
  reimplementation that happens to hit the same complexity is still a red
  flag, not a pass; the point is demonstrating the library call
- Unused imports or variables
- Anything that would read as a red flag in a live pair-programming
  interview — mainly, does the code and its stated complexity together
  tell an honest story about what it does

## Step 5 — Report

Give a concise grade summary, not a lecture:

```
Correctness: <pass/fail + detail>
Complexity analysis: <correct / question(s) to reconsider>
Code quality: <brief notes, or "nothing notable">
```

Keep it tight — this mirrors the manual review style already used in this
session, just entered via "grade <number>" instead of "review".
