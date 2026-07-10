# Theory:
## An interface is a contract: a set of methods every implementing class
## promises to provide, so code written against the interface works with
## any conforming class without caring which one it actually has. Python
## supports this informally via duck typing (if it has the method, call
## it) or formally via abc.ABC + @abstractmethod, which makes the contract
## enforced by the language itself - a subclass that doesn't implement
## every abstract method can't even be instantiated, raising a TypeError
## immediately at construction time rather than an AttributeError deep
## inside some unrelated code path much later. Duck typing is more
## flexible but defers the failure; an ABC catches a missing implementation
## as early and as loudly as possible, which matters most for a plugin-style
## system where new implementations get added over time.


# Packages:
## abc.ABC / abc.abstractmethod - declare and enforce an interface
## hasattr() / getattr() - duck-typing tools, check for a method without formally requiring it
## typing.Protocol - structural typing alternative to ABC (duck typing checked statically)
## inspect.isabstract - check whether a class still has unimplemented abstract methods


# Task:
## Given a list of payment processors and an amount, call each processor's
## process(amount) and collect the results in order.
## Test1: Inputs: processors = [CreditCardProcessor(), PayPalProcessor()], amount = 100   Outputs: ["Charged $100 to credit card", "Paid $100 via PayPal"]
## Test2: Inputs: processors = [PayPalProcessor()], amount = 50   Outputs: ["Paid $50 via PayPal"]
## Test3: Inputs: processors = [], amount = 10   Outputs: []
## Hint:
## Ugly way: hasattr(processor, "process") duck-typing checks before
## calling - a processor missing the method is silently skipped instead of
## failing loudly.
## Right way: an abc.ABC PaymentProcessor base class with an
## @abstractmethod process(amount) - any non-conforming class fails at
## instantiation, not silently at call time.


from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process(self, amount):
        pass


class CreditCardProcessor(PaymentProcessor):
    def process(self, amount):
        return f"Charged ${amount} to credit card"


class PayPalProcessor(PaymentProcessor):
    def process(self, amount):
        return f"Paid ${amount} via PayPal"


# Solutions:

# Space - Time Complexity analysis:
## space: O(n) - results list grows to hold one entry per processor
## time: O(n) - one hasattr check plus one process() call per processor

def process_all_ugly(processors, amount):
    results = []  # O(1) | O(1)
    for p in processors:  # O(1) | O(n)
        if hasattr(p, "process"):  # O(1) | O(1)
            results.append(p.process(amount))  # O(n) | O(1)
    return results  # O(1) | O(1)


# Space - Time Complexity analysis:
## space: O(n) - result list grows to hold one entry per processor
## time: O(n) - one process() call per processor, no duck-typing check needed - the ABC guarantees it exists

def process_all(processors, amount):
    return [p.process(amount) for p in processors]  # O(n) | O(n)


# Tests:
def validate():
    cases = [
        ([CreditCardProcessor(), PayPalProcessor()], 100,
         ["Charged $100 to credit card", "Paid $100 via PayPal"]),
        ([PayPalProcessor()], 50, ["Paid $50 via PayPal"]),
        ([], 10, []),
    ]
    for fn in (process_all_ugly, process_all):
        for processors, amount, expected in cases:
            result = fn(processors, amount)
            assert result == expected, (
                f"{fn.__name__}({processors!r}, {amount!r}): expected {expected!r}, got {result!r}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    validate()
