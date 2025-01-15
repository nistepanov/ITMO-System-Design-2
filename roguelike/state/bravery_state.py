import typing

from roguelike.algorithms import agressive_algo
from roguelike.state import default_state, mob_state


class BraveryState(mob_state.MobState):
    """BraveryState logic."""

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def move(entity: typing.Any, game_map: typing.Any) -> tuple[float, float] | None:
        """Move logic.

        Args:
            entity:mob.Mob
            game_map:map.GameMap

        Returns:
            tuple[float, float] | None: Description of return value
        """
        if entity.health != entity.maxHealth:
            entity.state = default_state.DefaultState
            return None

        return agressive_algo.AgressiveAlgo().move(entity=entity, game_map=game_map)
