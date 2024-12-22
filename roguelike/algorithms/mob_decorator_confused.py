import typing
from random import randint

import time

from roguelike.algorithms import mob_decorator, mob_algorithm
from roguelike.entities import mob
from roguelike.map import map


class ConfusedDecorator(mob_decorator.AbstractDecorator):
    """SimpleAlgo logic."""

    def __init__(self, confused_seconds:int, decoratee : mob_algorithm.MobAlgorithm) -> None:
        super().__init__(confused_seconds, decoratee)
        self.possibles_ways: list[typing.Callable[[mob.Mob, map.GameMap], tuple[float, float] | None]] = [
            self.shift_up,
            self.shift_down,
            self.shift_left,
            self.shift_right,
        ]

    def move(self, entity: mob.Mob, game_map: map.GameMap) -> tuple[float, float] | None:
        """Move logic.

        Args:
            entity (mob.Mob): Description of entity.
            game_map (GameMap): Description of game_map.

        Returns:
            None: Description of return value
        """

        if time.time() >=  self.start_time + self.confused_seconds:
            self.decoratee.move(entity, game_map)
            return

        x = randint(0, 3)

        return self.possibles_ways[x](entity, game_map)

    def shift_up(self, entity: mob.Mob, game_map: map.GameMap) -> tuple[float, float] | None:
        """shift_up logic.

        Args:
            entity (mob.Mob): Description of entity.
            game_map (GameMap): Description of game_map.

        Returns:
            None: Description of return value
        """
        x = entity.xcor()
        y = entity.ycor() + game_map.move_size
        if game_map.check_walls(x, y):
            return (x, y)

        return None

    def shift_down(self, entity: mob.Mob, game_map: map.GameMap) -> tuple[float, float] | None:
        """shift_down logic.

        Args:
            entity (mob.Mob): Description of entity.
            game_map (GameMap): Description of game_map.

        Returns:
            None: Description of return value
        """
        x = entity.xcor()
        y = entity.ycor() - game_map.move_size
        if game_map.check_walls(x, y):
            return (x, y)

        return None

    def shift_left(self, entity: mob.Mob, game_map: map.GameMap) -> tuple[float, float] | None:
        """shift_left logic.

        Args:
            entity (mob.Mob): Description of entity.
            game_map (GameMap): Description of game_map.

        Returns:
            None: Description of return value
        """
        x = entity.xcor() - game_map.move_size
        y = entity.ycor()
        if game_map.check_walls(x, y):
            return (x, y)

        return None

    def shift_right(self, entity: mob.Mob, game_map: map.GameMap) -> tuple[float, float] | None:
        """shift_right logic.

        Args:
            entity (mob.Mob): Description of entity.
            game_map (GameMap): Description of game_map.

        Returns:
            None: Description of return value
        """
        x = entity.xcor() + game_map.move_size
        y = entity.ycor()
        if game_map.check_walls(x, y):
            return (x, y)

        return None
