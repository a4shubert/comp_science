# A Practical Tour of Data Structures, Algorithms, and the Python Numerical Stack

This is a from-scratch course built out of a pair-programming interview-prep
exercise. Every topic below corresponds to a real, runnable file in this
repository (`python/1_core/`, `python/2_ds/`, `python/3_algo/`,
`python/numpy/`, `python/scipy/`, `python/pandas/`), and every code snippet
here either *is* that file's finished solution, or — for the topics still
left as practice exercises — a clean illustration of the technique the
exercise is built around. Read this document top to bottom for the full
course, or jump to a chapter for a specific topic.

The organizing idea throughout is the same one every file in this repo is
built on: **for a given problem, there is an "ugly way" (correct, usually
the first thing you'd think of, often a hand-rolled loop) and a "right way"
(the same result, produced by reaching for the correct tool — a data
structure, a standard-library function, or a vectorized numerical
library)**. Learning to recognize *which tool* a problem is asking for is
the actual skill being taught here — not just getting the right answer, but
getting it the way an experienced engineer would.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt   # numpy, scipy, pandas
```

## Table of contents

**Part I — Foundations**
1. [Recursion, Memoization, and the Cost of Repeated Work](#chapter-1)
2. [Hashing and the Space-Time Tradeoff](#chapter-2)
3. [Two Pointers and Sliding Windows](#chapter-3)
4. [Stacks and Matching Structures](#chapter-4)
5. [Binary Search](#chapter-5)
6. [Dynamic Programming I: Optimal Substructure](#chapter-6)
7. [Heaps and Priority Queues](#chapter-7)
8. [Vectorization: Why NumPy Exists](#chapter-8)

**Part II — Functional Programming**

9. [Composition, Partial Application, and Folds](#chapter-9)

**Part III — Object-Oriented Design**

10. [Polymorphism, Encapsulation, and Interfaces](#chapter-10)

**Part IV — Generators, Decorators, and the Standard Library**

11. [Generators and Iterators](#chapter-11)
12. [Decorators](#chapter-12)
13. [Context Managers](#chapter-13)
14. [Standard Library Deep Cuts](#chapter-14)

**Part V — Data Structures**

15. [Linked Lists](#chapter-15)
16. [Trees and Breadth-First Search](#chapter-16)
17. [Graphs I: Grids as Implicit Graphs](#chapter-17)
18. [Tries](#chapter-18)
19. [Union-Find](#chapter-19)
20. [Amortized Analysis](#chapter-20)

**Part VI — Algorithms**

21. [Sorting](#chapter-21)
22. [Two Pointers at Scale](#chapter-22)
23. [Backtracking](#chapter-23)
24. [Greedy Algorithms](#chapter-24)
25. [Graphs II: Shortest Paths](#chapter-25)
26. [Dynamic Programming II](#chapter-26)
27. [Bit Manipulation](#chapter-27)

**Part VII — The Numerical Stack**

28. [NumPy](#chapter-28)
29. [SciPy](#chapter-29)
30. [Pandas](#chapter-30)

**Appendices**
- [A. Tool Cheat Sheet](#appendix-a)
- [B. Repo Map and How to Keep Practicing](#appendix-b)

---

# Part I — Foundations

<a id="chapter-1"></a>
## Chapter 1: Recursion, Memoization, and the Cost of Repeated Work

*Files: `python/1_core/1_factorial.py`, `python/1_core/2_fibonacci.py`*

### 1.1 Factorial: recursion vs. iteration

Every recursive function has two parts: a **base case** (the smallest input
you can answer directly, without recursing) and a **recursive case** (how
to reduce a bigger input to a smaller one you already know how to solve).
Factorial's base case is `0! = 1`; its recursive case is `n! = n * (n-1)!`.
Recursion mirrors that mathematical definition almost line for line, which
is exactly why it reads so cleanly — but each call it makes waits on the
stack for the one below it to return, so computing `n!` recursively costs
O(n) stack space. An iterative loop computes the same product by walking
upward from 1 to n, using a single accumulator variable — O(1) space, same
O(n) time.

```python
def factorial_ugly(n):          # recursive - O(n) call-stack space
    if n <= 1:
        return 1
    return n * factorial_ugly(n - 1)

def factorial(n):               # iterative - O(1) space
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

The general lesson: recursion is often the *clearest* way to state a
solution, but every recursive call has a real memory cost (a stack frame)
that an equivalent loop doesn't pay. Whenever a recursive function is only
ever "waiting" on one pending call (not branching into multiple), it can
almost always be rewritten iteratively to trade that O(depth) space for
O(1).

### 1.2 Fibonacci: from exponential recursion to memoization

Naive recursive Fibonacci (`fib(n) = fib(n-1) + fib(n-2)`) looks just as
clean as factorial, but it hides a trap: `fib(n-1)` and `fib(n-2)` each
recursively recompute overlapping subproblems — `fib(5)` calls `fib(3)`
twice, `fib(2)` three times, and so on. The number of calls roughly doubles
per level of `n`, giving **O(2^n)** time, despite there only being `n`
*distinct* subproblems.

**Memoization** fixes this by caching each subproblem's result the first
time it's computed, so every subsequent call with the same argument is an
O(1) cache lookup instead of a re-computation. Python's `functools.lru_cache`
adds this caching to any pure function with one decorator line:

```python
import functools

def fibonacci_ugly(n):                     # O(2^n) time, O(n) stack space
    if n <= 1:
        return n
    return fibonacci_ugly(n - 1) + fibonacci_ugly(n - 2)

@functools.lru_cache(maxsize=None)
def fibonacci(n):                           # O(n) time, O(n) cache + stack
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

This is the first appearance of a pattern the rest of this course returns
to constantly: **trading space for time**. The memoized version holds onto
every subproblem's answer (O(n) extra space) so it never re-derives one
(O(n) time instead of O(2^n)). Recognizing when a recursive tree has
*overlapping subproblems* (as opposed to genuinely independent branches,
like the permutations in Chapter 23) is what tells you memoization applies
at all.

---

<a id="chapter-2"></a>
## Chapter 2: Hashing and the Space-Time Tradeoff

*File: `python/1_core/3_two_sum.py`*

A **hash map** (Python's `dict`) gives average O(1) insertion, lookup, and
deletion by computing a hash of the key and using it to jump almost
directly to the right storage bucket, instead of scanning. This is the
single most important data structure for turning an O(n²) brute-force
scan into an O(n) pass, and Two Sum is the canonical example.

The brute-force approach checks every pair of numbers for one that sums to
the target — two nested loops, O(n²) time, O(1) extra space:

```python
def two_sum_ugly(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```

The hashing approach walks the array *once*, and for each number asks "have
I already seen the value that would complete this pair?" — a question a
dict answers in O(1) average time:

```python
def two_sum(nums, target):
    seen = {}                        # value -> index
    for i, v in enumerate(nums):
        complement = target - v
        if complement in seen:
            return [seen[complement], i]
        seen[v] = i
    return []
```

The key move, worth internalizing: check **before** you insert, not after —
otherwise an element could pair with itself. This "have I seen X" /
"remember X for later" shape recurs constantly (duplicate detection,
frequency counting via `collections.Counter`, grouping via
`collections.defaultdict`) — whenever a brute-force solution is repeatedly
*searching* a collection, ask whether a hash map could make that search
O(1) instead.

---

<a id="chapter-3"></a>
## Chapter 3: Two Pointers and Sliding Windows

*File: `python/1_core/4_longest_substring.py`*

A **sliding window** maintains a contiguous range `[left, right]` over a
sequence and grows or shrinks it incrementally, rather than
re-examining every possible substring from scratch. It's the standard tool
whenever a problem asks for the best contiguous run satisfying some
condition (longest, shortest, max sum, etc.) — because as `right` advances
one step, the state describing the window (a character-to-last-seen-index
map, in this problem) only needs a small, incremental update, not a full
recomputation.

The brute-force approach checks every substring for the "no repeated
characters" property — O(n²) or worse:

```python
def longest_substring_ugly(s):
    best = 0
    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            best = max(best, j - i + 1)
    return best
```

The sliding window approach tracks the last index each character was seen
at; when a repeat is found *inside* the current window, it jumps `left`
directly past the previous occurrence instead of shrinking one step at a
time:

```python
def longest_substring(s):
    last_seen = {}                       # char -> most recent index
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        best = max(best, right - left + 1)
    return best
```

This runs in O(n) time — each index is visited by `right` exactly once,
and `left` only ever moves forward. The general recipe: **two pointers
bounding a window, plus a hash map summarizing what's currently inside
it**, updated incrementally as the window slides. Three Sum (Chapter 22)
uses a related but distinct two-pointer idea — pointers converging from
both ends of a *sorted* array rather than one window sliding forward.

---

<a id="chapter-4"></a>
## Chapter 4: Stacks and Matching Structures

*File: `python/1_core/5_valid_parentheses.py`*

A **stack** is a Last-In-First-Out (LIFO) structure: you can only push
onto, or pop from, one end. That restriction is exactly what makes it the
right tool for matching nested structure — brackets, parentheses, HTML
tags, function call frames — because the most recently opened thing must
be the next thing closed, which is precisely LIFO order.

The brute-force approach repeatedly finds and removes any adjacent matched
pair (`()`, `[]`, `{}`) until nothing more can be removed, then checks if
the string is empty — correct, but each removal pass rescans the whole
(shrinking) string:

```python
def is_valid_ugly(s):
    prev = None
    while prev != s:
        prev = s
        for pair in ("()", "[]", "{}"):
            s = s.replace(pair, "")
    return s == ""
```

The stack approach processes the string in a single left-to-right pass:
push every opening bracket; on a closing bracket, check that it matches
whatever is on *top* of the stack (the most recently opened, still-unclosed
bracket) and pop it:

```python
def is_valid(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in pairs.values():
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack
```

O(n) time, one pass, versus a brute-force approach that can degrade toward
O(n²) as it repeatedly rescans a slowly-shrinking string. Any time a
problem's correctness depends on "the most recent unmatched/unclosed thing"
— parsing expressions, undo history, DFS via an explicit stack instead of
recursion — reach for a stack first.

---

<a id="chapter-5"></a>
## Chapter 5: Binary Search

*File: `python/1_core/6_search_range.py`*

Binary search exploits **sorted order**: given a sorted sequence, you can
find a target (or the boundary where it would belong) by repeatedly
halving the search range — check the midpoint, and discard the half that
can't possibly contain the answer — in O(log n) time instead of O(n) for a
linear scan. This is the single biggest complexity win available whenever
"the data is sorted" is true or can be made true cheaply (e.g. sort once,
then answer many queries in O(log n) each).

The brute-force approach for "first and last position of a target" scans
linearly for both boundaries:

```python
def search_range_ugly(nums, target):
    first = last = -1
    for i, v in enumerate(nums):
        if v == target:
            if first == -1:
                first = i
            last = i
    return [first, last]
```

Python's `bisect` module implements binary search directly.
`bisect_left(nums, target)` finds the leftmost position where `target`
could be inserted keeping the list sorted (which, if `target` is present,
is its first occurrence); `bisect_right` finds the position just past its
last occurrence:

```python
import bisect

def search_range(nums, target):
    left = bisect.bisect_left(nums, target)
    if left == len(nums) or nums[left] != target:
        return [-1, -1]
    right = bisect.bisect_right(nums, target) - 1
    return [left, right]
```

Two calls to `bisect`, O(log n) each, versus one O(n) scan. `bisect.insort`
(insert into a sorted list, keeping it sorted, in O(n) due to the shift but
O(log n) to *find* the position) and `functools.cmp_to_key` (custom sort
comparators) round out the toolbox for this category.

---

<a id="chapter-6"></a>
## Chapter 6: Dynamic Programming I: Optimal Substructure

*File: `python/1_core/7_climbing_stairs.py`*

**Dynamic programming (DP)** applies when a problem has two properties:
*optimal substructure* (the answer to a big instance can be built from
answers to smaller instances of the *same* problem) and *overlapping
subproblems* (those smaller instances repeat, so caching them pays off —
exactly the Fibonacci situation from Chapter 1). Climbing Stairs (count the
number of ways to climb n stairs, taking 1 or 2 steps at a time) is
Fibonacci wearing a different costume: `ways(n) = ways(n-1) + ways(n-2)`,
because the last step taken was either a 1-step (leaving `ways(n-1)` ways
to have gotten to the step before) or a 2-step (leaving `ways(n-2)`).

```python
def climbing_stairs_ugly(n):              # naive recursion - O(2^n)
    if n <= 2:
        return n
    return climbing_stairs_ugly(n - 1) + climbing_stairs_ugly(n - 2)

def climbing_stairs(n):                   # bottom-up DP - O(n) time, O(1) space
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        prev2, prev1 = prev1, prev2 + prev1
    return prev1
```

This version doesn't even need `functools.lru_cache` — it builds the
answer **bottom-up**, from the smallest subproblem up to `n`, keeping only
the last two values instead of a full table. That's the general DP
refinement path: naive recursion (exponential) → top-down memoization
(cache results, still recursive) → bottom-up tabulation (an explicit loop,
often reducible to O(1) space if each step only needs a fixed window of
previous results, as here). Longest Common Subsequence (Chapter 26) is the
same idea one dimension up, where the "table" genuinely needs to stay 2D.

---

<a id="chapter-7"></a>
## Chapter 7: Heaps and Priority Queues

*File: `python/1_core/8_kth_largest.py`*

A **heap** is a tree-shaped structure that keeps one element — the
minimum (in a min-heap) or maximum (in a max-heap) — accessible in O(1),
with O(log n) insertion and removal. It's the standard tool for "give me
the smallest/largest thing right now" when the underlying set keeps
changing, which is exactly what a fully-sorted structure would be overkill
for. Python's `heapq` module implements a **min-heap** on top of a plain
list.

Finding the kth largest element by fully sorting is correct but does more
work than needed — sorting orders *everything*, when only one position
matters:

```python
def kth_largest_ugly(nums, k):
    return sorted(nums, reverse=True)[k - 1]     # O(n log n)
```

The heap approach keeps a min-heap of only the k largest elements seen so
far: push each new number, and if the heap grows past size k, pop the
smallest (evicting it from contention). After processing every element,
the heap's minimum — the top of a min-heap — *is* the kth largest overall,
because everything smaller than it has already been evicted:

```python
import heapq

def kth_largest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]
```

O(n log k) time — each of the n elements does at most one O(log k) push/pop
against a heap that never grows past size k — versus O(n log n) for a full
sort, which matters a great deal when k is small and n is large. This same
"min-heap of the k best candidates seen so far" shape is the standard
approach to any streaming top-k problem, and reappears as the core move
inside Dijkstra's algorithm (Chapter 25), where the heap tracks "closest
unvisited node" instead of "kth largest value."

---

<a id="chapter-8"></a>
## Chapter 8: Vectorization: Why NumPy Exists

*File: `python/1_core/9_rolling_average.py`*

This chapter is the bridge into Part VII. A **rolling (moving) average**
over a window of size `w` — the average of the last `w` values at every
position — looks innocent, but computing each window's sum from scratch is
O(n·w). The key insight for doing better: consecutive windows overlap in
all but two elements, so if you have a **prefix sum** array (`prefix[i]` =
sum of the first `i` elements), any window's sum is just one subtraction:
`prefix[right] - prefix[left]`.

```python
def rolling_average_ugly(prices, w):             # O(n*w)
    result = []
    for i in range(len(prices) - w + 1):
        result.append(sum(prices[i:i + w]) / w)
    return result

import numpy as np

def rolling_average(prices, w):                  # O(n)
    arr = np.array(prices, dtype=float)
    prefix = np.cumsum(np.insert(arr, 0, 0))
    window_sums = prefix[w:] - prefix[:-w]
    return (window_sums / w).tolist()
```

`numpy.cumsum` computes the entire prefix-sum array in one vectorized C
loop, and `prefix[w:] - prefix[:-w]` computes *every* window's sum at once
via array subtraction — no explicit loop over windows at all. This is the
core idea behind every NumPy/SciPy/Pandas chapter later in this course:
**push the loop down into compiled code operating on contiguous memory,
instead of running it as interpreted Python, one element at a time.** The
algorithmic complexity (O(n) either way, once you have the prefix-sum
insight) doesn't change — what changes is the constant factor, often by
100x or more, because a vectorized pass avoids per-element Python
interpreter overhead entirely. Chapters 28–30 explore this idea across
NumPy, SciPy, and Pandas in depth.

---

# Part II — Functional Programming

<a id="chapter-9"></a>
## Chapter 9: Composition, Partial Application, and Folds

*Files: `python/1_core/10_function_composition.py` through `14_lazy_prime_generator.py`*

Functional programming treats functions as data: they can be passed
around, combined, and built out of other functions, rather than always
being called directly by name. Python isn't a purely functional language,
but `functools` and `itertools` give you the core tools this style relies
on. The theme across this whole chapter is **`functools.reduce`** — Python's
general-purpose fold, which combines a sequence of values into one by
repeatedly applying a binary function, carrying an accumulator forward.
Once you see `reduce`, you'll notice it's the tool underneath several
seemingly different problems.

### 9.1 Function composition

`compose(f, g, h)` should return a single function equivalent to
`f(g(h(x)))` — each function's output feeding the next one's input,
right-to-left. The imperative version loops over the functions, reassigning
an accumulator:

```python
def compose_ugly(funcs):
    def composed(x):
        for f in reversed(funcs):
            x = f(x)
        return x
    return composed
```

`functools.reduce` expresses the same idea as a fold that builds up a
*chain of closures* instead of computing a value immediately — each
reduce step wraps the previous composed function inside a new one:

```python
import functools

def compose(funcs):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), funcs, lambda x: x)
```

Starting from the identity function `lambda x: x`, each step of the fold
produces `lambda x: f(g(x))` where `f` is everything composed so far and
`g` is the next function — so by the end, calling the result on `x` runs
every original function in the right order, right-to-left.

### 9.2 Partial application

Partial application fixes some of a function's arguments ahead of time,
producing a new, more specific function. `functools.partial` does this
directly:

```python
import functools

