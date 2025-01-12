import turtle
import typing

from roguelike.entities.mob import Mob


class SimpleMob(Mob):
    """Dragon mob class."""

    def __init__(self, algo: typing.Any) -> None:
        super().__init__(algo)
        self.health = 3
        self.maxHealth = self.health
        self.damage = 1
        turtle.register_shape(super().get_resources_path() + '/simple-mob.gif')
        self.shape(super().get_resources_path() + '/simple-mob.gif')
