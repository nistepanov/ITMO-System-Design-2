import turtle

from roguelike.entities.abstract_object import AbstractObject


class Wall(AbstractObject):
    """Wall logic."""

    def __init__(self) -> None:
        super().__init__()
        turtle.register_shape(super().get_resources_path() + '/wall.gif')
        self.shape(super().get_resources_path() + '/wall.gif')
        self.penup()
        self.level = 1

    @staticmethod
    def get_label() -> str:
        """get_label logic.

        Returns:
            str: Description of return value
        """
        return 'W'
