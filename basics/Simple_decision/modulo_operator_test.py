from modulo_operator import *


def test_is_an_odd_number():
    assert is_odd_number(3) == True
    assert is_odd_number(5) == True
    assert is_odd_number(7) == True
    assert is_odd_number(9) == True
    assert is_odd_number(11) == True


def test_isnot_an_odd_number():
    assert is_odd_number(2) == False
    assert is_odd_number(4) == False
    assert is_odd_number(50) == False
    assert is_odd_number(1010) == False

