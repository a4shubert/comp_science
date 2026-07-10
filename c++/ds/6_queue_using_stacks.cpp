// Theory:
// A stack is LIFO, a queue is FIFO - opposite orderings. You can still
// build a queue purely out of two stacks: push everything onto an "in"
// stack, and whenever you need to dequeue, if the "out" stack is empty,
// dump the entire "in" stack onto it (reversing the order), then pop
// from "out". Each element gets moved from "in" to "out" at most once
// over its lifetime, so even though a single dequeue can look expensive
// (O(n) if it triggers a dump), the *amortized* cost per operation
// averages out to O(1) - this "amortized analysis" idea (occasional
// expensive operations that are individually rare) shows up constantly:
// dynamic array resizing, hash table rehashing, and this two-stack queue
// all share the same argument.

// Headers & STL components:
// <stack> - std::stack, the two stacks (in/out) this design is built from
// <deque> - the "right way" to get an actual O(1)-both-ends queue directly, without needing two stacks at all
// <queue> - std::queue, the STL's own FIFO adaptor (usually deque-backed)

// Task:
// Design a FIFO queue using only two stacks. Implement:
// - push(x): add x to the back of the queue.
// - pop(): remove and return the value at the front of the queue.
// - peek(): return the value at the front of the queue without removing it.
// Test1: Inputs: ops=[push(1), push(2), peek(), pop(), pop()]   Outputs: {-, -, 1, 1, 2}
// Test2: Inputs: ops=[push(1), pop(), push(2), push(3), pop(), pop()]   Outputs: {-, 1, -, -, 2, 3}
// Test3: Inputs: ops=[push(5), peek(), peek()]   Outputs: {-, 5, 5}
// Hint:
// Ugly way: std::vector with insert(begin(), x) - push at the front
// directly, an O(n) shift of every existing element each time.
// Right way: two stacks (in/out) - amortized O(1) push/pop by only
// reversing the "in" stack onto "out" when "out" runs dry.

// Solutions:
#include <cassert>
#include <iostream>
#include <stack>
#include <vector>

// Space - Time Complexity analysis:
// space:
// time:

class QueueUgly {
public:
    void push([[maybe_unused]] int x) {
        // TODO: implement
    }

    int pop() {
        // TODO: implement
        return -1;
    }

    int peek() {
        // TODO: implement
        return -1;
    }
};

// Space - Time Complexity analysis:
// space:
// time:

class Queue {
public:
    void push([[maybe_unused]] int x) {
        // TODO: implement
    }

    int pop() {
        // TODO: implement
        return -1;
    }

    int peek() {
        // TODO: implement
        return -1;
    }
};

// Tests:
template <typename QueueT>
void run_queue_tests() {
    {
        QueueT q;
        q.push(1);
        q.push(2);
        assert(q.peek() == 1);
        assert(q.pop() == 1);
        assert(q.pop() == 2);
    }
    {
        QueueT q;
        q.push(1);
        assert(q.pop() == 1);
        q.push(2);
        q.push(3);
        assert(q.pop() == 2);
        assert(q.pop() == 3);
    }
    {
        QueueT q;
        q.push(5);
        assert(q.peek() == 5);
        assert(q.peek() == 5);
    }
}

void validate() {
    run_queue_tests<QueueUgly>();
    run_queue_tests<Queue>();
    std::cout << "SUCCESS" << std::endl;
}

int main() {
    validate();
    return 0;
}
