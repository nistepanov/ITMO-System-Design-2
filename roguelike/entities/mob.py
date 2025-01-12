import typing

from roguelike.entities import abstract_object
from roguelike.state.default_state import DefaultState


class Mob(abstract_object.AbstractObject):
    """Mob logic."""

    def __init__(self, algo: typing.Any) -> None:
        super().__init__()
        self.algo = algo
        self.health = 3
        self.maxHealth = self.health
        self.damage = 1
        self.penup()
        self.speed(3)
        self.state = DefaultState()

    @staticmethod
    def get_label() -> str:
        """get_label logic."""
        return 'M'

    def move(self, game_map: typing.Any) -> tuple[float, float] | None:
        """Move logic.

        Args:
            game_map (GameMap): Description of game_map.
        """
        return self.state.move(entity=self, game_map=game_map)
