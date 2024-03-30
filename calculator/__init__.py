'''main script'''
from calculator.calculate import Calculate
from calculator.history import History
past_calc = History()

number_cruncher = Calculate()


@staticmethod
def add(a,b):
    '''store history of add operations and return value'''
    #History.store_calculation(past_calc, a, "+", b, number_cruncher.add(a,b))
    past_calc.store_calculation(a, "+", b, number_cruncher.add(a,b))
    return number_cruncher.add(a,b)

@staticmethod
def subtract(a,b):
    '''store history of sub operations and return value'''
    History.store_calculation(past_calc, a, '-', b, number_cruncher.subtract(a,b))
    return number_cruncher.subtract(a,b)

@staticmethod
def multiply(a,b):
    '''store history of multi operations and return value'''
    History.store_calculation(past_calc, a, '*', b, number_cruncher.multiply(a,b))
    return number_cruncher.multiply(a,b)

@staticmethod
def divide(a,b):
    '''store history of div operations and return value'''
    History.store_calculation(past_calc, a, '/', b, number_cruncher.divide(a,b))
    return number_cruncher.divide(a,b)

@staticmethod
def get_history():
    ''' return stored history'''
    return past_calc.get_history()

@staticmethod
def clear_history():
    ''' clears history for tests'''
    past_calc.clear_history()

@staticmethod
def load_history(filename):
    ''' clears history for tests'''
    past_calc.load_history(filename)

@staticmethod
def save_history(filename):
    ''' clears history for tests'''
    past_calc.save_history(filename)

@staticmethod
def delete_history():
    ''' clears history for tests'''
    past_calc.delete_history()

@staticmethod
def clear_history():
    ''' clears history for tests'''
    past_calc.clear_history()

@staticmethod
def show_history():
    ''' clears history for tests'''
    past_calc.show_history()

@staticmethod
def get_dataframe():
    ''' clears history for tests'''
    return past_calc.get_dataframe()