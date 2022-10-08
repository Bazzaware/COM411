from pickle import FALSE
from modulo_operator import *


def test_is_an_odd_number():
    assert is_odd_number(3) == True


def test_isnot_an_odd_number():
    assert is_odd_number(2) == False

