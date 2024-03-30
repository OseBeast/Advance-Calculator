from app.commands import Command
from calculator import save_history
import logging 

#Plugin used for handler to execute the save history algorithm
class SaveCommand(Command):
    def execute(self):
        save_history(input("What name should the file have:"))



