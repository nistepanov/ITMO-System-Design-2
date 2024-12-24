import turtle
import typing

from roguelike.entities.mob import Mob


class Skeleton(Mob):
    """Skeleton mob class."""

    def __init__(self, algo: typing.Any) -> None:
        super().__init__(algo)
        self.health = 2
        self.damage = 1
        turtle.register_shape(super().get_resources_path() + '/skeleton.gif')
        self.shape(super().get_resources_path() + '/skeleton.gif')
