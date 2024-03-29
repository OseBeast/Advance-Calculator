from app.commands import Command
from calculator import add
import logging 



class AddCommand(Command):
    def execute(self):
        val1= input("Enter value one:")
        a=int(val1)
        logging.info("User entered the number: " + str(a))
        
        b=int(input("Enter value two:"))
        if (a.isdecimal() or b.isdecimal()) == False:
            print("The values have to be numbers. You will be directed to the menu to try again")
        else:
            logging.info("User entered the number: " + str(b))
            logging.info("User Answer: " + str(add(a,b)))