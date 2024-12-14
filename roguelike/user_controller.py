import typing


class UserController:
    def __init__(self, user, map, move_size):
        self.user = user
        self.map = map
        self._move_size: int = move_size



    def shift_up(self, game_map: typing.Any) -> None:
        """shift_up logic.

        Args:
            game_map (GameMap): Description of game_map.

        Returns:
            None: Description of return value
        """
        x = self.user.xcor()
        y = self.user.ycor() + self._move_size
        if game_map.check_walls(x, y):
            self.user.goto(x, y)

    def shift_down(self, game_map: typing.Any) -> None:
        """shift_down logic.

        Args:
            game_map (GameMap): Description of game_map.

        Returns:
            None: Description of return value
        """
        x = self.user.xcor()
        y = self.user.ycor() - self._move_size
        if game_map.check_walls(x, y):
            self.user.goto(x, y)

    def shift_left(self, game_map: typing.Any) -> None:
        """shift_left logic.

        Args:
            game_map (GameMap): Description of game_map.

        Returns:
            None: Description of return value
        """
        x = self.user.xcor() - self._move_size
        y = self.user.ycor()
        if game_map.check_walls(x, y):
            self.user.goto(x, y)

    def shift_right(self, game_map: typing.Any) -> None:
        """shift_right logic.

        Args:
            game_map (GameMap): Description of game_map.

        Returns:
            None: Description of return value
        """
        x = self.user.xcor() + self._move_size
        y = self.user.ycor()
        if game_map.check_walls(x, y):
            self.user.goto(x, y)

    def get_item(self, game_map: typing.Any) -> None:
        """get_item logic.

        Args:
            game_map (GameMap): Description of game_map.

        Returns:
            None: Description of return value
        """

        for _, item in enumerate(game_map.items):
            if item.xcor() == self.user.xcor() and item.ycor() == self.user.ycor():
                stats = self.user.inventory.add_item(item)
                self.update_damage(stats.damage)
                self.update_health(stats.health)
                return

    def throw_item(self, index : int) -> None:
        """throw_item logic.

        Returns:
            None: Description of return value
        """
        item = self.user.inventory.active_items[index]
        if item.item == None:
            return
        stats = self.user.inventory.deactivate_item(index)
        self.update_damage(stats.damage)
        self.update_health(stats.health)

    def activate_item(self, index : int) -> None:
        """throw_item logic.

        Returns:
            None: Description of return value
        """
        item = self.user.inventory.inventory[index]
        if item.item == None:
            return
        stats = self.user.inventory.activate_item(index)

        self.update_damage(stats.damage)
        self.update_health(stats.health)


    def update_damage(self, delta : int) -> None:
        self.user.damage += delta
        self.map.weapon_slot.clear()
        self.map.weapon_slot.write(str(self.user.damage), align="center", font=("Arial", 40, "normal"))


    def update_health(self, delta : int) -> None:
        self.user.health += delta
        self.map.shield_slot.clear()
        self.map.shield_slot.write(str(self.user.health), align="center", font=("Arial", 40, "normal"))
