'''My History Calculator Test'''
import os.path
import pandas as pd
from pandas.testing import assert_frame_equal
from calculator import save_history,clear_history,delete_history,History,add,subtract,get_dataframe


def test_load_history():
    '''Load History Test'''
    details = {
        'value1': [1,2,2,3],
        'symbol': ['+','-','*','/'],
        'value2':[2,3,2,2],
        'result':[3.0, -1.0, 4.0, 1.5],
        #'':[0,1,2,3]
    }
    ans_df = pd.DataFrame(details)
    test = History()
    test.load_history("test.csv")
    assert_frame_equal(test.df[['value1', 'symbol', 'value2', 'result']], ans_df, check_dtype=False)

def test_save_history():
    '''Save History Test'''
    save_history("test_save.csv")
    path = 'test_save.csv'
    assert os.path.isfile(path) is True

def test_delete():
    '''Delete History Test'''
    add(1,2)
    subtract(2,2)
    delete_history()
    assert get_dataframe().empty is True

def test_clear():
    '''Clear History Test'''
    add(1,2)
    subtract(2,2)
    clear_history()
    assert get_dataframe().empty is True