def specialize_ugly(fn, fixed_args):
    def specialized(*args):
        return fn(*fixed_args, *args)
    return specialized

def specialize(fn, fixed_args):
    return functools.partial(fn, *fixed_args)
```

`functools.partial(pow_fn, 2)` behaves exactly like the hand-written
closure — it's a reusable, introspectable object representing "`pow_fn`
with its first argument pinned to 2" — the idiomatic way to build a family
of specialized functions (e.g. `square = partial(power, exp=2)`) from one
general one.

### 9.3 Running accumulation

A running/prefix reduction — e.g. the running maximum seen so far at each
position — is `itertools.accumulate`'s job. It's a *lazy fold* that yields
every intermediate result, not just the final one:

```python
import itertools

def running_maximum_ugly(nums):
    result = []
    running_max = None
    for x in nums:
        running_max = x if running_max is None else max(running_max, x)
        result.append(running_max)
    return result

def running_maximum(nums):
    return list(itertools.accumulate(nums, max))
```

`accumulate`'s default combining function is addition (a running total);
passing `max` (or any two-argument function) generalizes it to any running
reduction.

### 9.4 Pipelines

A **pipeline** is the mirror image of composition: apply a sequence of
functions to a value in order, left to right — `value | f | g | h`, like a
Unix shell pipe. Same `reduce` shape, just with the combining function
flipped:

```python
import functools

