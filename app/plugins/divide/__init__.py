from app.commands import Command
from calculator import divide
import logging 


class DivideCommand(Command):
    def execute(self):
        try:
            a=int(input("Enter value one:"))
            logging.info("User entered the number: " + str(a))
            b=int(input("Enter value two:"))
            logging.info("User entered the number: " + str(b))
            logging.info("User Answer: " + str(divide(a,b)))
        except:
            print("Enter only numbers, you will be directed to the menu to try again.")
