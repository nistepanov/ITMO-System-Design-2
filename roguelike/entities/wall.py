import turtle
from pathlib import Path

from entities.abstract_object import AbstractObject


class Wall(AbstractObject):
    def __init__(self):
        super().__init__()
        turtle.register_shape(super().get_resources_path() + "/wall.gif")
        self.shape(super().get_resources_path() + "/wall.gif")
        self.penup()
        self.level = 1


    @staticmethod
    def get_label():
        return "W"
