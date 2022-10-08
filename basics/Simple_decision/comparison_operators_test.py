from comparison_operators import *

def test_number_comparison():
    assert number_comparison(1,2) == "first"
    assert number_comparison(2,1) == "second"
    assert number_comparison(2,2) == "equal"
