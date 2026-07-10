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
        pass


class PayPalProcessor(PaymentProcessor):
    def process(self, amount):
        pass


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

def process_all_ugly(processors, amount):
    pass


# Space - Time Complexity analysis:
## space:
## time:

def process_all(processors, amount):
    return process_all_ugly(processors, amount)


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
    # validate()
    print(process_all_ugly([CreditCardProcessor(), PayPalProcessor()], 100))
    print(process_all_ugly([PayPalProcessor()], 50))
    print(process_all_ugly([], 10))
