import math
import pytest
from src.Chapter03.Problem_3_2 import analyze_pair

def test_n_vs_n_squared():
    """
    n vs n^2:
    n grows slower than n^2 → O and o, not Ω or ω, not Θ.
    """
    n_vals = [10**k for k in range(2, 6)]
    result = analyze_pair(lambda n: n, lambda n: n**2, n_vals)
    assert result["O"] is True
    assert result["o"] is True
    assert result["Omega"] is False
    assert result["omega"] is False
    assert result["Theta"] is False

def test_sqrt_n_vs_n_sin_i():
    """
    sqrt(n) vs n^sin(i), where i in [0,1]:
    For i=1, n^sin(i) = n, so sqrt(n) grows slower → O and o.
    """
    i = 1
    n_vals = [10**k for k in range(2, 6)]
    result = analyze_pair(lambda n: math.sqrt(n), lambda n: n**math.sin(i), n_vals)
    assert result["O"] is True
    assert result["o"] is True
    assert result["Omega"] is False
    assert result["omega"] is False
    assert result["Theta"] is False

def test_n_power_i_vs_log_n():
    """
    n^i vs log(n), for i>0:
    Polynomial grows faster than log → Ω and ω.
    """
    i = 0.5
    n_vals = [10**k for k in range(2, 6)]
    result = analyze_pair(lambda n: n**i, lambda n: math.log(n), n_vals)
    assert result["O"] is False
    assert result["o"] is False
    assert result["Omega"] is True
    assert result["omega"] is True
    assert result["Theta"] is False

def test_n_squared_vs_n_power_k():
    """
    n^2 vs n^k:
    If k=2 → Θ, if k<2 → Ω, if k>2 → O.
    Here k=2 → Θ.
    """
    k = 2
    n_vals = [10**m for m in range(2, 6)]
    result = analyze_pair(lambda n: n**2, lambda n: n**k, n_vals)
    assert result["Theta"] is True

def test_log_n_vs_log_n_squared():
    """
    log(n) vs log(n^2) = 2log(n) → Θ.
    """
    n_vals = [10**m for m in range(2, 6)]
    result = analyze_pair(lambda n: math.log(n), lambda n: math.log(n**2), n_vals)
    assert result["Theta"] is True

def test_ln_n_power_i_vs_lg_n_power_i():
    """
    ln(n^i) vs lg(n^i):
    They differ by a constant factor → Θ.
    """
    i = 0.5
    n_vals = [10**m for m in range(2, 6)]
    result = analyze_pair(lambda n: math.log(n**i), lambda n: math.log(n**i, 10), n_vals)
    assert result["Theta"] is True

def test_lg_n_vs_lg_n_power_n():
    """
    lg(n) vs (lg(n))^n:
    (lg(n))^n grows much faster → O and o.
    """
    n_vals = [10**m for m in range(2, 6)]
    result = analyze_pair(lambda n: math.log(n, 10), lambda n: (math.log(n, 10))**n, n_vals)
    assert result["O"] is True
    assert result["o"] is True
    assert result["Omega"] is False
    assert result["omega"] is False
    assert result["Theta"] is False
