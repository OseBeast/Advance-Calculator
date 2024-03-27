import sys
from app import App
from calculator.calculate import Calculate

number_cruncher = Calculate()
#Forces the program to start when ran from the command line.

if __name__ == '__main__':
    app = App().start()   # Starts an instance of class: App
