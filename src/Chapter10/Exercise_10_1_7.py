# Exercise 10.1-7 (EN): Implement a stack using two queues. Estimate operation time.
# Exercise 10.1-7 (PL): Zaimplementuj stos za pomocą dwóch kolejek. Oszacuj czas działania operacji.

from collections import deque

class StackViaQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        # Dodajemy do pustej kolejki q2, potem przenosimy wszystko z q1 do q2
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        # Zamieniamy kolejki
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if not self.q1:
            raise IndexError("Stack underflow")
        return self.q1.popleft()

    def top(self):
        if not self.q1:
            raise IndexError("Stack is empty")
        return self.q1[0]

    def state(self):
        return list(self.q1)

if __name__ == "__main__":
    s = StackViaQueues()
    s.push(1)
    s.push(2)
    s.push(3)
    print("Stan stosu:", s.state())
    print("POP:", s.pop())
    s.push(4)
    print("Stan stosu:", s.state())
    print("TOP:", s.top())
