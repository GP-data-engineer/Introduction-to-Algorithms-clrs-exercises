import pytest
from Chapter02.Exercise_2_3_3 import T, formula


@pytest.mark.parametrize("n", [2, 4, 8, 16, 32, 64, 128])
def test_T_matches_formula(n):
    assert T(n) == formula(n)