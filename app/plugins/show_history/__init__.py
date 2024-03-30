from app.commands import Command
from calculator import show_history
import logging 




#Plugin used for handler to execute the correct algorithm for showing history in the main menu
class Show_HistoryCommand(Command):
    def execute(self):
        show_history()