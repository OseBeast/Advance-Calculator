from app.commands import Command
from calculator import multiply
import logging 


class MultiplyCommand(Command):
    def execute(self):
        a=int(input("Enter value one:"))
        logging.info("User entered the number: " + str(a))
        b=int(input("Enter value two:"))
        logging.info("User entered the number: " + str(b))
        logging.info("User Answer: " + str(multiply(a,b)))