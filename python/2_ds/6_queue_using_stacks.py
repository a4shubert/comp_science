# Theory:
## A stack is LIFO, a queue is FIFO - opposite orderings. You can still
## build a queue purely out of two stacks: push everything onto an
## "in" stack, and whenever you need to dequeue, if the "out" stack is
## empty, dump the entire "in" stack onto it (reversing the order), then
## pop from "out". Each element gets moved from "in" to "out" at most
## once over its lifetime, so even though a single dequeue can look
## expensive (O(n) if it triggers a dump), the *amortized* cost per
## operation averages out to O(1) - this "amortized analysis" idea
## (occasional expensive operations that are individually rare) shows up
## constantly: dynamic array resizing, hash table rehashing, and this
## two-stack queue all share the same argument.


# Packages:
## list - Python's list works as a stack via append()/pop() from the end
## collections.deque - the "right way" to get an actual O(1)-both-ends queue directly, without needing two stacks at all


# Task:
## Design a FIFO queue using only two stacks. Implement:
## - push(x): add x to the back of the queue.
## - pop(): remove and return the value at the front of the queue.
## - peek(): return the value at the front of the queue without removing it.
## Test1: Inputs: ops=[push(1), push(2), peek(), pop(), pop()]   Outputs: [None, None, 1, 1, 2]
## Test2: Inputs: ops=[push(1), pop(), push(2), push(3), pop(), pop()]   Outputs: [None, 1, None, None, 2, 3]
## Test3: Inputs: ops=[push(5), peek(), peek()]   Outputs: [None, 5, 5]
## Hint:
## Ugly way: list with insert(0, x) - push at the front directly, an O(n)
## shift of every existing element each time.
## Right way: two stacks (in/out) - amortized O(1) push/pop by only
## reversing the "in" stack onto "out" when "out" runs dry.


# Solutions:

# Space - Time Complexity analysis:
## space:
## time:

class QueueUgly:
    def __init__(self):
        pass

    def push(self, x):
        pass

    def pop(self):
        pass

    def peek(self):
        pass


# Space - Time Complexity analysis:
## space:
## time:

class Queue:
    def __init__(self):
        pass

    def push(self, x):
        pass

    def pop(self):
        pass

    def peek(self):
        pass


# Tests:
def validate():
    scenarios = [
        ([("push", 1, None), ("push", 2, None), ("peek", None, None), ("pop", None, None), ("pop", None, None)],
         [None, None, 1, 1, 2]),
        ([("push", 1, None), ("pop", None, None), ("push", 2, None), ("push", 3, None), ("pop", None, None), ("pop", None, None)],
         [None, 1, None, None, 2, 3]),
        ([("push", 5, None), ("peek", None, None), ("peek", None, None)],
         [None, 5, 5]),
    ]
    for cls in (QueueUgly, Queue):
        for ops, expected in scenarios:
            q = cls()
            results = []
            for op, arg, _ in ops:
                if op == "push":
                    results.append(q.push(arg))
                elif op == "pop":
                    results.append(q.pop())
                else:
                    results.append(q.peek())
            assert results == expected, (
                f"{cls.__name__}: expected {expected}, got {results}"
            )
    print("SUCCESS")


if __name__ == "__main__":
    # validate()
    q1 = QueueUgly()
    print([q1.push(1), q1.push(2), q1.peek(), q1.pop(), q1.pop()])
    q2 = QueueUgly()
    print([q2.push(1), q2.pop(), q2.push(2), q2.push(3), q2.pop(), q2.pop()])
    q3 = QueueUgly()
    print([q3.push(5), q3.peek(), q3.peek()])
