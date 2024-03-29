from app.commands import Command
from calculator import clear_history
import logging 





class ClearCommand(Command):
    def execute(self):
        clear_history()