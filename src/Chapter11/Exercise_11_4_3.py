# Exercise 11.4-3 — CLRS
# EN: Expected number of probes for successful and unsuccessful search.
# PL: Oczekiwana liczba sprawdzeń dla sukcesu i porażki.

def expected_probes(alpha):
    fail = 1 / (1 - alpha)
    success = (1 / alpha) * (1 / (1 - alpha))
    return success, fail

if __name__ == "__main__":
    for a in [0.75, 0.875]:
        s, f = expected_probes(a)
        print(f"α={a}: success={s:.2f}, fail={f:.2f}")
