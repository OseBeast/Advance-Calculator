from app.commands import Command
from calculator import add



class AddCommand(Command):
    def execute(self):
        a=int(input("Enter value one:"))
        b=int(input("Enter value two:"))
        print(add(a,b))
