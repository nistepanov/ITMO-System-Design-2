import turtle

from roguelike.entities.abstract_object import AbstractObject


class Image(AbstractObject):
    """Wall logic."""

    def __init__(self, image_path) -> None:
        super().__init__()
        turtle.register_shape(super().get_resources_path() + image_path)
        self.shape(super().get_resources_path() + image_path)
        self.penup()
        self.level = 1

    @staticmethod
    def get_label() -> str:
        """get_label logic.

        Returns:
            str: Description of return value
        """
        return 'W'

