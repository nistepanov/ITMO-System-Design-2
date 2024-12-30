import typing

from roguelike.algorithms import coward_algo
from roguelike.state import default_state, mob_state


class PanicState(mob_state.MobState):
    """DefaultState logic."""

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
        if entity.health >= entity.maxHealth - 3 and entity.algo != coward_algo.CowardAlgo:
            entity.state = default_state.DefaultState
            return None

        return coward_algo.CowardAlgo().move(entity=entity, game_map=game_map)
