from app.commands import Command
from calculator import subtract



class SubtractCommand(Command):
    def execute(self):
        a=int(input("Enter value one:"))
        b=int(input("Enter value two:"))
        print(subtract(a,b))