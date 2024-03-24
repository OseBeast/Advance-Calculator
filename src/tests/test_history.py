'''My History Calculator Test'''
from calculator import get_history, add, subtract, multiply, divide, clear_history

def test_history():
    '''Test that addition function works '''
    clear_history()
    add(2,2)
    subtract(2,2)
    multiply(3,3)
    divide(9,3)
    divide(9,0)
    assert get_history() == [
        (2, '+', 2, 4),
        (2, '-', 2, 0),
        (3, '*', 3, 9),
        (9, '/', 3, 3.0),
        (9, '/', 0, 'Error: Cannot divide by zero')
        ]
