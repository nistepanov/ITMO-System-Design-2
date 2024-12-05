import turtle
from pathlib import Path

from entities.abstract_object import AbstractObject


class Item(AbstractObject):
    def __init__(self):
        super().__init__()
        self.penup()
        turtle.register_shape(super().get_resources_path() + "/item.gif")
        self.shape(super().get_resources_path() + "/item.gif")


    @staticmethod
    def get_label():
        return "T"
