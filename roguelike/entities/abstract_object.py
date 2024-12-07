import turtle
from abc import abstractmethod
from pathlib import Path


class AbstractObject(turtle.Turtle):

    @abstractmethod
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()

    @staticmethod
    @abstractmethod
    def get_label():
        return ""

    @staticmethod
    def get_resources_path():
        return str(Path(__file__).resolve().parent.parent.parent) + "/resources"