def pipe_ugly(value, funcs):
    for f in funcs:
        value = f(value)
    return value

def pipe(value, funcs):
    return functools.reduce(lambda acc, f: f(acc), funcs, value)
```

### 9.5 Laziness: generators and `itertools.islice`

Lazy evaluation means computing values only as they're consumed, which
matters most for sequences with no natural stopping point — "the primes,"
for instance. A **generator function** (using `yield`) expresses an
infinite sequence directly, producing one value at a time and pausing in
between, so it never needs to hold more than one value in memory.
`itertools.islice` then takes a fixed number of items off the front of
that infinite generator — the lazy equivalent of slicing a list:

```python
import itertools, math

def _is_prime(candidate):
    if candidate < 2:
        return False
    return all(candidate % d for d in range(2, math.isqrt(candidate) + 1))

def _prime_stream():
    n = 2
    while True:
        if _is_prime(n):
            yield n
        n += 1

def first_n_primes(n):
    return list(itertools.islice(_prime_stream(), n))
```

The eager alternative — guess an upper bound, generate every candidate up
to it, filter for primality — either wastes work (bound too high) or
under-delivers (bound too low), and has to start over from scratch on
every failed guess. The generator sidesteps the guessing problem entirely:
it just keeps producing candidates until `islice` has taken enough.

---

# Part III — Object-Oriented Design

<a id="chapter-10"></a>
## Chapter 10: Polymorphism, Encapsulation, and Interfaces

*Files: `python/1_core/15_shape_polymorphism.py` through `19_abc_interface.py`*

Object-oriented design is fundamentally about **where behavior lives**.
The theme across every section in this chapter is the same trade: keeping
logic that varies by type *inside* each type's own class (so the type
"knows how to handle itself"), instead of centralizing it in one big
function that branches on type. The first version tends to be easier to
write quickly; the second scales better as the number of types grows,
because adding a new type never requires touching existing code.

### 10.1 Polymorphism

**Polymorphism** means calling the same method name on different types and
getting each type's own correct behavior, without the caller needing to
know which concrete type it's holding. The branching alternative —
`isinstance` checks dispatching to inline formulas — works, but couples
the caller to every type that exists today and silently fails to handle
new ones added later:

```python
def total_area_ugly(shapes):
    total = 0
    for s in shapes:
        if isinstance(s, Circle):
            total += math.pi * s.radius ** 2
        elif isinstance(s, Rectangle):
            total += s.width * s.height
    return total
```

`abc.ABC` with an `@abstractmethod` declares a contract every subclass
must fulfill; each subclass implements `area()` itself, and the caller
just invokes it polymorphically:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): ...

class Circle(Shape):
    def __init__(self, radius): self.radius = radius
    def area(self): return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height): self.width, self.height = width, height
    def area(self): return self.width * self.height

def total_area(shapes):
    return sum(s.area() for s in shapes)
```

Adding a `Triangle` now means writing one new class — `total_area` never
changes.

### 10.2 Operator overloading

Python lets a class respond to built-in syntax (`+`, `==`, `print(...)`) by
defining **dunder** (double-underscore) methods: `__add__` backs `+`,
`__eq__` backs `==`, `__repr__` controls how the object prints. Without
them, a class using `+` falls back to a `TypeError`, forcing callers to use
an awkward free function instead:

```python
class Vector2D:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return isinstance(other, Vector2D) and self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"
```

Once these are defined, `v1 + v2` and `v1 == v2` work directly, and every
future caller gets natural syntax "for free" — the class behaves
consistently everywhere it's used, including in assertions and print
statements.

### 10.3 Encapsulation via `@property`

**Encapsulation** hides an object's internal representation behind a
controlled interface. `@property` lets a method be accessed with plain
attribute syntax (`obj.value`, not `obj.value()`) while still running code
on every access — the natural tool when an attribute is *derived from*, or
must stay *in sync with*, other internal state:

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5 / 9
```

Without properties, keeping Celsius and Fahrenheit in sync requires every
caller to remember to call a conversion function on every update — a rule
enforced by convention, not by the language. With the setter, the sync
rule lives in exactly one place, no matter how many call sites update the
temperature.

### 10.4 Alternative constructors via `@classmethod`

A **classmethod** receives the class itself (conventionally `cls`) instead
of an instance, making it the natural home for "alternative constructor"
logic — building an instance from something other than `__init__`'s normal
signature:

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    @classmethod
    def from_string(cls, s):
        x_str, y_str = s.split(",")
        return cls(int(x_str), int(y_str))
```

