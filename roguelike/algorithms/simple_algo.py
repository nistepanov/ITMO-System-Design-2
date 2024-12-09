import typing
from random import randint

from roguelike.algorithms import mob_algorithm
from roguelike.entities import mob
from roguelike.map import map


class SimpleAlgo(mob_algorithm.MobAlgorithm):
    """SimpleAlgo logic."""

    def __init__(self) -> None:
        super().__init__()
        self.possibles_ways: list[typing.Callable[[mob.Mob, map.GameMap], None]] = [
            self.shift_up,
            self.shift_down,
            self.shift_left,
            self.shift_right,
        ]

    def move(self, entity: mob.Mob, game_map: map.GameMap) -> None:
        """Move logic.

        Args:
            entity (mob.Mob): Description of entity.
            game_map (GameMap): Description of game_map.

        Returns:
            None: Description of return value
        """
        x = randint(0, 3)
        self.possibles_ways[x](entity, game_map)

    def shift_up(self, entity: mob.Mob, game_map: map.GameMap) -> None:
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
            entity.goto(x, y)

    def shift_down(self, entity: mob.Mob, game_map: map.GameMap) -> None:
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
            entity.goto(x, y)

    def shift_left(self, entity: mob.Mob, game_map: map.GameMap) -> None:
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
            entity.goto(x, y)

    def shift_right(self, entity: mob.Mob, game_map: map.GameMap) -> None:
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
            entity.goto(x, y)
