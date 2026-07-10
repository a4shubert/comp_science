# Theory:
## A decorator is a function that takes a function and returns a new
## function wrapping it with extra behavior, applied with @decorator syntax
## above a def. A parameterized decorator (like @retry(times=3)) is one
## extra layer deeper: a function that takes the parameters and *returns* a
## decorator, which then wraps the target function. Retrying flaky
## operations (network calls, anything with transient failures) is a
## classic use case: without a decorator, every call site that needs
## retry behavior has to duplicate its own try/except loop, which is easy
## to get subtly wrong or forget entirely. functools.wraps matters here
## too - without it, the wrapped function loses its original __name__ and
## docstring, which breaks introspection and debugging tools that rely on
## them.


# Packages:
## functools.wraps - preserve a wrapped function's __name__/__doc__ through a decorator
## functools.lru_cache - a well-known parameterless decorator, useful comparison point
## time.sleep - common addition to a real retry decorator (backoff between attempts), not required here
## contextlib.contextmanager - another way to wrap behavior around a call, contrasted with decorators


# Task:
## Implement a retry(times) decorator: when applied to a function, calling
## the wrapped function retries on exception up to `times` total attempts,
## returning the first successful result; if every attempt raises, the last
## exception propagates to the caller.
## Test1: Inputs: a function failing on its first 2 calls then succeeding, wrapped with retry(times=3), called once   Outputs: the successful return value, and the function was actually called 3 times total
## Test2: Inputs: a function that always raises, wrapped with retry(times=2), called once   Outputs: the underlying exception propagates after exactly 2 attempts
## Test3: Inputs: a function that succeeds immediately, wrapped with retry(times=3), called once   Outputs: the successful return value, and the function was called exactly once (no unnecessary retries)
## Hint:
## Ugly way: a manual try/except loop written out at every call site that
## needs retry behavior, duplicated wherever it's needed.
## Right way: a reusable @retry(times) decorator (functools.wraps-preserving)
## applied once to the function definition itself.


import functools


# Solutions:

# Space - Time Complexity analysis:
## space: O(1) - only the last exception is held onto, no structure grows with the number of attempts
## time: O(times) - up to `times` calls to fn in the worst case (every attempt but the last fails)

def retry_ugly(fn, times, *args, **kwargs):
    last_exc = None  # O(1) | O(1)
    for _ in range(times):  # O(1) | O(times)
        try:
            return fn(*args, **kwargs)  # O(1) | O(1)
        except Exception as exc:  # O(1) | O(1)
            last_exc = exc  # O(1) | O(1)
    raise last_exc  # O(1) | O(1)


# Space - Time Complexity analysis:
## space: O(1) - only the last exception is held onto, same as the ugly version
## time: O(times) - up to `times` calls to the wrapped function in the worst case

def retry(times):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            return retry_ugly(fn, times, *args, **kwargs)  # O(1) | O(times)
        return wrapper
    return decorator


# Tests:
def make_flaky(fail_times):
    calls = {"count": 0}

    def flaky():
        calls["count"] += 1
        if calls["count"] <= fail_times:
            raise ValueError(f"attempt {calls['count']} failed")
        return "ok"

    return flaky, calls


def validate():
    flaky, calls = make_flaky(fail_times=2)
    assert retry_ugly(flaky, 3) == "ok"
    assert calls["count"] == 3

    always_fails, calls2 = make_flaky(fail_times=999)
    try:
        retry_ugly(always_fails, 2)
        assert False, "expected ValueError to propagate"
    except ValueError:
        pass
    assert calls2["count"] == 2

    immediate, calls3 = make_flaky(fail_times=0)
    assert retry_ugly(immediate, 3) == "ok"
    assert calls3["count"] == 1

    flaky, calls = make_flaky(fail_times=2)
    wrapped = retry(times=3)(flaky)
    assert wrapped() == "ok"
    assert calls["count"] == 3

    always_fails, calls2 = make_flaky(fail_times=999)
    wrapped_fail = retry(times=2)(always_fails)
    try:
        wrapped_fail()
        assert False, "expected ValueError to propagate"
    except ValueError:
        pass
    assert calls2["count"] == 2

    immediate, calls3 = make_flaky(fail_times=0)
    wrapped_immediate = retry(times=3)(immediate)
    assert wrapped_immediate() == "ok"
    assert calls3["count"] == 1
    print("SUCCESS")


if __name__ == "__main__":
    validate()
