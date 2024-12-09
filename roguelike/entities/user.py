import turtle
import typing

from roguelike.entities import abstract_object, artifact


# from roguelike.map import map


class User(abstract_object.AbstractObject):
    """User logic."""

    def __init__(self, move_size: int) -> None:
        super().__init__()
        turtle.register_shape(super().get_resources_path() + '/hero.gif')
        self.shape(super().get_resources_path() + '/hero.gif')
        self._health: int = 300
        self._move_size: int = move_size
        self._damage: int = 10
        self._active_inventory: list[artifact.Artifact] = []
        self._passive_inventory: list[artifact.Artifact] = []
        self.experience = 0
        self.level = 1
        self.penup()
        self.speed(3)

    @staticmethod
    def get_label() -> str:
        """get_label logic.

        Returns:
            str: Description of return value
        """
        return 'P'

    def shift_up(self, game_map: typing.Any) -> None:
        """shift_up logic.

        Args:
            game_map (GameMap): Description of game_map.

        Returns:
            None: Description of return value
        """
        x = self.xcor()
        y = self.ycor() + self._move_size
        if game_map.check_walls(x, y):
            self.goto(x, y)

    def shift_down(self, game_map: typing.Any) -> None:
        """shift_down logic.

        Args:
            game_map (GameMap): Description of game_map.

        Returns:
            None: Description of return value
        """
        x = self.xcor()
        y = self.ycor() - self._move_size
        if game_map.check_walls(x, y):
            self.goto(x, y)

    def shift_left(self, game_map: typing.Any) -> None:
        """shift_left logic.

        Args:
            game_map (GameMap): Description of game_map.

        Returns:
            None: Description of return value
        """
        x = self.xcor() - self._move_size
        y = self.ycor()
        if game_map.check_walls(x, y):
            self.goto(x, y)

    def shift_right(self, game_map: typing.Any) -> None:
        """shift_right logic.

        Args:
            game_map (GameMap): Description of game_map.

        Returns:
            None: Description of return value
        """
        x = self.xcor() + self._move_size
        y = self.ycor()
        if game_map.check_walls(x, y):
            self.goto(x, y)

    def get_item(self, game_map: typing.Any) -> None:
        """get_item logic.

        Args:
            game_map (GameMap): Description of game_map.

        Returns:
            None: Description of return value
        """
        for _, item in enumerate(game_map.items):
            if item.xcor() == self.xcor() and item.ycor() == self.ycor():
                self._active_inventory.append(item)
                if isinstance(item, artifact.Weapon):
                    self._damage += item.bonus_value
                elif isinstance(item, artifact.Shield):
                    self._health += item.bonus_value
                item.hideturtle()
                return

    def throw_item(self) -> None:
        """throw_item logic.

        Returns:
            None: Description of return value
        """
        item = self._active_inventory[0]
        self._active_inventory.remove(item)
        if isinstance(item, artifact.Weapon):
            self._damage -= item.bonus_value
        elif isinstance(item, artifact.Shield):
            self._health -= item.bonus_value
        self._passive_inventory.append(item)
