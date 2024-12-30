import typing

from roguelike.algorithms import coward_algo
from roguelike.state import bravery_state, mob_state, panic_state


def check_is_someone_near(entity: typing.Any, game_map: typing.Any) -> bool:
    """check_is_someone_near logic.

    Args:
        entity: mob.Mob
        game_map: map.GameMap

    Returns:
        bool: Description of return value
    """
    x = entity.xcor()
    y = entity.ycor()
    return any(abs(mob.xcor() - x) and abs(mob.ycor() - y) for mob in game_map.mobs)


class DefaultState(mob_state.MobState):
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
        if entity.health < entity.maxHealth - 3 and entity.algo != coward_algo.CowardAlgo:
            entity.state = panic_state.PanicState
            return None
        if entity.health == entity.maxHealth and check_is_someone_near(entity, game_map):
            entity.state = bravery_state.BraveryState
            return None

        return entity.algo.move(entity=entity, game_map=game_map)
