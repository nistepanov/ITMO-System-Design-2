import turtle

from roguelike.entities import abstract_object
from roguelike.inventory.inventory import Inventory


# from roguelike.map import map


class User(abstract_object.AbstractObject):
    """User logic."""

    def __init__(self, health: int, damage: int, level: int, inventory: Inventory) -> None:
        super().__init__()
        turtle.register_shape(super().get_resources_path() + '/hero.gif')
        self.shape(super().get_resources_path() + '/hero.gif')
        self.health: int = health
        self.damage: int = damage
        self.experience = 0
        self.level = level
        self.inventory = inventory
        self.penup()
        self.speed(3)

    @staticmethod
    def get_label() -> str:
        """get_label logic.

        Returns:
            str: Description of return value
        """
        return 'P'
