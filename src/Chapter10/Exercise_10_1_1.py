# Exercise 10.1-1 (EN): Simulate a sequence of PUSH and POP operations on a stack stored in array S[1..6].
# Exercise 10.1-1 (PL): Zasymuluj ciąg operacji PUSH i POP na stosie w tablicy S[1..6].

class Stack:
    def __init__(self, size):
        self.S = [None] * size
        self.top = -1

    def push(self, x):
        if self.top + 1 >= len(self.S):
            raise OverflowError("Stack overflow")
        self.top += 1
        self.S[self.top] = x

    def pop(self):
        if self.top == -1:
            raise IndexError("Stack underflow")
        val = self.S[self.top]
        self.S[self.top] = None
        self.top -= 1
        return val

    def state(self):
        return self.S

if __name__ == "__main__":
    stack = Stack(6)
    stack.push(4)
    stack.push(1)
    stack.push(3)
    stack.pop()
    stack.push(8)
    stack.pop()
    print("Stan stosu:", stack.state())
