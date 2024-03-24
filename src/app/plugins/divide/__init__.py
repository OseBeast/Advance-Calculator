from app.commands import Command
from calculator import divide



class DivideCommand(Command):
    def execute(self):
        a=int(input("Enter value one:"))
        b=int(input("Enter value two:"))
        print(divide(a,b))