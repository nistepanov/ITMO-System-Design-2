from roguelike.entities import artifact, mob, user
from roguelike.entities.text_object import TextObject
from roguelike.inventory import inventory


class GameMap:
    """GameMap logic."""

    def __init__(
        self,
        walls: list[tuple[int, int]],
        mobs: list[mob.Mob],
        items: list[artifact.Weapon | artifact.Shield],
        user_: user.User,
        move_size: int,
        inventory: inventory.Inventory,
        experience_slot: TextObject | None,
        weapon_slot: TextObject | None,
        shield_slot: TextObject | None,
    ) -> None:
        self.walls = walls
        self.mobs = mobs
        self.items = items
        self.user = user_
        self.move_size = move_size
        self.inventory = inventory
        self.experience_slot = experience_slot
        self.weapon_slot = weapon_slot
        self.shield_slot = shield_slot

    def check_walls(self, x: float, y: float) -> bool:
        """check_walls logic.

        Args:
            x (float): Coord of x.
            y (float): Coord of y.

        Returns:
            bool: Is coordinates not covered by walls.
        """
        return (x, y) not in self.walls

    def is_user(self, x: float, y: float) -> bool:
        """check_user logic.

        Args:
            x (float): Coord of x.
            y (float): Coord of y.

        Returns:
            bool: Is coordinates covered by users.
        """
        return x == self.user.xcor() and y == self.user.ycor()
