import turtle
import typing

# from roguelike.algorithms import simple_algo
from roguelike.entities import abstract_object


# from roguelike.map.map import GameMap


class Mob(abstract_object.AbstractObject):
    """Mob logic."""

    def __init__(self, algo: typing.Any) -> None:
        super().__init__()
        self.algo = algo
        turtle.register_shape(super().get_resources_path() + '/simple-mob.gif')
        self.shape(super().get_resources_path() + '/simple-mob.gif')
        self.health = 100
        self.attack = 10
        self.penup()
        self.speed(3)

    @staticmethod
    def get_label() -> str:
        """get_label logic."""
        return 'M'

    def move(self, game_map: typing.Any) -> None:
        """Move logic.

        Args:
            game_map (GameMap): Description of game_map.
        """
        self.algo.move(self, game_map)
