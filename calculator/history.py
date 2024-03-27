'''history script'''
class History:
    '''history class'''

    def __init__(self):
        self.history = []

    def store_calculation(self, a, symbol, b, result):
        '''storing function'''
        self.history.append((a, symbol, b, result))

    def get_history(self):
        '''get stored history function'''
        return self.history

    def clear_history(self):
        '''clear stored history'''
        self.history.clear()
