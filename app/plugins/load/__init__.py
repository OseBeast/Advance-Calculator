from app.commands import Command
from calculator import load_history
import logging 





class LoadCommand(Command):
    def execute(self):
        load_history(input("What is the name to load?:"))