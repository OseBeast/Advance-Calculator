'''calcluate script'''
class Calculate:
    '''calculate class'''
    def __init__(self) :
        self.a = 0
        self.b = 0

    def add(self, a, b):
        '''addtion function'''
        return a + b

    def subtract(self, a, b):
        '''subtraction function'''
        return a - b

    def multiply(self, a, b):
        '''multiplication function'''
        return a * b

    def divide(self, a, b):
        '''divide function'''
        if b == 0 :
            return "Error: Cannot divide by zero"
        return a / b
