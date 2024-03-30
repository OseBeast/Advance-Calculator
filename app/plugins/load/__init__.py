from app.commands import Command
from calculator import load_history
import logging 




#Plugin used for handler to execute the correct algorithm for multiplying
class LoadCommand(Command):
    def execute(self):
        load_history(input("What is the name to load?:"))