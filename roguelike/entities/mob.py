import typing

# from roguelike.algorithms import simple_algo
from roguelike.entities import abstract_object


# from roguelike.map.map import GameMap


class Mob(abstract_object.AbstractObject):
    """Mob logic."""

    def __init__(self, algo: typing.Any) -> None:
        super().__init__()
        self.algo = algo
        self.health = 3
        self.damage = 1
        self.penup()
        self.speed(3)

    @staticmethod
    def get_label() -> str:
        """get_label logic."""
        return 'M'

    def move(self, game_map: typing.Any) -> tuple[float, float]:
        """Move logic.

        Args:
            game_map (GameMap): Description of game_map.
        """
        return self.algo.move(self, game_map)
