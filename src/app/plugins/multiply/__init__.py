from app.commands import Command
from calculator import multiply



class MultiplyCommand(Command):
    def execute(self):
        a=int(input("Enter value one:"))
        b=int(input("Enter value two:"))
        print(multiply(a,b))