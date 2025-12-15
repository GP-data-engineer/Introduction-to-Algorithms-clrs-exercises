# Exercise 10.1-5 (EN): Implement four O(1) operations for a deque stored in an array.
# Exercise 10.1-5 (PL): Zaimplementuj cztery operacje O(1) dla kolejki dwustronnej w tablicy.

class Deque:
    def __init__(self, size):
        self.D = [None] * size
        self.front = 0
        self.rear = 0
        self.size = size
        self.count = 0

    def push_front(self, x):
        if self.count == self.size:
            raise OverflowError("Deque overflow")
        self.front = (self.front - 1 + self.size) % self.size
        self.D[self.front] = x
        self.count += 1

    def push_back(self, x):
        if self.count == self.size:
            raise OverflowError("Deque overflow")
        self.D[self.rear] = x
        self.rear = (self.rear + 1) % self.size
        self.count += 1

    def pop_front(self):
        if self.count == 0:
            raise IndexError("Deque underflow")
        val = self.D[self.front]
        self.D[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return val

    def pop_back(self):
        if self.count == 0:
            raise IndexError("Deque underflow")
        self.rear = (self.rear - 1 + self.size) % self.size
        val = self.D[self.rear]
        self.D[self.rear] = None
        self.count -= 1
        return val

    def state(self):
        return self.D

if __name__ == "__main__":
    d = Deque(6)
    d.push_back(1)
    d.push_front(2)
    d.push_back(3)
    d.pop_front()
    d.push_front(4)
    d.pop_back()
    print("Stan deque:", d.state())
