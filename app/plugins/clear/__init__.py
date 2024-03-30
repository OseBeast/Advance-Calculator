from app.commands import Command
from calculator import clear_history
import logging 




#Plugin used for handler to execute the correct algorithim to clear the history 
class ClearCommand(Command):
    def execute(self):
        clear_history()