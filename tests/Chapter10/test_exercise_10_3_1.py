from src.Chapter10.Exercise_10_3_1 import multitable_representation, single_table_representation

def test_multitable_structure():
    seq = [1, 2, 3]
    rep = multitable_representation(seq)
    assert rep["key"] == [1, 2, 3]
    assert rep["prev"] == [None, 0, 1]
    assert rep["next"] == [1, 2, None]

def test_single_table_structure():
    seq = [10, 20]
    rep = single_table_representation(seq)
    assert rep[0]["key"] == 10
    assert rep[0]["next"] == 1
    assert rep[1]["prev"] == 0
