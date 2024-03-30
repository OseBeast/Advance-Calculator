from app.commands import Command
from calculator import multiply
import logging 

#Plugin used for handler to execute the correct algorithm for multiplying
class MultiplyCommand(Command):
    def execute(self):
        try:
            a=int(input("Enter value one:"))
            logging.info("User entered the number: " + str(a))
            b=int(input("Enter value two:"))
            logging.info("User entered the number: " + str(b))
            logging.info("User Answer: " + str(multiply(a,b)))
        except:
            print("You must enter numbers only. You will be directed to the main menu to try again")