import time
from abc import abstractmethod

from roguelike.algorithms import mob_algorithm
from roguelike.entities import mob
from roguelike.map import map


class AbstractDecorator(mob_algorithm.MobAlgorithm):
    """AbstractDecorator logic."""

    def __init__(self, confused_seconds: int, decoratee: mob_algorithm.MobAlgorithm) -> None:
        super().__init__()
        self.start_time = time.time()
        self.confused_seconds = confused_seconds
        self.decoratee = decoratee

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
