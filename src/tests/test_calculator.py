'''My Calculator Test'''
from calculator import add, subtract, multiply, divide

def test_addition():
    '''Test that addition function works '''    
    assert add(2,2) == 4

def test_subtraction():
    '''Test that subtraction function works '''    
    assert subtract(2,2) == 0

def test_multiplication():
    '''Test that multiplication function works '''    
    assert multiply(3,3) == 9

def test_division():
    '''Test that dividacation function works '''    
    assert divide(9,3) == 3

def test_divide_by_zero():
    '''Test that divide by zero function works '''    
    assert divide(9,0) == "Error: Cannot divide by zero"
