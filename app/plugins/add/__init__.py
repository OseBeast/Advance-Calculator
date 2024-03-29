from app.commands import Command
from calculator import add
import logging 



class AddCommand(Command):
    def execute(self):
        a=int(input("Enter value one:"))
        logging.info("User entered the number: " + str(a))
        b=int(input("Enter value two:"))
        logging.info("User entered the number: " + str(b))
        logging.info("User Answer: " + str(add(a,b)))