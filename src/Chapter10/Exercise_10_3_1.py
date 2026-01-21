# Exercise 10.3-1 — CLRS
# EN: Illustrate multitable representation of doubly linked list and compare with single-table version.
# PL: Zilustruj wielotablicową reprezentację listy dwukierunkowej i porównaj z jednotablicową.

def multitable_representation(seq):
    n = len(seq)
    key = seq
    prev = [None] + list(range(n - 1))
    next = list(range(1, n)) + [None]
    return {"key": key, "prev": prev, "next": next}

def single_table_representation(seq):
    table = [{"key": k, "prev": i - 1 if i > 0 else None, "next": i + 1 if i < len(seq) - 1 else None}
             for i, k in enumerate(seq)]
    return table

if __name__ == "__main__":
    seq = [13, 4, 8, 19, 5, 11]
    print("Wielotablicowa reprezentacja:")
    print(multitable_representation(seq))
    print("Jednotablicowa reprezentacja:")
    print(single_table_representation(seq))
