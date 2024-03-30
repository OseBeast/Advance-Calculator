from app.commands import Command
from calculator import add
import logging 


#command used 
class AddCommand(Command):
    def execute(self):
        val1= input("Enter value one:")
        try:
            a=int(val1)
            logging.info("User entered the number: " + str(a))

            b=int(input("Enter value two:"))
            logging.info("User entered the number: " + str(b))
            logging.info("User Answer: " + str(add(a,b)))
        except:
            print("The values have to be numbers. You will be directed to the menu to try again")