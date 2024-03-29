from app.commands import Command
from calculator import delete_history
import logging 


class DeleteCommand(Command):
    def execute(self):
        delete_history()
        print("History has been deleted!")