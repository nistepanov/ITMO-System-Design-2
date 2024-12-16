import turtle

from roguelike.entities.abstract_object import AbstractObject
from roguelike.entities.artifact import Artifact


class InventorySlot(AbstractObject):
    """InventorySlot logic."""

    def __init__(self) -> None:
        super().__init__()
        turtle.register_shape(super().get_resources_path() + '/slot.gif')
        self.shape(super().get_resources_path() + '/slot.gif')
        self.penup()
        self.level = 1
        self.item: Artifact | None = None

    @staticmethod
    def get_label() -> str:
        """get_label logic.

        Returns:
            str: Description of return value
        """
        return 'IS'
