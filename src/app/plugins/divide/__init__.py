from app.commands import Command
from calculator import divide
import logging 


class DivideCommand(Command):
    def execute(self):
        a=int(input("Enter value one:"))
        logging.info("User entered the number: " + str(a))
        b=int(input("Enter value two:"))
        logging.info("User entered the number: " + str(b))
        print(divide(a,b))
        logging.info("User Answer: " + str(divide(a,b)))
