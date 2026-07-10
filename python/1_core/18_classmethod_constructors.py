# Theory:
## A classmethod receives the class itself (conventionally named cls)
## instead of an instance, which makes it the natural place to build
## "alternative constructor" logic: ways to create an instance from
## something other than the class's normal __init__ signature (a string, a
## dict, a file, another object's data). Without one, parsing logic lives
## in a free function that returns raw data (a tuple, a dict) which the
## caller must then manually pass into the constructor correctly every
## time - two steps, and nothing stops a caller from doing it wrong or
## forgetting a field. Point.from_string(s) folds both steps into one call
## that always returns a fully-formed, correct instance, and reads at the
## call site as clearly a Point-construction operation.


# Packages:
## @classmethod - define a method bound to the class, conventional way to write alternative constructors
## @staticmethod - a method that needs no access to the class or instance at all
## dataclasses.dataclass - can reduce boilerplate for the primary __init__ itself
## str.split - common parsing tool for classmethod constructors built from delimited strings


# Task:
## Implement a Point class with x and y, equality via ==, and a
## Point.from_string(s) classmethod that parses a "x,y" string into a Point.
## Test1: Inputs: Point.from_string("3,4")   Outputs: Point(3, 4)
## Test2: Inputs: Point.from_string("-1,7")   Outputs: Point(-1, 7)
## Test3: Inputs: Point.from_string("0,0")   Outputs: Point(0, 0)
## Hint:
## Ugly way: a free function parse_point_string_ugly(s) that returns a
## plain (x, y) tuple, leaving construction to the caller.
## Right way: a @classmethod Point.from_string(s) that returns a fully
## constructed Point directly.


# Solutions:

# Space - Time Complexity analysis:
## space: O(1) - a fixed-size tuple, independent of anything else in the program
## time: O(1) - one string split on a fixed-length input

def parse_point_string_ugly(s):
    x_str, y_str = s.split(",")  # O(1) | O(1)
    return (int(x_str), int(y_str))  # O(1) | O(1)


def point_from_string_ugly(s):
    x, y = parse_point_string_ugly(s)
    return Point(x, y)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    # Space - Time Complexity analysis:
    ## space: O(1) - one new Point instance, independent of anything else in the program
    ## time: O(1) - one string split on a fixed-length input

    @classmethod
    def from_string(cls, s):
        x_str, y_str = s.split(",")  # O(1) | O(1)
        return cls(int(x_str), int(y_str))  # O(1) | O(1)


# Tests:
def validate():
    cases = [
        ("3,4", Point(3, 4)),
        ("-1,7", Point(-1, 7)),
        ("0,0", Point(0, 0)),
    ]
    for s, expected in cases:
        result_ugly = point_from_string_ugly(s)
        assert result_ugly == expected, (
            f"point_from_string_ugly({s!r}): expected {expected!r}, got {result_ugly!r}"
        )
        result = Point.from_string(s)
        assert result == expected, (
            f"Point.from_string({s!r}): expected {expected!r}, got {result!r}"
        )
    print("SUCCESS")


if __name__ == "__main__":
    validate()