Without it, parsing logic lives in a free function returning raw data (a
tuple), which the caller must then manually pass into the constructor
correctly, every time. `Point.from_string(s)` folds both steps into one
call that always returns a fully-formed, correct instance.

### 10.5 Enforced interfaces vs. duck typing

Python supports interfaces informally via **duck typing** ("if it has the
method, call it," checked with `hasattr`) or formally via `abc.ABC` +
`@abstractmethod`, which makes the contract enforced *by the language
itself*:

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process(self, amount): ...

class CreditCardProcessor(PaymentProcessor):
    def process(self, amount):
        return f"Charged ${amount} to credit card"
```

A subclass that doesn't implement `process` can't even be instantiated —
`TypeError` fires immediately at construction time, rather than an
`AttributeError` deep inside unrelated code much later, whenever that
particular method finally gets called. Duck typing is more flexible;
`abc.ABC` catches a missing implementation as early and as loudly as
possible, which matters most in a plugin-style system where new
implementations get added over time by people who might get it wrong.

---

# Part IV — Generators, Decorators, and the Standard Library

<a id="chapter-11"></a>
## Chapter 11: Generators and Iterators

*File: `python/1_core/20_flatten_generator.py`*

A generator function pauses its execution state at every `yield` and
resumes exactly there on the next request — the mechanism behind Chapter
9.5's infinite prime stream. `yield from` lets a generator delegate to
another iterable (including another generator) transparently, which is
exactly what a recursive structure like an arbitrarily nested list wants:

```python
def flatten_ugly(nested):                  # eager - builds the full result up front
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_ugly(item))
        else:
            result.append(item)
    return result

def flatten(nested):                       # lazy - one value at a time
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item
```

The eager version can't hand back a single element until the *entire*
structure has been walked and fully materialized in memory. The generator
version starts producing values immediately, and a caller who only wants
the first few elements (`itertools.islice(flatten(huge_structure), 5)`)
never pays the cost of the rest.

<a id="chapter-12"></a>
## Chapter 12: Decorators

*File: `python/1_core/21_retry_decorator.py`*

A **decorator** is a function that takes a function and returns a new
function wrapping it with extra behavior — the `@decorator` syntax above a
`def`. A *parameterized* decorator (`@retry(times=3)`) is one layer
deeper: a function that takes the parameters and *returns* a decorator,
which then wraps the target function:

```python
import functools

def retry_ugly(fn, times, *args, **kwargs):
    last_exc = None
    for _ in range(times):
        try:
            return fn(*args, **kwargs)
        except Exception as exc:
            last_exc = exc
    raise last_exc

def retry(times):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            return retry_ugly(fn, times, *args, **kwargs)
        return wrapper
    return decorator

@retry(times=3)
def flaky_call():
    ...
```

Without the decorator, every call site that needs retry behavior
duplicates its own `try`/`except` loop — easy to get subtly wrong or
forget entirely. `functools.wraps(fn)` matters too: without it, the
wrapped function loses its original `__name__` and docstring, breaking any
introspection or debugging tooling that relies on them.

<a id="chapter-13"></a>
## Chapter 13: Context Managers

*File: `python/1_core/22_context_manager_transaction.py`*

A **context manager** guarantees setup and teardown code always run
together, no matter how the block in between exits — the generalization of
what `try`/`finally` does by hand, formalized via `__enter__` and
`__exit__`:

```python
class Transaction:
    def __init__(self, log):
        self.log = log

    def __enter__(self):
        self.log.append("BEGIN")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.log.append("ROLLBACK" if exc_type is not None else "COMMIT")
        return False   # False = re-raise whatever exception occurred

with Transaction(log):
    do_something_that_might_raise()
```

Duplicating a `try`/`except`/`finally` block at every call site that needs
this pattern is easy to get wrong (an early `return` that skips cleanup, an
`except` clause that swallows the wrong exception). A context manager
class centralizes the guarantee once, and every `with Transaction(log):`
call site gets it correctly for free. `contextlib.contextmanager` offers
the same capability starting from a generator function instead of a class,
for simpler cases.

<a id="chapter-14"></a>
## Chapter 14: Standard Library Deep Cuts

*Files: `python/1_core/23_run_length_encoding.py`, `24_dataclasses.py`, `25_concurrent_map.py`*

### 14.1 `itertools.groupby`: run-length encoding

Run-length encoding compresses a sequence by replacing runs of
**consecutive** equal elements with a single `(value, count)` pair.
`itertools.groupby` groups consecutive elements sharing a key in a single
pass — note this is different from `collections.Counter`, which counts
*all* occurrences regardless of position:

```python
import itertools

def run_length_encode_ugly(seq):
    result, prev, count = [], None, 0
    for x in seq:
        if x == prev:
            count += 1
        else:
            if prev is not None:
                result.append((prev, count))
            prev, count = x, 1
    if prev is not None:
        result.append((prev, count))
    return result

def run_length_encode(seq):
    return [(value, sum(1 for _ in group)) for value, group in itertools.groupby(seq)]
```

### 14.2 `dataclasses`: eliminating boilerplate

Many small classes exist purely to hold a fixed set of named fields, and
need `__init__`, `__eq__`, and a readable `__repr__` — mechanical,
repetitive, and easy to get subtly wrong by hand (an `__eq__` that only
compares some fields, a `__repr__` that drifts out of sync after a field
is added). `@dataclass` generates all three from a class body that just
declares the fields:

```python
from dataclasses import dataclass

class PointUgly:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __eq__(self, other):
        return isinstance(other, PointUgly) and self.x == other.x and self.y == other.y
    def __repr__(self):
        return f"PointUgly(x={self.x}, y={self.y})"

@dataclass
class PointRight:
    x: int
    y: int
```

`PointRight` gets a correct `__init__`, `__eq__`, and `__repr__`
(`"PointRight(x=1, y=2)"`) automatically — the class definition states
*what* the fields are once, and the decorator handles the *how*.

### 14.3 `concurrent.futures`: threads for I/O-bound work

I/O-bound work (network calls, disk reads — anything that spends most of
its time *waiting*) wastes wall-clock time run sequentially, since each
call blocks the whole program even though the CPU is idle during the wait.
Python threads are a good fit here despite the GIL, because the GIL is
released while a thread blocks on I/O — multiple threads can be "waiting"
concurrently, so total wall-clock time approaches the slowest single call
instead of the sum of all of them:

```python
import time
from concurrent.futures import ThreadPoolExecutor

def fetch(item):
    time.sleep(0.01)          # stand-in for a blocking network call
    return item * 2

def fetch_all_ugly(items):                      # sequential
    return [fetch(item) for item in items]

def fetch_all(items):                           # concurrent
    with ThreadPoolExecutor(max_workers=max(1, len(items))) as executor:
        return list(executor.map(fetch, items))
```

`ThreadPoolExecutor.map` preserves input order in its results, so it's a
drop-in replacement for a sequential loop wherever the work is independent
and I/O-bound. Note this is a **wall-clock** win, not a change in
asymptotic time complexity — both versions still perform n units of work;
what changes is how much of that work overlaps in real time.

---

# Part V — Data Structures

<a id="chapter-15"></a>
## Chapter 15: Linked Lists

*File: `python/2_ds/1_reverse_linked_list.py` (practice exercise)*

A singly linked list is a chain of nodes, each holding a value and a
pointer to the next node. Unlike an array, there's no contiguous memory or
O(1) random access — but insertion/removal at a known position is O(1)
(no shifting elements). **Reversing** a linked list is the classic entry
point into pointer manipulation: every node's `next` pointer must flip to
point backward, without losing your place in the original chain.

A recursive approach reverses the rest of the list first, then fixes up
the current node — clean to write, but O(n) call-stack space. The
iterative approach walks the list once with **three pointers**
(`prev`, `curr`, `next`), relinking as it goes, using only O(1) extra
space:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next   # save before we overwrite curr.next
        curr.next = prev        # reverse the link
        prev = curr             # advance prev
        curr = next_node        # advance curr
    return prev                 # prev is the new head
```

