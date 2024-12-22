from abc import abstractmethod

from roguelike.entities import mob
from roguelike.map import map


class MobAlgorithm:
    """MobAlgorithm logic."""

    def __init__(self) -> None:
        pass

    @abstractmethod
    def move(self, entity: mob.Mob, game_map: map.GameMap) -> tuple[float, float] | None:
        """Move logic.

        Args:
            entity (mob.Mob): Description of entity.
            game_map (GameMap): Description of game_map.

        Returns:
            None: Description of return value
        """
        pass
