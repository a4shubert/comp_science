# Theory:
## Many small classes exist purely to hold a fixed set of named fields and
## need __init__, __eq__, and a readable __repr__ - writing all three by
## hand is mechanical, repetitive boilerplate that's easy to get subtly
## wrong (e.g. __eq__ comparing only some fields, or __repr__ drifting out
## of sync after a field is added). The @dataclass decorator generates all
## of that from a class body that just declares typed fields, so the class
## definition states *what* the fields are once, and the decorator handles
## the *how* of construction, equality, and printing consistently and
## correctly. It's not a different feature from what a hand-written class
## does - it's the same result with the repetitive part automated.


# Packages:
## dataclasses.dataclass - auto-generate __init__/__eq__/__repr__ from field declarations
## dataclasses.field - customize a dataclass field's default/behavior (mutable defaults, etc.)
## typing.NamedTuple - a lighter-weight, immutable alternative for simple field bundles
## dataclasses.dataclass(frozen=True) - make a dataclass immutable/hashable


# Task:
## Implement two Point-like classes representing the same x, y data: one
## with __init__/__eq__/__repr__ written by hand, one using @dataclass to
## generate them automatically. Both should support equality comparison and
## produce a repr in the form "ClassName(x=<x>, y=<y>)".
## Test1: Inputs: PointUgly(1, 2) == PointUgly(1, 2)   Outputs: True
## Test2: Inputs: PointRight(1, 2) == PointRight(1, 3)   Outputs: False
## Test3: Inputs: repr(PointRight(1, 2))   Outputs: "PointRight(x=1, y=2)"
## Hint:
## Ugly way: a hand-written class defining __init__, __eq__, and __repr__
## explicitly, one line of boilerplate per field per method.
## Right way: @dataclass - declare the fields once, get __init__/__eq__/
## __repr__ generated automatically.


from dataclasses import dataclass


class PointUgly:
    def __init__(self, x, y):
        pass

    def __eq__(self, other):
        pass

    def __repr__(self):
        pass


@dataclass
class PointRight:
    x: int
    y: int


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def points_equal_ugly(p1, p2):
    return p1 == p2


# Tests:
def validate():
    assert points_equal_ugly(PointUgly(1, 2), PointUgly(1, 2)) is True
    assert points_equal_ugly(PointUgly(1, 2), PointUgly(1, 3)) is False
    assert PointRight(1, 2) == PointRight(1, 2)
    assert PointRight(1, 2) != PointRight(1, 3)
    assert repr(PointRight(1, 2)) == "PointRight(x=1, y=2)"
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(points_equal_ugly(PointUgly(1, 2), PointUgly(1, 2)))
    print(points_equal_ugly(PointUgly(1, 2), PointUgly(1, 3)))
    print(PointRight(1, 2) == PointRight(1, 2))
    print(repr(PointRight(1, 2)))
