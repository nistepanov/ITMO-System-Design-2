import turtle

from roguelike.entities.abstract_object import AbstractObject


class Artifact(AbstractObject):
    """Artifact logic."""

    def __init__(self, bonus_value: int) -> None:
        super().__init__()
        self.bonus_value = bonus_value

    @staticmethod
    def get_label() -> str:
        """get_label logic."""
        raise NotImplementedError


class Weapon(Artifact):
    """Weapon logic."""

    def __init__(self, bonus_value: int) -> None:
        super().__init__(bonus_value)
        self.penup()
        turtle.register_shape(super().get_resources_path() + '/weapon.gif')
        self.shape(super().get_resources_path() + '/weapon.gif')

    @staticmethod
    def get_label() -> str:
        """get_label logic."""
        return 'W'


class Shield(Artifact):
    """Shield logic."""

    def __init__(self, bonus_value: int) -> None:
        super().__init__(bonus_value)
        self.penup()
        turtle.register_shape(super().get_resources_path() + '/shield.gif')
        self.shape(super().get_resources_path() + '/shield.gif')

    @staticmethod
    def get_label() -> str:
        """get_label logic."""
        return 'S'
