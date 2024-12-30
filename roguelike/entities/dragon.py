import turtle
import typing

from roguelike.entities.mob import Mob


class Dragon(Mob):
    """Dragon mob class."""

    def __init__(self, algo: typing.Any) -> None:
        super().__init__(algo)
        self.health = 10
        self.maxHealth = 10
        self.damage = 5
        self.speed(1)
        turtle.register_shape(super().get_resources_path() + '/dragon.gif')
        self.shape(super().get_resources_path() + '/dragon.gif')
