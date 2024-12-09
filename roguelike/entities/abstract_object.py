import turtle
from abc import abstractmethod
from pathlib import Path


class AbstractObject(turtle.Turtle):
    """AbstractObject logic."""

    @abstractmethod
    def __init__(self) -> None:
        turtle.Turtle.__init__(self)
        self.penup()

    @staticmethod
    @abstractmethod
    def get_label() -> str:
        """get_label logic."""
        return ''

    @staticmethod
    def get_resources_path() -> str:
        """get_resources_path logic."""
        return str(Path(__file__).resolve().parent.parent.parent) + '/resources'
