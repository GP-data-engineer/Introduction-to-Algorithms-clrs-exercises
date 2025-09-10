# src/Chapter03/Problem_3_4.py
# Implementations of properties (a)–(g) for asymptotic notation relationships.
# Each property returns True or False according to whether the statement is
# generally true in asymptotic analysis.
import math

def is_big_o(f, g):
    C = 2
    for n in range(10, 1000, 100):
        if g(n) == 0:
            return False
        if f(n) > C * g(n):
            return False
    return True

def property_a():
    f = lambda n: n
    g = lambda n: n**2
    return is_big_o(f, g) and is_big_o(g, f)

def property_b():
    f = lambda n: n
    g = lambda n: n
    limit_ratio = f(10**6) / g(10**6)
    return is_big_o(f, g) and (limit_ratio == 0)

def property_c():
    f = lambda n: n**2
    g = lambda n: n**3
    if not is_big_o(f, g):
        return False
    log_f = lambda n: math.log(f(n))
    log_g = lambda n: math.log(g(n))
    return is_big_o(log_f, log_g)

def property_d():
    f = lambda n: n**2
    g = lambda n: n**2
    if not (is_big_o(f, g) and is_big_o(g, f)):
        return False
    f_sq = lambda n: f(n)**2
    g_sq = lambda n: n**4
    return is_big_o(f_sq, g_sq) and is_big_o(g_sq, f_sq)

def property_e():
    f = lambda n: n
    g = lambda n: n**2
    return is_big_o(f, g) and is_big_o(g, f)

def property_f():
    f = lambda n: n
    g = lambda n: n**2
    return is_big_o(f, g)

def property_g():
    f = lambda n: n
    g = lambda n: n**2
    h = lambda n: n**3
    return is_big_o(f, g) and is_big_o(g, h) and is_big_o(f, h)

def all_properties():
    return {
        "a": property_a(),
        "b": property_b(),
        "c": property_c(),
        "d": property_d(),
        "e": property_e(),
        "f": property_f(),
        "g": property_g()
    }

if __name__ == "__main__":
    print("Property results:")
    for key, value in all_properties().items():
        print(f"{key}: {value}")