This three-pointer relinking pattern generalizes to any singly-linked-list
problem that needs to restructure links in place — reversing a sublist,
detecting a cycle (Floyd's tortoise-and-hare, a two-pointer variant),
merging two sorted lists.

<a id="chapter-16"></a>
## Chapter 16: Trees and Breadth-First Search

*File: `python/2_ds/2_level_order_traversal.py` (practice exercise)*

A binary tree is hierarchical: each node has at most two children.
Traversing it **level order** (breadth-first — top to bottom, left to
right within each level) needs a **queue**, not a stack: process a node,
then enqueue its children so they're visited only after every other node
already waiting at the current depth. That FIFO discipline is exactly what
preserves "finish this level before starting the next." This differs from
depth-first traversals (preorder/inorder/postorder), which use a stack
(explicit or the call stack) and dive to a leaf before backtracking.

```python
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def level_order(root):
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):        # exactly this level's worth of nodes
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
```

`collections.deque` gives O(1) append/popleft — a plain `list` would cost
O(n) per `pop(0)`, turning an O(n) traversal into O(n²). BFS is the
natural choice whenever "shortest path" or "distance/depth" matters, since
it explores everything at distance k before anything at k+1 — the same
reason it drives the grid flood-fill in Chapter 17 and Dijkstra's
algorithm in Chapter 25.

<a id="chapter-17"></a>
## Chapter 17: Graphs I: Grids as Implicit Graphs

*File: `python/2_ds/3_number_of_islands.py` (practice exercise)*

A grid of cells is a graph in disguise: each cell is a node, connected to
its (up to four) orthogonal neighbors. "Number of islands" — counting
connected groups of land cells — is the classic **connected-components**
problem on that implicit graph: scan every cell, and whenever unvisited
land is found, that's a new island, so flood-fill outward marking every
reachable land cell visited (so it's never counted again):

```python
from collections import deque

def num_islands(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    count = 0

    def bfs(r, c):
        queue = deque([(r, c)])
        visited.add((r, c))
        while queue:
            row, col = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, col + dc
                if (0 <= nr < rows and 0 <= nc < cols
                        and grid[nr][nc] == "1" and (nr, nc) not in visited):
                    visited.add((nr, nc))
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                count += 1
                bfs(r, c)
    return count
```

DFS (recursion or an explicit stack) works just as well and has the same
O(rows·cols) time complexity — each cell is visited once regardless — but
DFS recursion depth can hit an island's full size, while BFS's queue holds
at most one "frontier" of cells at a time. This exact flood-fill shape —
scan for an unvisited starting point, explore everything reachable from
it, repeat — is the general template for counting connected components in
any graph, grid-shaped or not (compare Chapter 19's Union-Find, a
different algorithm for the same underlying question).

<a id="chapter-18"></a>
## Chapter 18: Tries

*File: `python/2_ds/4_trie.py` (practice exercise)*

A **trie** (prefix tree) stores a set of strings by sharing common
prefixes: each node represents one character position, with children for
each possible next character, and a marker for "a word ends here."
Looking up or inserting a string of length L costs O(L), independent of
how many other strings are stored:

```python
class TrieNode:
    def __init__(self):
        self.children = {}      # char -> TrieNode
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True

    def search(self, word):
        node = self._walk(word)
        return node is not None and node.is_word

    def starts_with(self, prefix):
        return self._walk(prefix) is not None

    def _walk(self, s):
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node
```

Compare this to a hash set of strings: insertion/lookup is O(L) too (to
hash the string), but "does any word start with this prefix?" would
require scanning every stored string — O(n·L) worst case, since a hash
gives you no way to find "things starting with X" without checking each
one. A trie answers prefix queries in O(L) by simply walking down the tree
as far as the prefix goes — exactly what autocomplete, spell-checkers, and
IP routing tables rely on.

<a id="chapter-19"></a>
## Chapter 19: Union-Find

*File: `python/2_ds/5_connected_components.py` (practice exercise)*

**Union-Find** (disjoint set union) tracks a partition of elements into
disjoint groups, supporting `find(x)` ("which group is x in?") and
`union(x, y)` ("merge x's group and y's group"). A naive implementation
makes both O(n) worst case (a long chain of parent pointers). Two
optimizations fix this:

- **Path compression**: during `find`, point every visited node directly
  at the root, flattening future lookups.
- **Union by rank**: always attach the smaller tree under the larger tree's
  root, keeping trees shallow.

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])   # path compression
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx                              # union by rank
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

def count_connected_components(n, edges):
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)
    return len({uf.find(x) for x in range(n)})
```

Combined, both operations become nearly O(1) amortized (technically
O(α(n)), the inverse Ackermann function — effectively constant for any
realistic n). Union-Find is the standard tool for connected components,
cycle detection in undirected graphs, and Kruskal's minimum spanning tree
algorithm — anywhere the question is "are these two things already in the
same group?" asked repeatedly as groups keep merging.

<a id="chapter-20"></a>
## Chapter 20: Amortized Analysis

*File: `python/2_ds/6_queue_using_stacks.py` (practice exercise)*

A stack is LIFO, a queue is FIFO — opposite orderings — yet a queue can be
built purely out of two stacks: push everything onto an "in" stack; to
dequeue, if the "out" stack is empty, dump the *entire* "in" stack onto it
(reversing the order), then pop from "out":

```python
class QueueUsingStacks:
    def __init__(self):
        self._in = []
        self._out = []

    def push(self, x):
        self._in.append(x)

    def _shift(self):
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())

    def pop(self):
        self._shift()
        return self._out.pop()

    def peek(self):
        self._shift()
        return self._out[-1]
```

A single `pop()` call can look expensive — O(n) if it triggers a full
dump — but each element only ever moves from `_in` to `_out` **once** over
its entire lifetime. Averaged over a long sequence of operations, the cost
per operation works out to O(1); this is **amortized analysis**:
occasional expensive operations that are individually rare, averaged over
the long run. The same argument underlies dynamic array resizing (an
occasional O(n) reallocation, amortized O(1) `append`) and hash table
rehashing — recognizing "this looks like O(n) worst case per call, but
each unit of work only ever happens once per element" is the skill.
`collections.deque` gets you a real O(1)-at-both-ends queue directly,
without needing two stacks at all — worth knowing as the practical answer,
even though the two-stack trick is the one worth understanding.

---

# Part VI — Algorithms

<a id="chapter-21"></a>
## Chapter 21: Sorting

*Files: `python/3_algo/1_merge_sort.py`, `2_quick_sort.py` (practice exercises)*

### 21.1 Merge sort

Merge sort is the canonical divide-and-conquer sort: split the array in
half, recursively sort each half, then merge the two sorted halves back
together in linear time.

```python
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return _merge(left, right)

def _merge(left, right):
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

Because the array halves at each level (log n levels) and merging a
level's worth of subarrays costs O(n) total per level, the whole algorithm
runs in **O(n log n) time, guaranteed** — not just on average, unlike
quicksort's worst case. The tradeoff is space: merging needs an auxiliary
array, O(n) extra space. Merge sort is also **stable** (equal elements
keep their relative order), which matters when sorting records by one
field while preserving an earlier sort on another.

### 21.2 Quicksort

Quicksort partitions in place around a pivot — everything smaller to its
left, everything larger to its right — then recursively sorts each side:

```python
def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[len(nums) // 2]
    left = [x for x in nums if x < pivot]
    mid = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)
```

