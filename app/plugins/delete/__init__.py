from app.commands import Command
from calculator import delete_history
import logging 

#Plugin used for handler to execute the correct algorithm for deleting history
class DeleteCommand(Command):
    def execute(self):
        delete_history()
        print("History has been deleted!")