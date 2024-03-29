from app.commands import Command
from calculator import show_history
import logging 





class Show_HistoryCommand(Command):
    def execute(self):
        show_history()