Partitioning can be done in place, so quicksort typically needs only
O(log n) extra space (the recursion stack) instead of merge sort's O(n) —
but its worst-case time is **O(n²)**, which happens when the pivot choice
repeatedly splits the array as unevenly as possible (e.g. always picking
the first element on an already-sorted array). Randomizing the pivot
choice makes that worst case astronomically unlikely in practice, which is
why quicksort — despite the theoretically worse bound — is often faster in
practice than merge sort, thanks to better cache locality and lower
constant factors.

<a id="chapter-22"></a>
## Chapter 22: Two Pointers at Scale

*File: `python/3_algo/3_three_sum.py` (practice exercise)*

The two-pointer technique from Chapter 3 extends naturally from two-sum to
**three-sum**: sort the array first (O(n log n)), then fix one element and
use two pointers — from the two ends of the remaining subarray — to find
pairs summing to the target, moving inward based on whether the current
sum is too high or too low:

```python
def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue                              # skip duplicate "fixed" elements
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1                      # skip duplicate pairs
    return result
```

Since the subarray is sorted, moving a pointer strictly increases or
decreases the sum, so the scan never needs to backtrack. This turns an
O(n³) brute-force triple-nested loop into **O(n²)**: O(n) choices for the
fixed element, times O(n) for the two-pointer scan. The same pattern
generalizes to k-sum problems by fixing k-2 elements and two-pointering
the rest.

<a id="chapter-23"></a>
## Chapter 23: Backtracking

*Files: `python/3_algo/4_permutations.py`, `5_subsets.py` (practice exercises)*

**Backtracking** builds a solution incrementally, one choice at a time,
and undoes a choice as soon as it can't lead to a valid complete solution —
DFS over a tree of partial solutions.

### 23.1 Permutations

At each step, choose one of the remaining unused elements, recurse, then
undo that choice (mark it unused again) before trying the next option:

```python
def permutations(nums):
    result = []
    used = [False] * len(nums)
    path = []

    def backtrack():
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i, num in enumerate(nums):
            if used[i]:
                continue
            used[i] = True
            path.append(num)
            backtrack()
            path.pop()          # undo
            used[i] = False     # undo
    backtrack()
    return result
```

There are n! permutations of n elements, and building each one takes O(n),
so total work is **O(n · n!)** — fundamentally exponential, not a
complexity you can improve algorithmically, since the answer itself has
that many entries. Backtracking's value here is systematically covering
every possibility without missing or repeating one.

### 23.2 Subsets

Subsets (the power set) branch differently: at each element, make a
*binary* choice — include it, or don't — rather than choosing among
remaining unused items:

```python
def subsets(nums):
    result = []
    path = []

    def backtrack(start):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()          # undo
    backtrack(0)
    return result
```

This produces 2ⁿ subsets (each element independently in or out) — the
output size alone is exponential, same shape as permutations' n!. The
backtracking template is identical in spirit: append the current partial
result, try including the next choice and recurse, then undo it and
continue — exhaustively covering both branches of the choice tree.

<a id="chapter-24"></a>
## Chapter 24: Greedy Algorithms

*File: `python/3_algo/6_jump_game.py` (practice exercise)*

A **greedy** algorithm makes the locally-best choice at each step and
never reconsiders it, trusting that leads to a globally optimal answer —
which only works when the problem has the right structure. Jump Game
(can you reach the last index, given each position's max jump length?) is
a clean example where greedy provably works: track the furthest index
reachable so far; if you ever reach an index beyond that furthest reach,
you're stuck.

```python
def can_jump(nums):
    furthest = 0
    for i, jump in enumerate(nums):
        if i > furthest:
            return False
        furthest = max(furthest, i + jump)
    return True
```

There's no need to explore every possible sequence of jumps (which would
be exponential) — just one running number, updated in a single **O(n)**
linear pass. Recognizing when a problem reduces to "track one running best
value" instead of "explore all choices" is the key skill greedy problems
test.

<a id="chapter-25"></a>
## Chapter 25: Graphs II: Shortest Paths

*File: `python/3_algo/7_dijkstra.py` (practice exercise)*

