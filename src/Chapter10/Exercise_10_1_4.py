# Exercise 10.1-4 (EN): Extend ENQUEUE and DEQUEUE procedures to detect overflow and underflow errors.
# Exercise 10.1-4 (PL): Rozszerz procedury ENQUEUE i DEQUEUE o wykrywanie błędów przepełnienia i niedomiaru.

class SafeQueue:
    def __init__(self, size):
        self.Q = [None] * size
        self.head = 0
        self.tail = 0
        self.size = size
        self.count = 0

    def enqueue(self, x):
        if self.count == self.size:
            raise OverflowError("Queue overflow")
        self.Q[self.tail] = x
        self.tail = (self.tail + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise IndexError("Queue underflow")
        val = self.Q[self.head]
        self.Q[self.head] = None
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return val

    def state(self):
        return self.Q

if __name__ == "__main__":
    q = SafeQueue(3)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    try:
        q.enqueue(40)
    except OverflowError as e:
        print("Błąd przepełnienia:", e)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    try:
        q.dequeue()
    except IndexError as e:
        print("Błąd niedomiaru:", e)
    print("Stan kolejki:", q.state())
