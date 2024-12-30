import typing

from roguelike.algorithms import mob_algorithm


class AgressiveAlgo(mob_algorithm.MobAlgorithm):
    """SimpleAlgo logic."""

    def __init__(self) -> None:
        super().__init__()

    def move(self, entity: typing.Any, game_map: typing.Any) -> tuple[float, float] | None:
        """Move logic.

        Args:
            entity (mob.Mob): Description of entity.
            game_map (GameMap): Description of game_map.

        Returns:
            None: Description of return value
        """
        x = entity.xcor()
        y = entity.ycor()
        user_x = game_map.user.xcor()
        user_y = game_map.user.ycor()

        if x < user_x:
            new_x = x + game_map.move_size
            if game_map.check_walls(new_x, y):
                return (new_x, y)
        elif x > user_x:
            new_x = x - game_map.move_size
            if game_map.check_walls(new_x, y):
                return (new_x, y)
        if y < user_y:
            new_y = y + game_map.move_size
            if game_map.check_walls(x, new_y):
                return (x, new_y)
        elif y > user_y:
            new_y = y - game_map.move_size
            if game_map.check_walls(x, new_y):
                return (x, new_y)

        return None
