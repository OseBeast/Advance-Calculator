from abc import ABC, abstractmethod
import logging

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


'''Class that is used to handle commands made by the user. This makes it so the pluggins can be activated seamlessly'''
class CommandHandler:
    def __init__(self):
        self.commands = {}

    #This is used to register the commands for later use
    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    #This will execute the command selected by user.
    def execute_command(self, command_name: str):
        """ Look before you leap (LBYL) - Use when its less likely to work
        if command_name in self.commands:
            self.commands[command_name].execute()
        else:
            print(f"No such command: {command_name}")
        """
        """Easier to ask for forgiveness than permission (EAFP) - Use when its going to most likely work"""
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")
            logging.error("User Entered Bad Command:"  +  str(command_name))
