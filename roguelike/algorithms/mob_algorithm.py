import typing
from abc import abstractmethod


class MobAlgorithm:
    """MobAlgorithm logic."""

    def __init__(self) -> None:
        pass

    @abstractmethod
    def move(self, entity: typing.Any, game_map: typing.Any) -> tuple[float, float] | None:
        """Move logic.

        Args:
            entity (mob.Mob): Description of entity.
            game_map (GameMap): Description of game_map.

        Returns:
            None: Description of return value
        """
        pass
