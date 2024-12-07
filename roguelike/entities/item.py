import turtle
from pathlib import Path

from entities.abstract_object import AbstractObject


class Item(AbstractObject):
    def __init__(self, bonus_value: int):
        super().__init__()
        self.bonus_value = bonus_value
        # self.penup()
        # turtle.register_shape(super().get_resources_path() + "/item.gif")
        # self.shape(super().get_resources_path() + "/item.gif")


    @staticmethod
    def get_label():
        raise NotImplementedError
    

class Weapon(Item):

    def __init__(self, bonus_value):
        super().__init__(bonus_value)
        self.penup()
        turtle.register_shape(super().get_resources_path() + "/weapon.gif")
        self.shape(super().get_resources_path() + "/weapon.gif")

    @staticmethod
    def get_label():
        return "W"
    
class Shield(Item):

    def __init__(self, bonus_value):
        super().__init__(bonus_value)
        self.penup()
        turtle.register_shape(super().get_resources_path() + "/shield.gif")
        self.shape(super().get_resources_path() + "/shield.gif")

    @staticmethod
    def get_label():
        return "S"
    

    