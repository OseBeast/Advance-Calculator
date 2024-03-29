import sys
from app.commands import Command


class MenuCommand(Command):
    def execute(self):
        print("add \nsubtract \nmultiply \ndivide \nload \nsave \nclear \ndelete \nexit")