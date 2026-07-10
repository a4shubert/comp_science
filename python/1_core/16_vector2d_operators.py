# Theory:
## Operator overloading lets a custom class respond to built-in syntax like
## +, ==, and repr() by defining "dunder" (double-underscore) methods:
## __add__ backs the + operator, __eq__ backs ==, __repr__ controls how the
## object prints. Without these, a class using +/== falls back to identity
## comparison and a TypeError on +, forcing every caller to use free
## functions instead (add_vectors(v1, v2) rather than v1 + v2) - which
## works but reads less naturally and doesn't compose with code that
## expects arithmetic-like objects. Implementing the dunder methods once on
## the class means every future caller gets natural syntax for free, and
## the class behaves consistently everywhere it's used (assertions, print
## statements, other arithmetic expressions).


# Packages:
## dataclasses.dataclass - can auto-generate __init__/__eq__/__repr__ for simple classes
## operator module - functional counterparts of the dunder operators (operator.add, etc.)
## functools.total_ordering - fills in comparison dunders given a minimal set
## NamedTuple - a lighter-weight alternative for simple immutable coordinate pairs


# Task:
## Implement a Vector2D class holding x and y, supporting addition via + and
## equality via ==, with a readable repr.
## Test1: Inputs: Vector2D(1, 2) + Vector2D(3, 4)   Outputs: Vector2D(4, 6)
## Test2: Inputs: Vector2D(0, 0) + Vector2D(-1, -1)   Outputs: Vector2D(-1, -1)
## Test3: Inputs: Vector2D(2, 3) + Vector2D(2, 3)   Outputs: Vector2D(4, 6)
## Hint:
## Ugly way: a plain add_vectors_ugly((x1, y1), (x2, y2)) free function
## operating on tuples, with no dedicated type.
## Right way: __add__ and __eq__ dunder methods on the class - v1 + v2 and
## v1 == v2 work directly.


# Solutions:

# Space - Time Complexity analysis:
## space: O(1) - a fixed-size tuple, independent of anything else in the program
## time: O(1) - two additions, no scaling factor

def add_vectors_ugly(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])  # O(1) | O(1)


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Space - Time Complexity analysis:
    ## space: O(1) - one new Vector2D instance, independent of anything else in the program
    ## time: O(1) - two additions, no scaling factor

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)  # O(1) | O(1)

    def __eq__(self, other):
        return isinstance(other, Vector2D) and self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"


# Tests:
def validate():
    cases = [
        (Vector2D(1, 2), Vector2D(3, 4), Vector2D(4, 6)),
        (Vector2D(0, 0), Vector2D(-1, -1), Vector2D(-1, -1)),
        (Vector2D(2, 3), Vector2D(2, 3), Vector2D(4, 6)),
    ]
    for v1, v2, expected in cases:
        result_ugly = Vector2D(*add_vectors_ugly((v1.x, v1.y), (v2.x, v2.y)))
        assert result_ugly == expected, (
            f"add_vectors_ugly(({v1.x}, {v1.y}), ({v2.x}, {v2.y})): "
            f"expected {expected!r}, got {result_ugly!r}"
        )
        result = v1 + v2
        assert result == expected, f"{v1!r} + {v2!r}: expected {expected!r}, got {result!r}"
    assert repr(Vector2D(1, 2)) == "Vector2D(1, 2)"
    print("SUCCESS")


if __name__ == "__main__":
    validate()
