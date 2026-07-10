# Theory:
## A context manager guarantees setup and teardown code always runs
## together, in order, no matter how the block in between exits - normally
## via __enter__/__exit__, invoked with the `with` statement. It's the
## generalization of what try/finally is used for by hand: acquiring a
## resource (a transaction, a file, a lock) and guaranteeing its release
## even if an exception is raised partway through. Duplicating a
## try/except/finally block at every call site that needs this pattern
## works but is easy to get wrong (an early return that skips the
## cleanup, an except clause that swallows the wrong exception) and
## duplicates the same logic everywhere it's needed. A context manager
## class centralizes the guarantee in __enter__ and __exit__ once, and
## every `with Transaction(log):` call site gets it correctly for free.


# Packages:
## __enter__ / __exit__ - the protocol methods that back the `with` statement
## contextlib.contextmanager - build a context manager from a generator function instead of a class
## contextlib.suppress - a built-in context manager for ignoring specific exceptions
## try / finally - the manual, unreusable version of what a context manager formalizes


# Task:
## Implement a Transaction context manager: entering appends "BEGIN" to a
## shared log; on a clean exit it appends "COMMIT"; if the block raises, it
## appends "ROLLBACK" instead and lets the exception propagate.
## Test1: Inputs: with Transaction(log): pass (no exception)   Outputs: log == ["BEGIN", "COMMIT"]
## Test2: Inputs: with Transaction(log): raise ValueError() (caught by caller)   Outputs: log == ["BEGIN", "ROLLBACK"], ValueError propagates
## Test3: Inputs: two sequential successful `with Transaction(log):` blocks   Outputs: log == ["BEGIN", "COMMIT", "BEGIN", "COMMIT"]
## Hint:
## Ugly way: a manual try/except/finally block written out at every call
## site that needs begin/commit/rollback behavior.
## Right way: a Transaction context manager class (__enter__/__exit__) used
## via `with Transaction(log):`.


class Transaction:
    def __init__(self, log):
        self.log = log

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass


def run_transaction_ugly(log, should_raise):
    pass


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def run_transaction(log, should_raise):
    return run_transaction_ugly(log, should_raise)


# Tests:
def validate():
    log = []
    run_transaction_ugly(log, should_raise=False)
    assert log == ["BEGIN", "COMMIT"], f"expected BEGIN/COMMIT, got {log}"

    log = []
    try:
        run_transaction_ugly(log, should_raise=True)
        assert False, "expected ValueError to propagate"
    except ValueError:
        pass
    assert log == ["BEGIN", "ROLLBACK"], f"expected BEGIN/ROLLBACK, got {log}"

    log = []
    with Transaction(log):
        pass
    assert log == ["BEGIN", "COMMIT"]
    with Transaction(log):
        pass
    assert log == ["BEGIN", "COMMIT", "BEGIN", "COMMIT"]

    log = []
    try:
        with Transaction(log):
            raise ValueError("boom")
        assert False, "expected ValueError to propagate"
    except ValueError:
        pass
    assert log == ["BEGIN", "ROLLBACK"]
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    log = []
    run_transaction_ugly(log, should_raise=False)
    print(log)
