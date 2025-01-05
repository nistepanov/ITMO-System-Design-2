import turtle
import typing

from roguelike.entities.mob import Mob


class CopyMob(Mob):
    """CopyMob mob class."""

    def __init__(self, algo: typing.Any) -> None:
        super().__init__(algo)
        self.health = 1
        self.maxHealth = 1
        self.damage = 1
        self.speed(1)
        turtle.register_shape(super().get_resources_path() + '/copy.gif')
        self.shape(super().get_resources_path() + '/copy.gif')

    def clone(self) -> typing.Any:
        """Clone logic.

        Returns:
            Mob: Description of return value
        """
        return CopyMob(self.algo)
