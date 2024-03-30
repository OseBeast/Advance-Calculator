'''My History Calculator Test'''
from calculator import *
from pandas.testing import assert_frame_equal
import pandas as pd
import os.path
         
def test_load_history():
    details = {
        'value1': [1,2,2,3],
        'symbol': ['+','-','*','/'],
        'value2':[2,3,2,2],
        'result':[3.0, -1.0, 4.0, 1.5],
        #'':[0,1,2,3]
    }
    ansDF = pd.DataFrame(details)
    test = History()
    test.load_history("test.csv")
    assert_frame_equal(test.df[['value1', 'symbol', 'value2', 'result']], ansDF, check_dtype=False)

def test_save_history():
    save_history("test_save.csv")
    path = 'test_save.csv'
    assert os.path.isfile(path) == True

def test_delete():
    add(1,2)
    subtract(2,2)
    delete_history()
    assert get_dataframe().empty == True

def test_clear():
    add(1,2)
    subtract(2,2)
    clear_history()
    assert get_dataframe().empty == True
