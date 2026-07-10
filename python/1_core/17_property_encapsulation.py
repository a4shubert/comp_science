# Theory:
## Encapsulation means hiding an object's internal representation behind a
## controlled interface, so callers interact with meaningful operations
## instead of raw fields. Python's @property decorator lets a method be
## accessed with plain attribute syntax (obj.value instead of obj.value())
## while still running code on every access - useful when an attribute is
## actually derived from, or must stay in sync with, other internal state.
## Without properties, keeping two related values in sync (e.g. a
## temperature stored in both Celsius and Fahrenheit) requires the caller
## to remember to call a conversion function every time either one changes,
## which is easy to forget and easy to get out of sync. A property-based
## setter enforces the sync rule in exactly one place, inside the class,
## no matter how many places update the value.


# Packages:
## property() / @property - define computed/managed attribute access
## @x.setter - pair with @property to allow assignment through the same name
## functools.cached_property - like @property, but caches the computed value after first access
## dataclasses.dataclass(frozen=True) - alternative pattern for immutable, sync-free value objects


# Task:
## Implement a Temperature class constructed with a Celsius value, exposing
## both celsius and fahrenheit so that reading either always reflects the
## current temperature, and assigning to either updates the other.
## Test1: Inputs: Temperature(0), read .fahrenheit   Outputs: 32.0
## Test2: Inputs: Temperature(100), read .fahrenheit   Outputs: 212.0
## Test3: Inputs: Temperature(0), then set .fahrenheit = 32, then read .celsius   Outputs: 0.0
## Hint:
## Ugly way: plain attributes plus free conversion functions
## (celsius_to_fahrenheit_ugly(c)) that the caller must remember to call
## every time either value changes.
## Right way: @property / @x.setter - celsius and fahrenheit read and write
## through the same underlying value, always in sync.


# Solutions:

# Space - Time Complexity analysis:
## space: O(1) - a single float, independent of anything else in the program
## time: O(1) - one multiply and one add

def celsius_to_fahrenheit_ugly(celsius):
    return celsius * 9 / 5 + 32  # O(1) | O(1)


# Space - Time Complexity analysis:
## space: O(1) - a single float, independent of anything else in the program
## time: O(1) - one subtract and one multiply

def fahrenheit_to_celsius_ugly(fahrenheit):
    return (fahrenheit - 32) * 5 / 9  # O(1) | O(1)


def read_fahrenheit(temperature):
    return celsius_to_fahrenheit_ugly(temperature._celsius)


class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    # Space - Time Complexity analysis:
    ## space: O(1) - reads the single underlying _celsius field, no extra structure
    ## time: O(1) - one multiply and one add, same conversion as the ugly version

    @property
    def fahrenheit(self):
        return celsius_to_fahrenheit_ugly(self._celsius)  # O(1) | O(1)

    # Space - Time Complexity analysis:
    ## space: O(1) - writes the single underlying _celsius field, no extra structure
    ## time: O(1) - one subtract and one multiply, same conversion as the ugly version

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = fahrenheit_to_celsius_ugly(value)  # O(1) | O(1)


# Tests:
def validate():
    assert celsius_to_fahrenheit_ugly(0) == 32.0
    assert celsius_to_fahrenheit_ugly(100) == 212.0
    assert fahrenheit_to_celsius_ugly(32) == 0.0

    t = Temperature(0)
    assert read_fahrenheit(t) == 32.0

    t = Temperature(100)
    assert read_fahrenheit(t) == 212.0

    t = Temperature(0)
    assert t.fahrenheit == 32.0
    t.fahrenheit = 32
    assert t.celsius == 0.0
    print("SUCCESS")


if __name__ == "__main__":
    validate()
