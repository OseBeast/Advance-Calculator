import sys
from app.commands import Command

#Plugin used for handler to execute the correct algorithm to exit the program
class ExitCommand(Command):
    def execute(self):
        sys.exit("Exiting...")
