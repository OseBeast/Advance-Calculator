============================= test session starts ==============================
platform linux -- Python 3.10.12, pytest-8.0.0, pluggy-1.4.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/solokid11/Advance-Calculator
configfile: pytest.ini
testpaths: tests
plugins: pylint-0.21.0, cov-4.1.0, Faker-23.1.0
collecting ... collected 15 items

tests/test_app.py::test_app_start_add_command PASSED                     [  6%]
tests/test_app.py::test_app_start_subtract_command PASSED                [ 13%]
tests/test_app.py::test_app_start_multiply_command PASSED                [ 20%]
tests/test_app.py::test_app_start_divide_command PASSED                  [ 26%]
tests/test_app.py::test_app_start_menu_command FAILED                    [ 33%]
tests/test_app.py::test_app_start_unknown_command PASSED                 [ 40%]
tests/test_calculator.py::test_addition PASSED                           [ 46%]
tests/test_calculator.py::test_subtraction PASSED                        [ 53%]
tests/test_calculator.py::test_multiplication PASSED                     [ 60%]
tests/test_calculator.py::test_division PASSED                           [ 66%]
tests/test_calculator.py::test_divide_by_zero PASSED                     [ 73%]
tests/test_history.py::test_history FAILED                               [ 80%]
tests/test_history.py::test_load_history PASSED                          [ 86%]
tests/test_history.py::test_save_history PASSED                          [ 93%]
tests/test_history.py::test_delete PASSED                                [100%]

=================================== FAILURES ===================================
_________________________ test_app_start_menu_command __________________________

capfd = <_pytest.capture.CaptureFixture object at 0x7f421d4bd660>
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f421d4bd6f0>

>   ???
E   AssertionError: assert 'add \nsubtract \nmultiply \ndivide \nexit' in 'Type the command to select the following:\n                add: Adds two numbers\n                subtract: Subtracts two numbers\n                multiply: Multiplies two numbers\n                divide: Divides two numbers\n                load: Load history from a csv file which will add to the current history\n                save: Save the current history\n                delete: Deletes the history\n                clear: Clears the history from display \n                exit: Exits out of the program   \n        \n   value1 symbol  value2  result\n0       1      +       2     3.0\n1       2      -       1     1.0\n2       3      *       3     9.0\n3       9      /       3     3.0\nNo such command: menu\nType the command to select the following:\n                add: Adds two numbers\n                subtract: Subtracts two numbers\n                multiply: Multiplies two numbers\n                divide: Divides two numbers\n                load: Load history from a csv file which will add to the current history\n                save: Save the current history\n                delete: Deletes the history\n                clear: Clears the history from display \n                exit: Exits out of the program   \n        \n   value1 symbol  value2  result\n0       1      +       2     3.0\n1       2      -       1     1.0\n2       3      *       3     9.0\n3       9      /       3     3.0\n'

/home/solokid11/Advance-Calculator/src/tests/test_app.py:79: AssertionError
_________________________________ test_history _________________________________

    def test_history():
        '''Test that addition function works '''
        clear_history()
        add(2,2)
        subtract(2,2)
        multiply(3,3)
        divide(9,3)
        divide(9,0)
>       assert get_history() == [
            (2, '+', 2, 4),
            (2, '-', 2, 0),
            (3, '*', 3, 9),
            (9, '/', 3, 3.0),
            (9, '/', 0, 'Error: Cannot divide by zero')
            ]
E       AssertionError: assert [(1, '+', 2, ...', 2, 0), ...] == [(2, '+', 2, ...ide by zero')]
E         
E         At index 0 diff: (1, '+', 2, 3) != (2, '+', 2, 4)
E         Left contains 9 more items, first extra item: (2, '-', 2, 0)
E         
E         Full diff:
E           [
E         +     (...
E         
E         ...Full output truncated (84 lines hidden), use '-vv' to show

tests/test_history.py:17: AssertionError
----------------------------- Captured stderr call -----------------------------
c]104[!p[?3;4l[4l>[?69l
=============================== warnings summary ===============================
tests/test_history.py::test_load_history
  /home/solokid11/Advance-Calculator/calculator/history.py:31: FutureWarning: The behavior of DataFrame concatenation with empty or all-NA entries is deprecated. In a future version, this will no longer exclude empty or all-NA columns when determining the result dtypes. To retain the old behavior, exclude the relevant entries before the concat operation.
    self.df = pd.concat([self.df,pd.read_csv(filename)])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ============================
FAILED tests/test_app.py::test_app_start_menu_command - AssertionError: asser...
FAILED tests/test_history.py::test_history - AssertionError: assert [(1, '+',...
=================== 2 failed, 13 passed, 1 warning in 1.29s ====================
