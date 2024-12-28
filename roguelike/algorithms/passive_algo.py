from roguelike.algorithms import mob_algorithm
from roguelike.entities import mob
from roguelike.map import map


class PassiveAlgo(mob_algorithm.MobAlgorithm):
    """SimpleAlgo logic."""

    def __init__(self) -> None:
        super().__init__()

    def move(self, entity: mob.Mob, game_map: map.GameMap) -> tuple[float, float] | None:
        """Move logic.

        Args:
            entity (mob.Mob): Description of entity.
            game_map (GameMap): Description of game_map.

        Returns:
            None: Description of return value
        """
        return (entity.xcor(), entity.ycor())
