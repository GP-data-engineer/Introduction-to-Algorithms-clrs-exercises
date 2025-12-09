# Exercise 10.1-2 (EN): Implement two stacks in one array A[1..n] with O(1) PUSH and POP vvv.
# Exercise 10.1-2 (PL): Zaimplementuj dwa stosy w jednej tablicy A[1..n] z operacjami PUSH i POP w czasie O(1).

class DualStack:
    def __init__(self, n):
        self.A = [None] * n
        self.top1 = -1
        self.top2 = n

    def push1(self, x):
        if self.top1 + 1 == self.top2:
            raise OverflowError("Stack overflow")
        self.top1 += 1
        self.A[self.top1] = x

    def push2(self, x):
        if self.top2 - 1 == self.top1:
            raise OverflowError("Stack overflow")
        self.top2 -= 1
        self.A[self.top2] = x

    def pop1(self):
        if self.top1 == -1:
            raise IndexError("Stack1 underflow")
        val = self.A[self.top1]
        self.A[self.top1] = None
        self.top1 -= 1
        return val

    def pop2(self):
        if self.top2 == len(self.A):
            raise IndexError("Stack2 underflow")
        val = self.A[self.top2]
        self.A[self.top2] = None
        self.top2 += 1
        return val

if __name__ == "__main__":
    ds = DualStack(6)
    ds.push1(1)
    ds.push2(9)
    ds.push1(2)
    ds.push2(8)
    print("Stan tablicy:", ds.A)
