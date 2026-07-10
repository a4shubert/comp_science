---
name: next
description: >
  Generate the next interview-prep coding task file in this repo (Man Group /
  AHL Quant Developer pair-programming prep), following the numbered
  N_topic.py convention established in this repo. Use this whenever the user
  asks for "the next task", "next question", says they've finished a problem
  and want another, or invokes "/next" (optionally with a topic
  override, e.g. "/next heaps"). Progresses gradually through a
  DS&A + NumPy/Pandas roadmap rather than jumping straight to hard problems.
---

# next

Generate the next practice-interview task file for this repo, in the same
format as the existing `N_*.py` files, and hand it back for the user to
solve — you write the task, they write the solution, you review later.

## Why this format

The user is prepping for a live pair-programming interview (Man Group / AHL
Quant Developer — Stage 1 is a 1.5h HackerRank pair-programming session,
Stage 2 is DS&A + code review). The point of each generated file is
practice, not a memory test: task descriptions should hint at the relevant
stdlib/NumPy/Pandas/SciPy tool by *name only* — e.g. `dict`, `heapq`,
`bisect`, `collections.deque`, `.rolling()` — not by describing the
algorithm or technique that uses it. Naming the tool is recall practice;
describing the approach (e.g. "use a sliding window with two pointers,
tracking last-seen index in a dict so you can jump left directly") hands
over the solution shape, which defeats the point. Never include example
code or pseudocode snippets in the hint (e.g. `set(s[i:j])`) — that's
already a partial solution, not a pointer to a tool.

Keep hints to this shape: one line for the brute-force tool, one line for
the optimized tool, labeled "Ugly way:" / "Right way:". Each line can carry
a short clause of extra framing beyond the bare tool name (e.g. "list (as a
stack) - push as you go, check against what's on top") as long as it still
names the *tool*, not the algorithm's steps — a dash-clause naming what the
tool is *for* is fine, a clause that walks through the steps of the
solution is not. Don't add a generic best-practice callout (e.g. "state
your complexity out loud before optimizing") — that boilerplate got
repetitive across files and was cut; only include a best-practice note if
it's specific to *this* task's algorithm (e.g. two-sum's "check before you
insert, so you don't pair an element with itself").

## Step 1 — Find the next file number

List files in `python/` (this repo also has a sibling `c++/` folder for
the same kind of practice in C++ — this skill is Python-only, don't touch
`c++/`) matching `[0-9]*_*.py` and take the highest leading integer `N`.
The new file is `python/(N+1)_<topic_slug>.py`. If none exist, start at `1`.

## Step 2 — Pick the next topic

If the user gave an explicit topic (e.g. `/next heaps`), use that.

Otherwise, read the `# Task:` header of each existing numbered file to see
which topics from the roadmap below are already covered, and pick the next
uncovered one in order. Progress gradually — don't jump to a hard topic
just because it's next on the list if the last couple of problems were
trivial for the user; use your judgment from how the review conversation
went (if you have that context), but default to roadmap order.

Roadmap (adjust/reorder if the user's actual progress suggests otherwise —
this is a guide, not a hard contract):

1. Warm-ups: recursion/iteration (factorial, Fibonacci)
2. Arrays & hashing (two-sum style, frequency counting — `dict`, `set`,
   `collections.Counter`)
3. Two pointers / sliding window (string & array problems)
4. Stacks & queues (parsing/matching — `collections.deque`)
5. Searching & sorting (`bisect`, custom `sort`/`sorted` keys)
6. Recursion → DP (memoization via `functools.lru_cache`, then manual
   tabulation)
7. Heaps (`heapq` — priority-queue / streaming problems)
8. NumPy/Pandas: vectorization vs. explicit loops, `.rolling()`, `.groupby()`
9. Design/code-review flavored (LRU cache, simplified order book) — this
   one may want a stub `class Solution:` rather than a bare function

Once you reach the end of the roadmap, either loop back for a harder
variant of an earlier category, or ask the user what they want next.

## Step 3 — Write a Theory primer

Before the `# Task:` section, write a `# Theory:` block: roughly 100 words
of educational background on the underlying concept/data structure/
technique this task is built on — not a hint about *this specific*
problem, but the general knowledge a candidate should already have walking
in (e.g. what a heap is and why it's O(log n), what makes hash maps O(1)
average, why sliding window is O(n) instead of O(n^2)/O(n^3)). This is the
"why does this tool exist and what's the tradeoff" context; the Hint
section further down stays specific to this problem. See
`8_kth_largest.py`'s Theory section for a concrete example of the length
and tone to match.

## Step 4 — List relevant Packages

After Theory, before Task, write a `# Packages:` block: a broader,
comprehensive list of stdlib (or NumPy/Pandas/SciPy, where relevant)
functions/modules useful for *this category* of problem — not just the
two specific tools named in the Hint below. Where the Hint says "here are
the two approaches for this exact problem," Packages says "here's the
full toolbox for this class of problem," so the user builds a wider
mental index of what's available, not just what this one task needs.

One line per entry, name + one-line description of what it's for, e.g.
(from a hashing/arrays task):

```
# Packages:
## dict - hash map, average O(1) lookup/insert/delete
## collections.Counter - frequency counting, dict subclass with default 0
## collections.defaultdict - dict with an automatic default value/factory
## itertools.combinations - generate all k-element combinations of a sequence
```

Aim for comprehensiveness over the minimum — list every function/module a
candidate might reach for on this category of problem, even ones the
Hint's two approaches don't use directly (e.g. for a searching/sorting
task, list `bisect.insort` and `functools.cmp_to_key` alongside
`bisect_left`/`bisect_right` even if the solutions only need the latter
two).

## Step 5 — Write the file

Use this exact structure (matches `1_factorial.py`, `2_fibonacci.py`,
`3_two_sum.py` in this repo — read one of them if you want a concrete
reference):

```python
# Theory:
## <~100 words of educational background per Step 3 above>


# Packages:
## <broad list per Step 4 above, one function/module per line>


# Task:
## <clear problem statement, including any convention/edge-case assumptions
## worth stating explicitly, e.g. indexing convention or "assume exactly one
## valid answer">
## Test1: Inputs: <param = value, param = value>   Outputs: <expected return value>
## Test2: Inputs: <param = value, param = value>   Outputs: <expected return value>
## Test3: Inputs: <param = value, param = value>   Outputs: <expected return value>
## Hint:
## Ugly way: <tool name, optionally + a short dash-clause on what it's for,
## e.g. "str.replace in a loop - repeatedly strip matched pairs until
## nothing changes">
## Right way: <tool name, optionally + a short dash-clause, e.g.
## "list (as a stack) - push opening brackets, check closers against the
## top">
## <only include a best-practice line if it's specific to this task's
## algorithm, not a generic "state your complexity out loud" boilerplate>


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def <function_name>_ugly(<params>):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def <function_name>(<params>):
    return <function_name>_ugly(<params>)
```

Include up to 3 worked examples as `## Test1:` / `## Test2:` / `## Test3:`
lines right in the Task section, each with `Inputs:` (every parameter,
named, e.g. `nums = [2, 7, 11, 15], target = 9`) and `Outputs:` (the exact
expected return value) — the same concrete style LeetCode-type problem
statements use, so the user can see the shape of a correct answer before
writing any code. These should be a subset of (or consistent with) the
cases you'll also put in `validate()` further down, not invented
separately — one source of truth for what "correct" means on this task.

Stub **both** functions from the start whenever the hint names two
approaches (an "Ugly way" and a "Right way") — `<function_name>_ugly` for
the brute-force tool, `<function_name>` for the optimized one — matching
the naming already used in `3_two_sum.py` and `5_valid_parentheses.py`.
Only stub a single function if the hint genuinely only names one approach.

The optimized function's stub body delegates to the `_ugly` one instead of
`pass` (matching `7_climbing_stairs.py`) — that way, once the user finishes
just the brute-force version, `validate()`'s loop over both functions
already passes end to end, since the optimized one is temporarily just
forwarding to the working one. They replace the delegating body with the
real optimized logic afterward, once the ugly version is confirmed
correct — same problem, staged in two passes instead of blocked until
both are done at once.

Note the section header is `# Solutions:` (plural), with a blank line
after it before the first function — and each function's
`# Space - Time Complexity analysis:` block goes *above* that function,
not below it, so the complexity is the first thing read before the code
that produces it. Leave the `## space:` / `## time:` lines blank (matching
`7_climbing_stairs.py`) — this is the user's own analysis to write, not
yours to fill in when generating the task.

(If the task is naturally class-shaped — e.g. an LRU cache or order book —
stub a `class Solution:` with `pass`-bodied methods instead, same idea:
the file must compile standalone with nothing implemented yet, and each
method that has a meaningfully different complexity gets its own analysis
block above the class rather than inline per-method.)

```python

# Tests:
def validate():
    <a handful of concrete test cases via assert, comparing against
    known-correct expected values you computed yourself — not against the
    unimplemented function(s)>
    for fn in (<function_name>_ugly, <function_name>):
        for ...:
            <run fn on each case and assert>
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(<function_name>_ugly(<first test case's input, unpacked as real args>))
```

Wire `validate()` to loop over both stubs from the start (same shape as
`3_two_sum.py`/`5_valid_parentheses.py`'s `for fn in (..._ugly, ...):`
loop). It'll fail until `_ugly` is actually implemented (the optimized
one just delegates to it, so both fail together, then both pass together
once `_ugly` is done) — expected, same as any unsolved file failing
`validate()`.

`print("SUCCESS")` must be the last line of `validate()`, after all
asserts — since a failed assert raises immediately, this only prints when
every case passes.

Leave `validate()` commented out in `__main__` and call the `_ugly`
function directly on the first test case's input instead (not the
optimized one) — that's the user's debugging workflow: start by getting
the brute-force version working and observable, same order they're meant
to tackle the problem in. Match the args to whatever `<function_name>_ugly`
actually takes — e.g. `print(two_sum_ugly([2, 7, 11, 15], 9))` for a
two-arg function.

## Step 6 — Verify it compiles

Run `python3 -m py_compile <new_file>` before finishing. It's expected to
fail `validate()` at this point (the solution is unimplemented `pass`) —
that's fine. It must not have a `SyntaxError`.

## Step 7 — Report back

Tell the user: which file was created, a one-line description of the task,
and a one-line reason it's next in the progression (e.g. "first sliding
window problem, natural follow-up to the hashing pattern from two-sum").
Keep it brief — the file itself is the deliverable, not the summary.