**Dijkstra's algorithm** finds shortest paths from a source node to every
other node in a graph with non-negative edge weights. It's greedy: at each
step, pick the unvisited node with the smallest known distance, finalize
it (it can't improve later, since all edge weights are non-negative), then
**relax** its outgoing edges — updating neighbors' distances if going
through this node is shorter than what's currently known:

```python
import heapq
from collections import defaultdict

def dijkstra(n, edges, source):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))

    dist = [float("inf")] * n
    dist[source] = 0
    heap = [(0, source)]                    # (distance, node)
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue                        # stale entry, already found a shorter path
        for v, w in graph[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(heap, (dist[v], v))
    return dist
```

A min-heap keyed by distance (the same `heapq` tool from Chapter 7) makes
"pick the smallest unvisited distance" an O(log n) operation instead of an
O(n) scan, bringing total time to **O((V + E) log V)**. This is the same
priority-queue pattern used in the kth-largest-style streaming problem —
just applied to graph traversal, greedily finalizing the closest node
instead of tracking the k largest values.

<a id="chapter-26"></a>
## Chapter 26: Dynamic Programming II: Compressed and 2D State

*Files: `python/3_algo/8_maximum_subarray.py`, `10_longest_common_subsequence.py` (practice exercises)*

### 26.1 Kadane's algorithm

**Kadane's algorithm** finds the maximum-sum contiguous subarray in O(n)
by making one local decision at each position: extend the current
subarray by including this element, or start a new subarray here —
whichever gives a larger running sum. A negative running sum can never
help a future subarray, so once the running total drops below the current
element alone, it's better to restart than to drag the negative baggage
forward:

```python
def max_subarray(nums):
    best = current = nums[0]
    for x in nums[1:]:
        current = max(x, current + x)
        best = max(best, current)
    return best
```

This is DP with the "state" compressed to a single running value (best sum
ending exactly at the current index) rather than a full table, since each
step only depends on the immediately preceding one — the same
one-step-back-only shape as Chapter 6's climbing-stairs.

### 26.2 Longest common subsequence

The **LCS** of two strings is the longest sequence of characters
appearing in both, in the same relative order, but not necessarily
contiguous. Unlike Kadane's, this genuinely needs a 2D table: define
`dp[i][j]` as the LCS length using the first `i` characters of one string
and the first `j` of the other. If those characters match,
`dp[i][j] = dp[i-1][j-1] + 1` (extend the previous match); otherwise
`dp[i][j] = max(dp[i-1][j], dp[i][j-1])` (skip a character from whichever
side preserves the longer match):

```python
def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]
```

This gives **O(m·n)** time and space — reducible to O(min(m, n)) space,
since each row only ever depends on the row directly above it, the same
observation that let Chapter 6 collapse Fibonacci's whole table down to
two variables. The naive alternative — trying every subsequence of one
string against the other — is exponential.

<a id="chapter-27"></a>
## Chapter 27: Bit Manipulation

*File: `python/3_algo/9_single_number.py` (practice exercise)*

**XOR** (`^`) has two properties that make it a powerful bit-manipulation
tool: `x ^ x == 0` (anything XORed with itself cancels to zero), and
`x ^ 0 == x` (a no-op) — and it's commutative and associative, so order
doesn't matter. XOR every element of an array together, and every value
appearing an *even* number of times cancels out completely, leaving only
whatever appears an *odd* number of times:

```python
import functools
import operator

def single_number(nums):
    return functools.reduce(operator.xor, nums, 0)
```

This solves "find the element that doesn't appear twice" in **O(n) time
and O(1) space** — no hash set needed to track what's been seen, which is
normally the O(n)-space tool you'd reach for first (compare Chapter 2).
Bit tricks like this show up whenever a problem has an "everything pairs
up except one thing" structure — and note the reappearance of
`functools.reduce` from Chapter 9, folding an array down with a different
binary operator this time.

---

# Part VII — The Numerical Stack

This part is the direct continuation of Chapter 8: every section below
follows the same recipe — identify the Python-loop version, then find the
vectorized library call that pushes the same loop down into compiled code.

<a id="chapter-28"></a>
## Chapter 28: NumPy

*Files: `python/numpy/1_matrix_multiplication.py` through `5_axis_reduction.py` (practice exercises)*

### 28.1 Matrix multiplication and BLAS

The textbook definition of matrix multiplication — for each output cell,
sum the products of a row and a column — is a triple-nested loop, O(n³)
for n×n matrices, and in pure Python each multiply-add pays interpreter
overhead per element:

```python
def matmul_ugly(A, B):
    n, m, p = len(A), len(B), len(B[0])
    result = [[0] * p for _ in range(n)]
    for i in range(n):
        for j in range(p):
            for k in range(m):
                result[i][j] += A[i][k] * B[k][j]
    return result

import numpy as np

def matmul(A, B):
    return (np.array(A) @ np.array(B)).tolist()
```

`np.dot`/`@` delegates to **BLAS** (Basic Linear Algebra Subprograms) —
highly optimized, often multi-threaded C/Fortran routines exploiting CPU
cache lines and SIMD instructions. The algorithmic complexity doesn't
change (still roughly O(n³) for naive BLAS), but the constant-factor
difference between a Python triple loop and BLAS is often 100–1000x for
realistic sizes.

### 28.2 Boolean masking

Comparing an array to a value (`arr > threshold`) produces a same-shaped
boolean array in one vectorized pass; indexing the array with that mask
(`arr[arr > threshold]`) returns only the matching elements:

```python
def above_threshold_ugly(nums, threshold):
    return [x for x in nums if x > threshold]

import numpy as np

def above_threshold(nums, threshold):
    arr = np.array(nums)
    return arr[arr > threshold].tolist()
```

Both the comparison and the selection run as compiled C loops over
contiguous memory, instead of a Python-level loop testing and appending
one element at a time. The same mechanism underlies conditional assignment
(`arr[mask] = value`) and combining conditions with `&`/`|` (not
`and`/`or`, which don't vectorize element-wise).

### 28.3 Broadcasting

**Broadcasting** applies an operation between arrays of different but
compatible shapes without an explicit loop or manually replicated data.
Shapes are compared dimension by dimension from the right: dimensions are
compatible if they're equal, or if one of them is 1 (conceptually
"stretched" to match, without actually copying memory):

```python
import numpy as np

def add_vector_to_rows(matrix, vector):
    return (np.array(matrix) + np.array(vector)).tolist()
```

Adding a length-n vector to every row of an (m, n) matrix is the classic
example: the vector's shape `(n,)` broadcasts against `(m, n)` as if
repeated m times, but that repetition is never actually materialized — the
whole thing happens in a single vectorized pass, avoiding both a Python
loop and the O(m·n) memory a literal tile/repeat would cost.

### 28.4 Partial sorting

Finding the k largest values doesn't require fully sorting — full sorting
costs O(n log n) but gives far more ordering information than needed.
`numpy.argpartition` rearranges an array so the element at a given index
lands in its final sorted position, with everything smaller to its left
and everything larger to its right (each side individually unordered) —
the same partial-sort idea as quickselect, O(n) average time:

```python
import numpy as np

def top_k(nums, k):
    arr = np.array(nums)
    idx = np.argpartition(arr, -k)[-k:]
    return sorted(arr[idx].tolist(), reverse=True)
```

Partitioning around the `(n-k)`-th position and slicing the top k off is
O(n); sorting just those k afterward is O(k log k) — much cheaper than
sorting all n elements when k is small.

### 28.5 Axis-aware reductions

Reductions (`sum`, `mean`, `max`, ...) collapse an array along one or more
dimensions. NumPy's `axis` parameter picks which dimension collapses: for
a 2D array, `axis=0` reduces down the rows (a per-column result), `axis=1`
reduces across columns (a per-row result) — a useful mental model is
"`axis=k` means the result loses dimension k":

```python
import numpy as np

def row_and_col_sums(matrix):
    arr = np.array(matrix)
    return arr.sum(axis=1).tolist(), arr.sum(axis=0).tolist()
```

Doing this manually means nested loops re-summing each row/column from
scratch; NumPy's axis-aware reduction does the same work as one
vectorized C-level pass, and generalizes cleanly to arrays with more than
two dimensions, where manual nested loops get unwieldy fast.

<a id="chapter-29"></a>
## Chapter 29: SciPy

*Files: `python/scipy/1_optimize.py` through `5_interpolate.py` (practice exercises)*

### 29.1 Numerical optimization

Minimizing a function by hand-coded grid search evaluates it at every
point on a fixed grid — simple, but accuracy is capped by grid spacing,
and cost grows exponentially with dimensions. `scipy.optimize` implements
proper numerical optimization algorithms (BFGS, Nelder-Mead, etc.) that
use the function's local behavior to iteratively step toward a minimum:

```python
from scipy.optimize import minimize_scalar

def minimize_quadratic(a, b, c):
    result = minimize_scalar(lambda x: a * x**2 + b * x + c)
    return round(result.x, 2)
```

This typically converges in a handful of evaluations rather than
thousands, with precision limited by numerical tolerance rather than grid
spacing — the workhorse behind fitting models to data, calibrating
parameters, and portfolio optimization.

### 29.2 Statistics: z-scores

A z-score measures how many standard deviations a value is from a
dataset's mean: `z = (x - mean) / std`. Computing it by hand means three
separate O(n) passes (mean, then std, then each z-score):

```python
from scipy import stats

def zscores(nums):
    return [round(z, 2) for z in stats.zscore(nums)]
```

`scipy.stats.zscore` computes the whole thing as one vectorized call — the
basis of outlier detection (flag anything beyond ±3 std), standardization
before feeding data into ML models, and comparing values measured on
different scales.

### 29.3 Pairwise distances

Computing pairwise Euclidean distances between every pair of points in two
sets is a common building block in clustering and nearest-neighbor search.
The direct approach nests a loop over each point in A inside a loop over
each point in B — O(n·m) distance computations:

```python
from scipy.spatial.distance import cdist

def pairwise_distances(A, B):
    return [[round(d, 2) for d in row] for row in cdist(A, B)]
```

`scipy.spatial.distance.cdist` computes the entire n×m distance matrix in
one vectorized call, using the same trick as matrix multiplication:
`‖a-b‖² = ‖a‖² + ‖b‖² - 2·a·b` expands the squared distance into dot
products, which BLAS computes for the whole matrix at once.

### 29.4 Linear algebra

Solving `Ax = b` by hand means Gaussian elimination — forward elimination
to zero out entries below the diagonal, then back-substitution — O(n³) and
easy to get numerically unstable without pivoting:

```python
from scipy.linalg import solve

def solve_system(A, b):
    return [round(x, 2) for x in solve(A, b)]
```

`scipy.linalg.solve` calls LAPACK routines performing LU decomposition
with partial pivoting automatically — better numerical stability *and* a
heavily optimized O(n³) implementation. This is the direct workhorse
behind linear regression (the normal equations reduce to a linear system)
and portfolio optimization.

### 29.5 Interpolation

Linear interpolation fills a missing value between two known points by
assuming a constant rate of change between them:
`y0 + (y1 - y0) * (x - x0) / (x1 - x0)`. Doing this for a whole series
manually means finding the surrounding known points for each gap, in a
loop:

```python
from scipy.interpolate import interp1d

def interpolate(xs, ys, queries):
    f = interp1d(xs, ys)
    return [round(float(y), 2) for y in f(queries)]
```

`scipy.interpolate.interp1d` builds a reusable interpolating function from
the known points once, then evaluates it at any x (or array of x's) in a
vectorized call — useful for filling gaps in a time series or resampling
data onto a different set of x-coordinates entirely.

<a id="chapter-30"></a>
## Chapter 30: Pandas

*Files: `python/pandas/1_groupby.py` through `5_resample.py` (practice exercises)*

### 30.1 Split-apply-combine

**GroupBy** implements the "split-apply-combine" pattern: split data into
groups by a key, apply a function (sum, mean, count, ...) to each group
independently, then combine the results back together. Doing this by hand
means a dict keyed by group, appended to in a loop, then reduced in a
second pass:

```python
import pandas as pd

def average_by_category(rows):
    df = pd.DataFrame(rows, columns=["category", "value"])
    return df.groupby("category")["value"].mean().round(2).to_dict()
```

`DataFrame.groupby` does the same conceptual thing, but grouping and
aggregation both run as vectorized operations over NumPy arrays
underneath, and compose cleanly with any aggregation function (or several
at once via `.agg()`) without new looping code per aggregation.

### 30.2 Joins

Joining two datasets on a common key is one of the most common data
operations, and one of the easiest to implement naively-but-slowly: a
nested loop comparing every row of A against every row of B is O(n·m).
The efficient approach builds a hash index on the join key for one side
(O(n)), then does a single O(1)-average-lookup pass over the other side —
O(n+m) total, the same "index once, probe many times" idea as a database's
hash join:

```python
import pandas as pd

def inner_join(left, right):
    left_df = pd.DataFrame(left, columns=["key", "left_value"])
    right_df = pd.DataFrame(right, columns=["key", "right_value"])
    merged = pd.merge(left_df, right_df, on="key").sort_values("key")
    return list(merged.itertuples(index=False, name=None))
```

`pandas.merge` implements exactly this (hash join, or sort-merge depending
on the data), so joining two DataFrames on a key column is a single
vectorized call rather than hand-rolled nested loops.

### 30.3 Missing data

Forward-fill (carry the last known value forward) assumes a value hasn't
changed since the last observation — reasonable for something like a price
that only updates on trades. By hand, it means tracking "the last
non-missing value seen" in a loop:

```python
import pandas as pd

def forward_fill(nums):
    return pd.Series(nums).ffill().tolist()
```

`pandas.Series.ffill()` (and the related `bfill()`, `interpolate()`,
`fillna()`) do the same as a vectorized operation, composing with the rest
of pandas' missing-data handling (`isna()`, `dropna()`).

### 30.4 Pivot tables

A pivot table reshapes "long" data (one row per observation) into "wide"
data (one row per category, one column per sub-category, cells holding an
aggregate) — the same reshape spreadsheets do. By hand it's a nested dict,
built by iterating every record once and updating the right (row, col)
bucket:

```python
import pandas as pd

def pivot_sum(rows):
    df = pd.DataFrame(rows, columns=["row_key", "col_key", "value"])
    table = df.pivot_table(index="row_key", columns="col_key",
                            values="value", aggfunc="sum", fill_value=0)
    return {r: {c: int(table.loc[r, c]) for c in table.columns if table.loc[r, c]}
            for r in table.index}
```

`pandas.pivot_table` generalizes this: it groups by row and column keys
simultaneously and applies an aggregation function, producing the
reshaped DataFrame directly without manually managing the nested bucket
structure.

### 30.5 Resampling

Resampling changes a time series' frequency — e.g. daily data into weekly
data by aggregating every 7 consecutive days into one value. By hand, this
means walking the series in fixed-size chunks with careful
off-by-one bucket-boundary bookkeeping:

```python
import pandas as pd

def weekly_sums(daily_values):
    idx = pd.date_range("2020-01-01", periods=len(daily_values), freq="D")
    series = pd.Series(daily_values, index=idx)
    return series.resample("7D").sum().tolist()
```

`DataFrame.resample` (built on a `DatetimeIndex`) does the bucketing and
aggregation as one vectorized operation, correctly handling calendar-aware
boundaries (weeks, months, quarters don't have a fixed number of days)
that a naive fixed-size chunking loop would get wrong — the standard tool
for downsampling high-frequency financial or sensor data to a coarser
reporting frequency.

---

<a id="appendix-a"></a>
## Appendix A: Tool Cheat Sheet

| Tool | What it's for | Where it appears |
|---|---|---|
| `dict` | O(1) average hash-map lookup/insert | Ch. 2, 3 |
| `collections.Counter` | frequency counting | Ch. 2 |
| `collections.defaultdict` | dict with an automatic default | Ch. 2, 18 |
| `collections.deque` | O(1) both-ends queue | Ch. 16, 17, 20 |
| `bisect.bisect_left/right` | binary search on a sorted list | Ch. 5 |
| `functools.lru_cache` | memoize a pure function | Ch. 1, 6 |
| `heapq` | min-heap / priority queue | Ch. 7, 25 |
| `numpy.cumsum` | vectorized prefix sums | Ch. 8 |
| `functools.reduce` | general-purpose fold | Ch. 9, 27 |
| `functools.partial` | fix arguments ahead of time | Ch. 9 |
| `itertools.accumulate` | running/prefix reduction | Ch. 9 |
| `itertools.islice` | lazily slice an iterable/generator | Ch. 9, 11 |
| `abc.ABC` / `@abstractmethod` | enforced interfaces | Ch. 10 |
| `@property` | computed/managed attribute access | Ch. 10 |
| `@classmethod` | alternative constructors | Ch. 10 |
| `yield` / `yield from` | lazy generators, generator delegation | Ch. 11 |
| `functools.wraps` | preserve metadata through a decorator | Ch. 12 |
| `__enter__` / `__exit__` | context manager protocol | Ch. 13 |
| `itertools.groupby` | group consecutive equal elements | Ch. 14 |
| `dataclasses.dataclass` | auto-generate `__init__`/`__eq__`/`__repr__` | Ch. 14 |
| `concurrent.futures.ThreadPoolExecutor` | concurrent I/O-bound calls | Ch. 14 |
| Union-Find (path compression + union by rank) | disjoint sets, connected components | Ch. 19 |
| `numpy.argpartition` | partial sort for top-k | Ch. 28 |
| `numpy` broadcasting | vectorized ops across mismatched shapes | Ch. 28 |
| `scipy.optimize.minimize_scalar` | numerical function minimization | Ch. 29 |
| `scipy.stats.zscore` | vectorized standardization | Ch. 29 |
| `scipy.spatial.distance.cdist` | vectorized pairwise distances | Ch. 29 |
| `scipy.linalg.solve` | LAPACK-backed linear system solving | Ch. 29 |
| `scipy.interpolate.interp1d` | vectorized linear interpolation | Ch. 29 |
| `pandas.DataFrame.groupby` | split-apply-combine | Ch. 30 |
| `pandas.merge` | hash/sort-merge join | Ch. 30 |
| `pandas.Series.ffill` | forward-fill missing values | Ch. 30 |
| `pandas.pivot_table` | reshape long data to wide | Ch. 30 |
| `pandas.DataFrame.resample` | calendar-aware time series bucketing | Ch. 30 |

<a id="appendix-b"></a>
## Appendix B: Repo Map and How to Keep Practicing

```
python/
  1_core/    25 files, fully solved — Chapters 1-14 above
  2_ds/       6 files, practice stubs — Chapter 15-20
  3_algo/    10 files, practice stubs — Chapter 21-27
  numpy/      5 files, practice stubs — Chapter 28
  scipy/      5 files, practice stubs — Chapter 29
  pandas/     5 files, practice stubs — Chapter 30
```

Every folder numbers its files independently starting from 1. Three
Claude Code skills drive the practice loop:

| Skill | Does |
|-------|------|
| `next` | Generates the next numbered stub task into `python/1_core/`. |
| `solve` | Writes a full, working solution for a given `<number>` or `<folder>/<number>`. |
| `grade` | Reviews a solved file: runs its tests, checks the complexity analysis, flags code-quality issues. |

The stub files in `2_ds/`, `3_algo/`, `numpy/`, `scipy/`, and `pandas/` are
where the theory above turns into practice: each has the same Theory /
Packages / Task / Hint structure as the solved `1_core/` files, with the
`_ugly`/right-way functions left as `pass` for you to fill in. Solve them
yourself first — the code in Chapters 15–30 above shows the shape of a
correct answer, but working through the `_ugly` version, hitting its
complexity limits, and then reaching for the named tool is the actual
exercise.
