from app.commands import Command
from calculator import subtract
import logging 



class SubtractCommand(Command):
    def execute(self):
        a=int(input("Enter value one:"))
        logging.info("User entered the number: " + str(a))
        b=int(input("Enter value two:"))
        logging.info("User entered the number: " + str(b))
        print(subtract(a,b))
        logging.info("User Answer: " + str(subtract(a,b)))