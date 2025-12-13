# Exercise 10.1-3 (EN): Simulate a sequence of ENQUEUE and DEQUEUE operations on a queue stored in array Q[1..6].
# Exercise 10.1-3 (PL): Zasymuluj ciąg operacji ENQUEUE i DEQUEUE na kolejce w tablicy Q[1..6].

class Queue:
    def __init__(self, size):
        self.Q = [None] * size
        self.head = 0
        self.tail = 0
        self.size = size

    def enqueue(self, x):
        self.Q[self.tail] = x
        self.tail = (self.tail + 1) % self.size

    def dequeue(self):
        val = self.Q[self.head]
        self.Q[self.head] = None
        self.head = (self.head + 1) % self.size
        return val

    def state(self):
        return self.Q

if __name__ == "__main__":
    q = Queue(6)
    q.enqueue(4)
    q.enqueue(1)
    q.enqueue(3)
    q.dequeue()
    q.enqueue(8)
    q.dequeue()
    print("Stan kolejki:", q.state())
