import typing

from roguelike.entities.user import User


class UserController:
    """UserController logic."""

    def __init__(self, user: User, game_map: typing.Any, move_size: int) -> None:
        self.user = user
        self.game_map = game_map
        self._move_size = move_size
        self.font = ('Arial', 40, 'normal')

    def shift_up(self) -> None:
        """shift_up logic.

        Args:
            game_map (GameMap): Description of game_map.

        Returns:
            None: Description of return value
        """
        x = self.user.xcor()
        y = self.user.ycor() + self._move_size
        if self.game_map.check_walls(x, y):
            self.user.goto(x, y)

    def shift_down(self) -> None:
        """shift_down logic.

        Args:
            game_map (GameMap): Description of game_map.

        Returns:
            None: Description of return value
        """
        x = self.user.xcor()
        y = self.user.ycor() - self._move_size
        if self.game_map.check_walls(x, y):
            self.user.goto(x, y)

    def shift_left(self) -> None:
        """shift_left logic.

        Args:
            game_map (GameMap): Description of game_map.

        Returns:
            None: Description of return value
        """
        x = self.user.xcor() - self._move_size
        y = self.user.ycor()
        if self.game_map.check_walls(x, y):
            self.user.goto(x, y)

    def shift_right(self) -> None:
        """shift_right logic.

        Args:
            game_map (GameMap): Description of game_map.

        Returns:
            None: Description of return value
        """
        x = self.user.xcor() + self._move_size
        y = self.user.ycor()
        if self.game_map.check_walls(x, y):
            self.user.goto(x, y)

    def get_item(self) -> None:
        """get_item logic.

        Args:
            game_map (GameMap): Description of game_map.

        Returns:
            None: Description of return value
        """
        for _, item in enumerate(self.game_map.items):
            if item.xcor() == self.user.xcor() and item.ycor() == self.user.ycor():
                stats = self.user.inventory.add_item(item)
                self.update_damage(stats.damage)
                self.update_health(stats.health)
                return

    def deactivate_item(self, index: int) -> None:
        """throw_item logic.

        Returns:
            None: Description of return value
        """
        item = self.user.inventory.active_items[index]
        if item.item is None:
            return
        stats = self.user.inventory.deactivate_item(index)
        self.update_damage(stats.damage)
        self.update_health(stats.health)

    def activate_item(self, index: int) -> None:
        """throw_item logic.

        Returns:
            None: Description of return value
        """
        item = self.user.inventory.inventory[index]
        if item.item is None:
            return
        stats = self.user.inventory.activate_item(index)

        self.update_damage(stats.damage)
        self.update_health(stats.health)

    def update_damage(self, delta: int) -> None:
        """update_damage logic.

        Returns:
            None: Description of return value
        """
        self.user.damage += delta
        self.game_map.weapon_slot.clear()
        self.game_map.weapon_slot.write(str(self.user.damage), align='center', font=self.font)

    def update_health(self, delta: int) -> None:
        """update_health logic.

        Returns:
            None: Description of return value
        """
        self.user.health += delta
        self.game_map.shield_slot.clear()
        if self.user.health <= 0:
            self.user.health = 0
            self.user.hideturtle()
        self.game_map.shield_slot.write(str(self.user.health), align='center', font=self.font)

    def update_xp(self, delta: int) -> None:
        """update_health logic.

        Returns:
            None: Description of return value
        """
        self.user.experience += delta
        if self.user.experience >= 5:
            self.update_level()
            self.user.experience = 0

    def update_level(self) -> None:
        """update_health logic.

        Returns:
            None: Description of return value
        """
        self.game_map.experience_slot.clear()
        self.user.level += 1
        self.update_health(1)
        self.update_damage(1)
        self.game_map.experience_slot.write(str(self.user.level), align='center', font=self.font)
