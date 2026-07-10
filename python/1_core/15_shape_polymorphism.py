# Theory:
## Polymorphism means calling the same method name on objects of different
## types and having each type respond with its own correct behavior,
## without the caller needing to know which concrete type it's holding.
## The alternative - a caller that branches on type manually (isinstance
## checks or a type-tag field) - works but couples the caller to every
## concrete type that exists today, and silently fails to handle new types
## added later since nothing forces the branching code to be updated.
## Defining an abstract base class with an abstract method (via the abc
## module) flips this: each subclass is required to implement the method
## itself, and callers just invoke it polymorphically, so adding a new
## shape means writing one new class, not touching every place shapes are
## processed.


# Packages:
## abc.ABC / abc.abstractmethod - declare an interface subclasses must implement
## math.pi - needed for circle area
## isinstance() - runtime type check, the tool this task's "ugly way" leans on
## dataclasses.dataclass - alternative concise way to define simple value-holding classes


# Task:
## Given a list of shape objects (Circle or Rectangle), compute the total
## area. A Circle is constructed with a radius, a Rectangle with a width and
## a height.
## Test1: Inputs: shapes = [Rectangle(2, 2), Rectangle(3, 3)]   Outputs: 13
## Test2: Inputs: shapes = [Circle(1)]   Outputs: 3.141592653589793
## Test3: Inputs: shapes = []   Outputs: 0
## Hint:
## Ugly way: isinstance checks on each shape, computing the area formula
## inline in the total function instead of on the shape itself.
## Right way: an abstract Shape base class with an abstract area() method -
## sum(s.area() for s in shapes), polymorphic dispatch instead of branching.


import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        pass


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def total_area_ugly(shapes):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def total_area(shapes):
    return total_area_ugly(shapes)


# Tests:
def validate():
    cases = [
        ([Rectangle(2, 2), Rectangle(3, 3)], 13),
        ([Circle(1)], math.pi),
        ([], 0),
        ([Circle(2), Rectangle(1, 1)], 4 * math.pi + 1),
    ]
    for fn in (total_area_ugly, total_area):
        for shapes, expected in cases:
            result = fn(shapes)
            assert math.isclose(result, expected, rel_tol=1e-9), (
                f"{fn.__name__}({shapes!r}): expected {expected!r}, got {result!r}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    print(total_area_ugly([Rectangle(2, 2), Rectangle(3, 3)]))
    print(total_area_ugly([Circle(1)]))
    print(total_area_ugly([]))
    print(total_area_ugly([Circle(2), Rectangle(1, 1)]))
