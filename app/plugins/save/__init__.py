from app.commands import Command
from calculator import save_history
import logging 





class SaveCommand(Command):
    def execute(self):
        save_history(input("What name should the file have:"))



