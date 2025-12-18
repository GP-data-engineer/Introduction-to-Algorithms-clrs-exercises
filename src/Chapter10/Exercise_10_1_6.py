# Exercise 10.1-6 (EN): Implement a queue using two stacks and analyze operation time.
# Exercise 10.1-6 (PL): Zaimplementuj kolejkę za pomocą dwóch stosów i oszacuj czas operacji.

class QueueViaStacks:
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def enqueue(self, x):
        self.inbox.append(x)

    def dequeue(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        if not self.outbox:
            raise IndexError("Queue underflow")
        return self.outbox.pop()

    def state(self):
        return self.outbox[::-1] + self.inbox

if __name__ == "__main__":
    q = QueueViaStacks()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Stan kolejki:", q.state())
    print("Usunięto:", q.dequeue())
    q.enqueue(4)
    print("Stan kolejki:", q.state())
