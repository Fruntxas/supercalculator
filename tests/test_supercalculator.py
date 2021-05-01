from supercalculator.supercalculator import soma,diff,div,mult

def test_soma():
    assert soma(1,1) == 2

def test_diff():
    assert diff(1,1) == 0

def test_mult():
    assert mult(3,3) == 9

def test_div():
    assert div(20,4) == 5