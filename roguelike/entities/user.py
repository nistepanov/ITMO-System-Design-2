import turtle
from typing import List

from entities.abstract_object import AbstractObject
from entities.item import Item, Shield, Weapon


class User(AbstractObject):
    
    _health: int
    _move_size: int
    _damage: int
    _speed: int
    _active_inventory: List[Item]
    _passive_inventory: List[Item]

    def __init__(self, move_size):
        super().__init__()
        turtle.register_shape(super().get_resources_path() + "/hero.gif")
        self.shape(super().get_resources_path() + "/hero.gif")
        self._health = 300
        self._move_size = move_size
        self._damage = 10
        self._active_inventory = []
        self._passive_inventory = []
        self.experience = 0
        self.level = 1
        self.penup()
        self.speed(3)

    @staticmethod
    def get_label():
        return "P"

    def shift_up(self, map):
        x = self.xcor()
        y = self.ycor() + self._move_size
        if map.check_walls(x, y):
            self.goto(x, y)

    def shift_down(self, map):
        x = self.xcor()
        y = self.ycor() - self._move_size
        if map.check_walls(x, y):
            self.goto(x, y)

    def shift_left(self, map):
        x = self.xcor() - self._move_size
        y = self.ycor()
        if map.check_walls(x, y):
            self.goto(x, y)

    def shift_right(self, map):
        x = self.xcor() + self._move_size
        y = self.ycor()
        if map.check_walls(x, y):
            self.goto(x, y)

    def get_item(self, map):
        for i, item in enumerate(map.items):
            if item.xcor() == self.xcor() and item.ycor() == self.ycor():
                self._active_inventory.append(item)
                if isinstance(item, Weapon):
                    self._damage += item.bonus_value
                elif isinstance(item, Shield):
                    self._health += item.bonus_value
                item.hideturtle()
                return

    def throw_item(self):
        item = self._active_inventory[0]
        self._active_inventory.remove(item)
        if isinstance(item, Weapon):
            self._damage -= item.bonus_value
        elif isinstance(item, Shield):
            self._health -= item.bonus_value
        self._passive_inventory.append(item)


